# acct & psacct 监控用户行为 #

## 介绍 ##

acct & psacct可用于监控系统上用户行为和消耗的资源

## 安装使用 ##

1. 安装
    a. ubuntu 16.04

        sudo apt install acct

    b. centos 6.8

        sudo yum install psacct

2. 启动\&停止

    a. ubuntu 16.04

        /etc/init.d/acct status     查看后台状态
        /etc/init.d/acct start      启动后台服务
        /etc/init.d/acct stop       停止后台服务
        accton on                   激活
        accton off                  禁用

    b. centos 6.8

        /etc/init.d/psacct status     查看后台状态
        /etc/init.d/psacct start      启动后台状态
        /etc/init.d/psacct stop       停止后台服务

3. 使用
    工具 ac, sa, lastcomm

    a. ac 统计用户连接时间

        ac                      显示所有用户连接总时间
        ac -p                   显示每个用户连接时间
        ac -d                   显示每天所有用户连接总时间
        ac silence              显示指定用户连接时间
        ac -d silence           显示指定用户每天连接时间

    b. sa 输出用户活动信息

        sa                      显示所有用户执行命令情况
        sa -u                   按用户显示执行命令情况
        sa -m                   按进程显示执行命令情况
        sa -p                   按使用率显示执行命令情况

    c. lastcomm 输出最近执行命令信息

        lastcomm                显示所有执行命令
        lastcomm silence        显示指定用户执行命令
        lastcomm ls             显示指定命令执行情况

4. 其他

        last        查看最近用户登录成功列表
        last -x     显示系统关机、重新开启等信息
        last -a     将IP显示在最后一列
        last -d     对IP进行域名解析
        last -R     不显示IP列
        last -n 3   显示最近3条
        lastb       查看最近用户登录失败的列表
