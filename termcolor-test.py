#!/usr/bin/env python

import sys

from termcolor import colored


def file_to_list(fname):
    rslt = []
    with open(fname, "r") as f:
        rslt = [x for x in f.read().split("\n") if x.strip() != ""]
    return rslt


def make_colored(ch):
    color = "red"  # error
    attrs = []
    if ch == "~":
        color = "blue"
    elif ch == ".":
        color = "white"
    elif ch == "#":
        color = "green"
    elif ch == "O":
        color = "white"
        attrs = ["bold"]
    elif ch == "^":
        color = "red"
        attrs = ["dark"]
    elif ch == "=":
        color = "red"
        attrs = ["dark"]
    return colored(ch, color, attrs=attrs)


if len(sys.argv) < 2:
    print("Usage: {} <infile>".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)

lines = file_to_list(sys.argv[1])
for src_line in lines:
    dst_line = ""
    i = 0
    chnum = len(src_line)
    while i < chnum:
        ch = src_line[i]
        dst_line = dst_line + make_colored(ch)
        i += 1
    print(dst_line)
