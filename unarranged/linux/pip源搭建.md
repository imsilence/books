title: pip源搭建
date: 2015-12-18 16:50:21
tags: [pip]
categories: [linux]
---

## 为什么要搭建pip源 ##
1. 公司网络隔离, 有一部分服务器不允许链接外网
2. 自己开发的python安装程序需要统一管理

## 搭建步骤 ##

1. 在一个可以连接外网的机器上使用pip安装python 3rd并设置本地缓存

```
mkdir -p /tmp/pip/
pip install pyes --cache-dir  /tmp/pip
pip install -r requires_3rd.txt --cache-dir /tmp/pip
```

2.整理安装包文件
/tmp/pip
└─pyes
    └─pyes-0.99.6-py2-none-any.whl

3. 安装apache服务器

`apt-get install apache2`

4. 部署deb源

`cp -rf /tmp/pip /var/www/html/`

## 使用 ##

```
pip install pyes -i http://ip/pip
pip install -r requires_3rd.txt -I http://ip/pip
```