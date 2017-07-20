# docker应用搭建 #
## 部署结构 ##

```
          |--->django app--->|                   |--->redis-slave
haproxy---|                  |--->redis master---|
          |--->django app--->|                   |--->redis-slave
```

## 获取所有镜像 ##

```
docker pull index.alauda.cn/library/ubuntu
docker pull index.alauda.cn/library/django
docker pull index.alauda.cn/library/redis
docker pull index.alauda.cn/library/haproxy
```

## 启动容器 ##

```
docker run -it --name redis-master index.alauda.cn/library/redis /bin/bash
docker run -it --name redis-slave-01 --link redis-master:master index.alauda.cn/library/redis /bin/bash
docker run -it --name redis-slave-02 --link redis-master:master index.alauda.cn/library/redis /bin/bash
docker run -it --name django-app-01 --link redis-master:redis -v ~/Documents/Codes/docker/03/app01:/usr/src/app index.alauda.cn/library/django /bin/bash
docker run -it --name django-app-02 --link redis-master:redis -v ~/Documents/Codes/docker/03/app02:/usr/src/app index.alauda.cn/library/django /bin/bash
docker run -it --name haproxy --link django-app-01:app01 --link django-app-02:app02 -v ~/Documents/Codes/docker/03/haproxy:/tmp i -p 8080:8080 ndex.alauda.cn/library/haproxy /bin/bash
```

## 配置redis ##

+ 查看redis-master挂在本地目录信息

```
docker inspect --format='{{.Mounts}}' redis-master
sudo cp ./03/redis/redis-master.conf /var/lib/docker/volumes/6236e83442ec9d1c335774f4fa8fb54ece0753ea14be5b63f50afd42b6327371/_data/
[{6236e83442ec9d1c335774f4fa8fb54ece0753ea14be5b63f50afd42b6327371 /var/lib/docker/volumes/6236e83442ec9d1c335774f4fa8fb54ece0753ea14be5b63f50afd42b6327371/_data /data local  true }]
```

docker启动时自动将目录`/var/lib/docker/volumes/6236e83442ec9d1c335774f4fa8fb54ece0753ea14be5b63f50afd42b6327371/_data`挂载到容器中的`/data`目录, 可以通过这两个目录实现本地和容器中文件交换

+ 将redis-master.conf拷贝到redis-master容器中

```
sudo cp ./03/redis/redis-master.conf /var/lib/docker/volumes/6236e83442ec9d1c335774f4fa8fb54ece0753ea14be5b63f50afd42b6327371/_data/
```

+ 在redis-master容器中启动redis-server
```
cd /data && redis-server redis-master.conf
```

+ 同redis-master配置将./03/redis/redis.conf拷贝到容器redis-slave-01和redis-slave-02中，并启动服务

+ 测试

在redis-master, redis-slave-01, redis-slave-02分别启动redis-cli， 在master中使用set test "1"设置redis数据，并在两个slave中使用get test获取master设置的数据

## 配置django app ##

+ 安装 python 3rd redis

```
pip install redis
```

+ 启动django app

```
cd /usr/src/app && python manage.py runserver 0.0.0.0:8080
```

## 配置haproxy ##

+ 启动haproxy

```
/usr/local/sbin/haproxy -f /tmp/haproxy.cfg
```

## 访问 ##

在浏览器中访问 [http://localhost:8080/home/](http://localhost:8080/home/ "home")，查看应用栈
