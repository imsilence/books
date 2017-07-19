# pyre2 #

## 为欸什么要使用 pyre2 ##

## 安装re2 ##

1. [下载]("https://codeload.github.com/google/re2/tar.gz/2017-05-01" "re2") https://github.com/google/re2/releases
2. 解压

    ```
    tar zvxf re2-2017-05-01.tar.gz
    ```

3. 编译安装

    ```
    cd re2-2017-05-01/ && make CFLAGS='-fPIC -c -Wall -Wno-sign-compare -O3 -g -I.' && sudo make install
    ```

## 安装pyre2 ##


1. 安装python-dev

    ```
    sudo apt install python-dev
    ```

2. 设置编译环境变量

        env CPPFLAGS='-I/home/silence/Downloads/re2-2017-05-01/re2' LDFLAGS='-L/home/silence/Downloads/re2-2017-05-01/obj/so'

3. [下载]("https://codeload.github.com/facebook/pyre2/tar.gz/v1.0.5" "pyre2") https://github.com/facebook/pyre2/releases
4. 解压

    ```
    tar zvxf pyre2-1.0.5.tar.gz
    ```

5. 编译安装

    ```
    cd pyre2-1.0.5 && sudo python setup.py install
    ```

## 测试 ##

```
import re2
print(re2.match('[a-zA-Z]+$', 'abc'))
print(re2.match('[a-zA-Z]+$', 'abc1'))
print(re2.search('[a-zA-Z]+$', 'abc'))
print(re2.search('[a-zA-Z]+$', 'abc1'))
regex = re2.compile('[a-zA0Z]+$')
print(regex.match('abc'))
print(regex.match('abc1'))
print(regex.search('abc'))
print(regex.search('abc1'))
```
