#!/usr/bin/python3
"""This module appends string at the end of a text file"""


def append_write(filename="", text=""):
    """appends string to a text file"""
    with open(filename, "a", encoding="utf8") as file:
        return(file.write(text))
