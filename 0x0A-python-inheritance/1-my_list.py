#!/usr/bin/python3
"""This class inherits from list class"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
