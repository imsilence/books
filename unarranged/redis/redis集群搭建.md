title: redis集群搭建
date: 2016-01-27 09:53:21
tags: [redis集群搭建]
categories: [redis]
---

1. master配置
daemonize yes

2. slave配置

daemonize yes
slaveof master-ip 6379
