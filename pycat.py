#!/usr/bin/env python
# coding=utf-8

import sys
from optparse import OptionParser


def Files(files):
    for file in files:
        yield file

def Read(args):
    for file in Files(args):
        try:
            f = open(file)
            yield f.readlines()
        except (FileNotFoundError, PermissionError) as e:
            yield e



def main():
    parser = OptionParser(usage="usage: %prog [options] [filename, ...]",
                          version="%prog 1.0")
    parser.add_option("-n", "--number",
                      action="store_true",
                      dest="number",
                      default=False,
                      help="show line numbers")
    options, args = parser.parse_args()

    if len(args) < 1:
        parser.error("wrong number of arguments")

    if options.number:
        for file in Read(args):
            if not isinstance(file, list):
                print('\n', file); continue
            for number, line in enumerate(file):
                result = str(number+1) + ' ' + line
                sys.stdout.write(result)
    else:
        for file in Read(args):
            if not isinstance(file, list):
                print('\n', file); continue
            for line in file:
                sys.stdout.write(line)

if __name__ == '__main__':
    main()
