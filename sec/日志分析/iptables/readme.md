# iptables 日志分析 #

## 用途 ##

防火墙除了进行有效的网络访问控制之外，还可以清晰记录网络上的访问，并自动生成日志进行保存. 在防火墙日志中主要记录消息发送源IP、消息目的IP、消息流向、消息内容以及应用几个方面.管理员可以按照不同的需求查找日志、审计日志，还可以分析网络带宽利用，各种协议和端口的使用情况，防火墙产生的安全告警对网络安全管理提供帮助信息


## 配置iptables 日志(ubuntu 16.04) ##


1. 配置 /etc/rsyslog.d/30-iptables.conf文件内容，将消息内容包含iptables: 的日志写入到 /var/log/iptables.log中

        :msg,contains,"iptables:" /var/log/iptables.log

2. 重启rsyslog服务

        /etc/init.d/rsyslog restart

3. 配置记录日志规则

        iptables -N SILENCE_INPUT_LOG
        iptables -I INPUT 1 -j SILENCE_INPUT_LOG

        iptables -A SILENCE_INPUT_LOG -p tcp --dport 8080 -j LOG --log-prefix "iptables:"
        iptables -A SILENCE_INPUT_LOG -p icmp -j LOG --log-prefix "iptables:"
        iptables -A SILENCE_INPUT_LOG -p tcp --dport 8081 -j LOG --log-prefix "iptables:"
        iptables -A SILENCE_INPUT_LOG -p udp --dport 8082 -j LOG --log-prefix "iptables:"

4. tail 查看 iptables.log 文件

        tail -n 0 -f /var/log/iptables.log

5. 测试

    web测试
        a. 使用curl命令访问目标的8080端口, 查看iptables.log:

            curl -XGET "192.168.1.116:8080"

            产生日志:

                May 14 17:57:53 silence kernel: [80156.647246] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=52 TOS=0x00 PREC=0x00 TTL=64 ID=10065 DF PROTO=TCP SPT=39548 DPT=8080 WINDOW=8192 RES=0x00 SYN URGP=0
                May 14 17:57:54 silence kernel: [80157.157241] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=52 TOS=0x00 PREC=0x00 TTL=64 ID=10067 DF PROTO=TCP SPT=39548 DPT=8080 WINDOW=8192 RES=0x00 SYN URGP=0
                May 14 17:57:54 silence kernel: [80157.663905] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=48 TOS=0x00 PREC=0x00 TTL=64 ID=10069 DF PROTO=TCP SPT=39548 DPT=8080 WINDOW=8192 RES=0x00 SYN URGP=0

        c. 启动web服务器:

            python3 -mhttp.server --bind 0.0.0.0 8080

        d. 再次使用curl命令访问目标的8080端口, 查看iptables.log:

            curl -XGET "192.168.1.116:8080"

            产生日志:

                May 14 17:58:41 silence kernel: [80204.153519] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=52 TOS=0x00 PREC=0x00 TTL=64 ID=10313 DF PROTO=TCP SPT=39609 DPT=8080 WINDOW=8192 RES=0x00 SYN URGP=0
                May 14 17:58:41 silence kernel: [80204.522080] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=40 TOS=0x00 PREC=0x00 TTL=64 ID=10314 DF PROTO=TCP SPT=39609 DPT=8080 WINDOW=16425 RES=0x00 ACK URGP=0
                May 14 17:58:41 silence kernel: [80204.522164] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=122 TOS=0x00 PREC=0x00 TTL=64 ID=10315 DF PROTO=TCP SPT=39609 DPT=8080 WINDOW=16425 RES=0x00 ACK PSH URGP=0
                May 14 17:58:41 silence kernel: [80204.535677] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=40 TOS=0x00 PREC=0x00 TTL=64 ID=10317 DF PROTO=TCP SPT=39609 DPT=8080 WINDOW=16425 RES=0x00 ACK URGP=0
                May 14 17:58:41 silence kernel: [80204.544903] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=40 TOS=0x00 PREC=0x00 TTL=64 ID=10318 DF PROTO=TCP SPT=39609 DPT=8080 WINDOW=16425 RES=0x00 ACK URGP=0
                May 14 17:58:41 silence kernel: [80204.553159] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=40 TOS=0x00 PREC=0x00 TTL=64 ID=10320 DF PROTO=TCP SPT=39609 DPT=8080 WINDOW=16425 RES=0x00 ACK FIN URGP=0

    icmp测试

        a. 使用ping命令访问目标, 查看iptables.log:

            ping 192.168.1.116 -c 1

            产生日志:

                May 14 18:11:29 silence kernel: [80972.571111] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=12568 PROTO=ICMP TYPE=8 CODE=0 ID=1 SEQ=106

    TCP测试

        a. 使用nc命令创建服务

            nc -l 0.0.0.0 8081

        b. 使用nc命令访问目标的8081端口, 查看iptables.log

            echo "hello world" | nc 192.168.1.116 8081

            产生日志:

                May 14 18:27:37 silence kernel: [81940.888216] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=52 TOS=0x00 PREC=0x00 TTL=64 ID=19910 DF PROTO=TCP SPT=42178 DPT=8081 WINDOW=8192 RES=0x00 SYN URGP=0
                May 14 18:27:37 silence kernel: [81940.891373] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=40 TOS=0x00 PREC=0x00 TTL=64 ID=19911 DF PROTO=TCP SPT=42178 DPT=8081 WINDOW=16425 RES=0x00 ACK URGP=0
                May 14 18:27:37 silence kernel: [81940.894137] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=56 TOS=0x00 PREC=0x00 TTL=64 ID=19912 DF PROTO=TCP SPT=42178 DPT=8081 WINDOW=16425 RES=0x00 ACK PSH URGP=0
                May 14 18:27:40 silence kernel: [81943.873860] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=40 TOS=0x00 PREC=0x00 TTL=64 ID=19919 DF PROTO=TCP SPT=42178 DPT=8081 WINDOW=0 RES=0x00 ACK RST URGP=0

    UDP测试

    a. 使用nc命令创建服务

        nc -l -u 0.0.0.0 8082

    b. 使用nc命令访问目标的8081端口, 查看iptables.log

        echo "hello world" | nc -u 192.168.1.116 8082

        产生日志:

            May 14 18:30:10 silence kernel: [82093.478533] iptables:IN=wlp6s0 OUT= MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00 SRC=192.168.1.105 DST=192.168.1.116 LEN=44 TOS=0x00 PREC=0x00 TTL=64 ID=23082 PROTO=UDP SPT=57747 DPT=8082 LEN=24


## 日志格式 ##

|字段|含义|
|---|---|
|May 14 17:57:53|日志时间, 由syslog产生|
|silence|主机名|
|kernel|进程名称,说明netfilter由内核运行|
|80156.647246||
|iptables:|日志前缀, 通过--log-prefix配置|
|IN=wlp6s0|数据包进入的接口,若为表示本地产生|
|OUT=|数据包离开的接口,若为空表示本地接收|
|MAC=00:26:c6:54:89:be:ec:0e:c4:3e:e3:e9:08:00|00:26:c6:54:89:be为目的MAC地址, ec:0e:c4:3e:e3:e9为源MAC地址|
|08:00|表示上层协议代码, IP协议|
|SRC=192.168.1.105|源IP地址|
|DST=192.168.1.116|目的IP地址|
|LEN=52|IP头长度,字节(MTU)|
|TOS=0x00|服务字段|
|PREC=0x00|服务类型的优先级字段|
|TTL=64|IP数据包的生存时间|
|ID=10065|IP数据包标识|
|DF|标识不分段|
|PROTO=TCP|传输层协议类型, 其他ICMP, UDP|
|SPT=39548|源端口|
|DPT=8080|目的端口|
|LEN=24|传输层协议头长度|
|WINDOW=8192|窗口大小|
|RES=0x00|保留值|
|SYN|TCP标志位, 其他CWR, ECE, URG, ACK, PSH, RST, FIN|
|URGP=0|紧急指针起点|
|TYPE=8 CODE=0 ID=1 SEQ=106|ICMP协议出现|
