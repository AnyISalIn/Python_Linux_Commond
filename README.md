# Python_Linux_Commond

本仓库代码仅支持 `python 3`, 均在 `python 3.5.2` 版本中测试过.

## pycat

```shell
$ python pycat.py --help
Usage: pycat.py [options] [filename, ...]

Options:
      --version     show program version number and exit
      -h, --help    show this help message and exit
      -n, --number  show line numbers

```

```shell
# 打开一个文件
$ python pycat.py testfile
{
        "auth": "admin",
        "password": "passwd"

}

#打开多个文件

$ python pycat.py ~/num.txt ~/person.json ~/hello.rb
1 2 3 4
{
        "auth": "admin",
        "password": "passwd"

}
#!/usr/bin/ruby
puts "Hello World";

# 显示行号
$ python pycat.py -n testfile
1 {
2     "auth": "admin",
3     "password": "passwd"
4 }

```
