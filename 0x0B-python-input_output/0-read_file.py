#!/usr/bin/python3
"""Read a text file"""


def read_file(filename=""):
    """Read a text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
