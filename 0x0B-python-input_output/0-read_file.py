#!/usr/bin/python3
"""Function that read a file"""


def read_file(filename=""):
    """The function scope ."""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
