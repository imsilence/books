title: deb源搭建
date: 2015-12-18 16:20:21
tags: [deb]
categories: [linux]
---

## 为什么要搭建deb源 ##
1. 公司网络隔离, 有一部分服务器不允许链接外网
2. 自己开发的安装程序需要统一管理

## 搭建步骤 ##

1. 在一个可以连接外网的机器上使用apt-get安装程序

`apt-get install python-dev`

2. 将使用apt-get安装的缓存拷贝到/tmp/debs目录下

```
mkdir -p /tmp/debs
cd /var/cache/apt

find . -name "*.deb" | xargs -i cp -rf {} /tmp/debs/
```

3. 构建deb描述文件

安装deb描述文件构建工具

`apt-get install -y --force-yes dpkg-deb` 

创建描述文件
```
cd /tmp/
rm -fr debs/Packages.gz
dpkg-scanpackages debs/ | gzip > debs/Packages.gz
```

4. 安装apache服务器

`apt-get install apache2`

5. 部署deb源

`cp -rf /tmp/debs /var/www/html/`

## 使用 ##

1. 在sources.list中添加内网deb源地址

`echo "deb http://ip debs/ " >> /etc/apt/sources.list`

2. 使用apt-get安装程序