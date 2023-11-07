#!/usr/bin/python3
"""This module reads text file"""


def read_file(filename=""):
    """reads a text file"""
    with open(filename, 'r') as file:
        print(file.read(), end="")
