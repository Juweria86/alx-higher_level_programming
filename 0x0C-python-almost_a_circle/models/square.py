#!/usr/bin/python3
"""This module defines square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes a new square
        args:
        size: size of square
        x: coordinate of new square
        y: coordinate of new square
        id: id of new square
        """
        super.__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
