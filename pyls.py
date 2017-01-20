import sys
import os
import stat
import pwd
import grp
from optparse import OptionParser


parser = OptionParser(usage="usage: %prog [options] [path, ...]",
                      version="%prog 1.0")
parser.add_option("-l", "--list",
                  action="store_true",
                  dest="list",
                  default=False,
                  help="list")
parser.add_option("-a", "--all",
                  action="store_true",
                  dest="all",
                  default=False,
                  help="show all")

options, args = parser.parse_args()


def list(path):
    return os.listdir(path)


def parse(path):
    files = [file for file in list(path) if not file.startswith('.')]

    if options.all:
        files = list(path)
    result = ' '.join(files)

    if options.list:
        result = ""
        for file in files:
            f_info = os.stat(os.path.join(path, file))
            mode = stat.filemode(f_info.st_mode)
            size = f_info.st_size
            if size > 1000000:
                size = str(size / 1000000) + "M"
            elif size > 1000:
                size = str(size / 1000) + "K"
            link = f_info.st_nlink
            user = pwd.getpwuid(f_info.st_uid).pw_name
            group = grp.getgrgid(f_info.st_gid).gr_name
            result += "{mode}  {link}  {user}  {group}  {size}  {file}\n".format(
                mode=mode, link=link, user=user, group=group, size=size, file=file)

    return result


def main():
    if len(args) < 1:
        print(parse())
    elif len(args) == 1:
        print(parse(args[0]))
    else:
        for path in args:
            print("{}:".format(path))
            print(parse(path))

if __name__ == '__main__':
    main()
