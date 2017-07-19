title: rsync同步文件
date: 2016-01-05 11:38:21
tags: [rsync]
categories: [linux]
---

备份到远程机器
rsync -avz /var/www/html rget@192.168.1.1:/var/www/html
rsync -avz /usr/share/elasticsearch/data/audit_es/nodes/0/indices/event_20151013 wuke-c@10.120.100.165:/home/wuke-c/es_backups

备份到本地
#rsync -avz rget@192.168.1.1:/var/www/html /opt