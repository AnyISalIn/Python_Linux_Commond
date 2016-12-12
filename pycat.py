#!/usr/bin/env python
# coding=utf-8

import sys

def Files(files):
    for file in files:
        yield file

def Read():
    for file in Files(sys.argv[1:]):
        try:
            f = open(file)
            yield f.readlines()
        except (FileNotFoundError, PermissionError) as e:
            yield e

if __name__ == '__main__':
    for file in Read():
        if not isinstance(file, list):
            print('\n', file); continue
        for line in file:
            sys.stdout.write(line)
