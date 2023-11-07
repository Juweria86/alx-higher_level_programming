#!/usr/bin/python3
"""Tis module writes into a file"""


def write_file(filename="", text=""):
    """writes string into a text file(UTF8)"""
    with open(filename, "w") as file:
        print(file.write(text))
