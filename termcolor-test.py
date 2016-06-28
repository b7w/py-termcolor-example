#!/usr/bin/env python

import sys

from termcolor import colored


def file_to_list(fname):
    with open(fname, "r") as f:
        return [x.strip() for x in f.readlines() if x.strip()]


def make_colored(ch):
    chars = {
        "~": ("blue", []),
        ".": ("white", []),
        "#": ("green", []),
        "O": ("white", ["bold"]),
        "^": ("red", ["dark"]),
        "=": ("red", ["dark"]),
    }
    default = ("red", [])
    color, attrs = chars.get(ch, default)
    return colored(ch, color, attrs=attrs)


def main(fname):
    lines = file_to_list(fname)
    for src_line in lines:
        for ch in src_line:
            print(make_colored(ch), end='')
        print()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Usage: {} <infile>".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)
