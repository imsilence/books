# bash 日志分析 #

## 配置记录 bash 日志(ubuntu 16.04) ##

1. 在 /etc/profile.d/history_command.sh 中添加sh代码

        #export HISTTIMEFORMAT="[%Y-%m-%d %H:%M:%S] [`who am i | awk '{print $NF}' | sed -e 's/[()]//g'`] "
        export HISTTIMEFORMAT=""
        export LOGIN_ADDR=`who am i | awk '{print $NF}' | sed -e 's/[()]//g'`;
        export PROMPT_COMMAND='
        if [ -z "$OLD_PWD" ];then
            export OLD_PWD=$PWD;
        fi;
        if [ ! -z "$LAST_CMD" ] && [ "$(history 1)" != "$LAST_CMD" ]; then
            logger -t shell_cmd "`whoami` `date +\"[%Y-%m-%d %H:%M:%S]\"` [$LOGIN_ADDR] $PWD `history 1 | cut -c 8-`";               
        fi;
        export LAST_CMD="$(history 1)";
        export OLD_PWD=$PWD;'

    说明:

        a. HISTTIMEFORMAT 配置历史命令格式
        b. LOGIN_ADDR 获取当前登录者的IP地址
        c. PROMPT_COMMAND  环境变量设置的命令会在用户提示符之前被执行

2. 立即生效配置文件

        source /etc/profile


## 测试 ##

1. tailf查看日志记录文件/var/log/syslog

        tail -n 0 -f /var/log/syslog

2. 在系统中执行命令:

        ls -la
        pwd

    查看日志信息

        May 15 10:31:07 silence shell_cmd: silence [2017-05-15 10:31:07] [192.168.46.1] /home/silence ls -la
        May 15 10:31:10 silence shell_cmd: silence [2017-05-15 10:31:10] [192.168.46.1] /home/silence pwd

## 日志格式 ##

|字段|含义|
|---|---|
|May 15 10:31:07|日志时间, 由syslog产生|
|silence|主机名|
|shell_cmd:|日志前缀|
|silence|登录用户|
|2017-05-15 10:31:07|执行命令时间|
|192.168.46.1|登录IP地址|
|/home/silence|所在目录|
|ls -la|命令|
