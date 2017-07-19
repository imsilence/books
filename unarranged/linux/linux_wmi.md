title: linux环境下通过WMI对windows进行软件部署
date: 2017-03-30 09:10:21
tags: [win]
categories: [linux]
---

## 目的 ##

需要在linux环境下对客户windows环境安装agent

## 环境准备 ##

### 安装 ###

安装包下载[WMI client (WMIC) for Linux]("http://www.openvas.org/download/wmi/" "WMI client (WMIC) for Linux")


### 测试 ###

1.通过wmic命令远程查询信息
```
# 查看计算机信息
wmic -U administrator%kk123456 //192.168.1.108 "select * from Win32_ComputerSystem"

# 查看操作系统信息
wmic -U administrator%kk123456 //192.168.1.108 "Select * from Win32_OperatingSystem"

# 查看进程信息
wmic -U administrator%kk123456 //192.168.1.108 "Select * from Win32_Process Where CommandLine like '%explorer%'"

# 查看进程监控信息
wmic -U administrator%kk123456 //192.168.1.108 "Select PrivateBytes from Win32_PerfFormattedData_PerfProc_Process"
```

2.通过winexe命令远程执行命令、

```
winexe -U administrator%kk123456 //192.168.1.108 "cmd /c ipconfig"
```

## 功能实现 ##

### 基本原理 ###

1.通过winexe远程调用echo命令，在windows机器上创建vbs脚本
    vbs脚本中远程下载安装包、执行安装脚本
2.通过winexe远程调用wscript执行vbs脚本

### 代码实现 ###

1.winexe_wrapper.py文件

代码功能: 调用winexe命令

```
#encoding: utf-8

import os
import subprocess
import logging
import traceback


logger = logging.getLogger(__name__)


def _command(args):                                                             #执行系统命令
    _process = subprocess.Popen(args, \
                                stdin=subprocess.PIPE, \
                                stdout=subprocess.PIPE, \
                                stderr=subprocess.PIPE, \
                                shell=True)
    _stdout, _stderr = _process.communicate()
    _returncode = _process.returncode
    return _returncode, _stdout, _stderr


class WinexeWrapper(object):

    def __init__(self, host, username, password):
        self.username = username
        self.password = password
        self.host = host
        self.bin = '/bin/winexe'

    def _make_credential_args(self):
        arguments = []
        userpass = '--user="{username}%{password}"'.format(
            username=self.username,
            password=self.password,
        )
        arguments.append(userpass)
        hostaddr = '"//{host}"'.format(host=self.host)
        arguments.append(hostaddr)
        return arguments

    def execute(self, cmds):
        credentials = self._make_credential_args()                              #拼接命令行中用户名密码参数
        if type(cmds) != type([]):
            cmds = [cmds]
        arguments = [self.bin] + credentials + cmds                             #拼接命令行参数
        return _command(' '.join(arguments))                                    #执行命令


def winexe(host, username, password, cmd):
    if os.name == 'nt':
        import wmi
        try:
            client = wmi.WMI(computer=host, user=username, password=password)
            return client.Win32_Process.Create(CommandLine=cmd)[1]
        except wmi.x_access_denied as e:
            logger.error(e)
            logger.exception(traceback.format_exc())
        except wmi.x_wmi as e:
            logger.error(e)
            logger.exception(traceback.format_exc())
        except BaseException as e:
            logger.error(e)
            logger.exception(traceback.format_exc())
        return -1
    else:
        client = WinexeWrapper(host=host, username=username, password=password)
        return client.execute("'{0}'".format(cmd))[0]


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    host = '192.168.1.108'
    username = 'administrator'
    password = 'kk123456'
    print winexe(host, username, password, 'cmd /c ipconfig')
```

2. install.py脚本

代码功能: 拼接执行创建vbs脚本，调用winexe接口远程执行

```
#encoding: utf-8
from __future__ import with_statement
from winexe_wrapper import WinexeWrapper

if __name__ == '__main__':
    host = '192.168.1.108'                                                      #win机器地址
    username = 'administrator'                                                  #win机器用户名
    password = 'kk123456'                                                       #win机器密码
    client = WinexeWrapper(host=host, username=username, password=password)     #创建WinexeWrapper对象

    vbs_file = r'c:\install'                                                    #vbs文件
    download_file_url = r'http://192.168.1.101/package.exe'                     #安装包下载位置
    install_file = r'c:\install.exe'                                            #安装包下载后保存文件
    log_file = r'c:\install.log'                                                #安装日志输出

    contents = [
        'Set Post = CreateObject("Msxml2.ServerXMLHTTP")',                      #创建vbs中HTTP(S)请求对象
        'Set Shell = CreateObject("Wscript.Shell")',                            #创建vbs中命令行对象
        'Set FSO = CreateObject("Scripting.FileSystemObject")',                 #创建vbs中文件系统对象
        'Post.setOption 2, 13056',                                              #设置HTTPS请求不检查服务器端证书
        'Post.Open "GET","{0}",0'.format(download_file_url),                    #请求下载URL
        'Post.Send()',                                                          #发送HTTP请求
        'Set aGet = CreateObject("ADODB.Stream")',                              #创建vbs中流对象
        'aGet.Mode = 3',                                                        #设置流对象模式(读、写)
        'aGet.Type = 1',                                                        #设置流对象类型(二进制类型)
        'aGet.Open()',                                                          #打开流对象
        'aGet.Write(Post.responseBody)',                                        #将HTTP(S)请求结果写入流对象
        'aGet.SaveToFile "{0}",2'.format(install_file),                         #保存流到安装包
        'wscript.sleep 5000',                                                   #休眠5s
        'Shell.Run "{0}", 0, True'.format(install_file),                        #同步执行安装脚本
        'wscript.sleep 1000',
        'FSO.DeleteFile("{0}"), True'.format(install_file),                     #删除下载的安装包
        'wscript.sleep 1000',
        'FSO.DeleteFile("{0}"), True'.format(vbs_file),                         #删除vbs脚本
    ]

    cmds = []

    cmds.append("echo Rem client install > {0}".format(vbs_file))               #重写vbs文件,第一行写入注释

    for content in contents:
        cmds.append('echo {0} >> "{1}"'.format(content, vbs_file))              #追加方式写入vbs文件

    cmds.append('wscript.exe /E:vbs "{0}" > {1}'.format(vbs_file, log_file))    #执行vbs脚本

    print client.execute("'cmd /c {0}'".format(' & '.join(cmds)))               #调用winexe命令
```


## 后续功能 ##

1.对winc进行封装, 通过查询执行进程是否存在判断是否安装成功
2.并行对不同机器进行安装
