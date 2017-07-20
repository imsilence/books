# ctypes #

用于调用动态链接库, 创建C语言中的数据类型和底层操作函数

## 使用动态链接库 ##

window上叫dll(Dynamic link libraries), \*nix上叫so(Shard objects)

在window中调用printf函数(c:/windows/system32/msvcrt.dd中)

```
from ctypes import cdll

cdll.msvcrt.printf('Hello, %s\n', 'Silence')
```

在Linux中调用printf函数(libc.so.6)

```
from ctypes import CDLL|
libc = CDLL('libc.so.6')
libc.printf('Hello, %s\n', 'Silence')
```

## 构建C语言数据类型 ##

常用基本数据类型

| c | ctypes | comment |
|---|--------|---------|
|bool|c_bool|布尔类型|
|char|c_char|字符类型|
|wchar|c_wchar|unicode字符类型|
|short int|c_short|短整型|
|int|c_int|整数类型|
|unsigned int|c_uint|无符号整数类型|
|long|c_long|长整型|
|longlong|c_longlong|长长整型|
|float|c_float|浮点型|
|double|c_double|双浮点型|
|void *|c_void_p|无类型指针|
|char *|c_char_p|字符指针|
|wchar *|c_wchar_p|unicode字符指针|

结构体类型

```
class Person(ctypes.Structure):
    _fields_ = [
        ('name', c_char * 25),
        ('password', c_char * 32),
        ('age', c_int)
    ]
```

联合体类型

```
class Color(ctypes.Union):
    _fields_ = [
        ('name', c_char * 25),
        ('rgb', c_long)
    ]
```
