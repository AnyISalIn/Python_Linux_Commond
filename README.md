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

## pyls

```shellscript
$ python pyls.py --help                                                                                                                                               
Usage: pyls.py [options] [path, ...]

Options:
  --version   show program's version number and exit
  -h, --help  show this help message and exit
  -l, --list  list
  -a, --all   show all
```

```shellscript
$ python pyls.py -a .
.git pycat.py pyfind.py pyls.py README.md

$ python pyls.py -l .
-rw-r--r--  1  anyisalin  staff  1.317K  pycat.py
-rw-r--r--  1  anyisalin  staff  4.411K  pyfind.py
-rw-r--r--  1  anyisalin  staff  1.739K  pyls.py
-rw-r--r--  1  anyisalin  staff  756  README.md

$ python pyls.py -la .
drwxr-xr-x  14  anyisalin  staff  476  .git
-rw-r--r--  1  anyisalin  staff  1.317K  pycat.py
-rw-r--r--  1  anyisalin  staff  4.411K  pyfind.py
-rw-r--r--  1  anyisalin  staff  1.739K  pyls.py
-rw-r--r--  1  anyisalin  staff  756  README.md

$ python pyls.py ~/ /
/Users/anyisalin/:
Applications codes Desktop Documents Downloads Library Movies Music Pictures Public wallpaper ycm ~
/:
Applications bin cores dev etc home installer.failurerequests Library net Network private sbin System tmp Users usr var Volumes
```

## pyfind

```shellscript
$ python pyfind.py --help
Usage: pyfind.py [options] [path, ...]

Options:
 --version             show program's version number and exit
 -h, --help            show this help message and exit
 -t TYPE, --type=TYPE
 -e DIR, --exclude=DIR
 -n FILE, --name=FILE
 -c TIMESTAMP, --ctime=TIMESTAMP
 -m TIMESTAMP, --mtime=TIMESTAMP
 -u UID, --uid=UID
 -g GID, --gid=GID
```

```shellscript
$ python pyfind.py  / -u 501 -g 20 -n 'aaa' -t file
/Users/anyisalin/codes/Python_Linux_Commond/aaa
/Users/anyisalin/.atom/compile-cache/coffee/b6aaa5c43b02afb32da4bc696251af6ae351d3bd.js
```
