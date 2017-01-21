import os
import ipdb
import sys
from optparse import OptionParser
import stat

parser = OptionParser(usage="usage: %prog [path, ...] [option]",
                      version="%prog 1.0")
parser.add_option("-t", "--type",
                  action="store",
                  dest="type",
                  default="",
                  metavar="TYPE")
parser.add_option("-e", "--exclude",
                  action="store",
                  dest="ex",
                  default="",
                  metavar="DIR")
parser.add_option("-n", "--name",
                  action="store",
                  dest="pattern",
                  default="",
                  metavar="FILE")
parser.add_option("-c", "--ctime",
                  action="store",
                  dest="ctime",
                  type="int",
                  metavar="TIMESTAMP")
parser.add_option("-m", "--mtime",
                  action="store",
                  dest="mtime",
                  type="int",
                  metavar="TIMESTAMP")
parser.add_option("-u", "--uid",
                  action="store",
                  dest="uid",
                  type="int",
                  metavar="UID")
parser.add_option("-g", "--gid",
                  action="store",
                  dest="gid",
                  type="int",
                  metavar="GID")
options, args = parser.parse_args()


def get(path):
    try:
        return os.listdir(path)
    except Exception:
        pass


def type_check():
    check = options.type
    if check == 'socket':
        result = stat.S_ISSOCK
    elif check == 'directory':
        result = stat.S_ISDIR
    elif check == 'block':
        result = stat.S_ISBLK
    elif check == 'link':
        result = stat.S_ISLNK
    elif check == 'fifo':
        result = stat.S_ISFIFO
    elif check == 'file':
        result = stat.S_ISREG
    return result


def path_join(path, file):
    return os.path.join(path, file)


def file_info(path, file):
    file_path = path_join(path, file)
    try:
        return os.stat(file_path)
    except Exception:
        pass


def flatten(nlist):
    try:
        try:
            nlist + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nlist:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nlist


def parse(path):
    files = get(path)
    if not files:
        return

    try:
        check_fun = type_check()
    except:
        pass
    filter_files = []
    excep_files = []
    for file in files:
        f_info = file_info(path, file)
        if f_info is not None:
            if options.type:
                if check_fun(f_info.st_mode):
                    filter_files.append(file)
            excep_files.append(file)
    if not options.type:
        filter_files = excep_files

    filter_files = [file for file in filter_files if options.ex != path]

    if options.uid is not None:
        filter_files = [
            file for file in filter_files if options.uid == file_info(path, file).st_uid]
    if options.gid is not None:
        filter_files = [
            file for file in filter_files if options.gid == file_info(path, file).st_gid]
    if options.mtime is not None:
        filter_files = [
            file for file in filter_files if options.mtime > int(file_info(path, file).st_mtime)]
    if options.ctime is not None:
        filter_files = [
            file for file in filter_files if options.ctime > int(file_info(path, file).st_ctime)]
    dirs = []
    for file in excep_files:
        f_info = file_info(path, file)
        if f_info is not None:
            if stat.S_ISDIR(f_info.st_mode):
                dirs.append(path_join(path, file))

    for file in filter_files:
        if options.pattern in file:
            print(path_join(path, file))
    return dirs


def runner(dirs):
    result = []
    for _dir in dirs:
        res = parse(_dir)
        if res:
            result.append(res)
    result = list(flatten(result))
    if result:
        return runner(result)


def main():
    if len(args) < 1:
        parser.error("wrong number of arguments")
    elif len(args) == 1:
        dirs = parse(args[0])
        if dirs:
            try:
                runner(dirs)
            except KeyboardInterrupt:
                pass

if __name__ == '__main__':
    main()
