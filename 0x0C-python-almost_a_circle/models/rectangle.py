#!/usr/bin/python3
"""Thi module defines rectangle"""
from models.base import Base


class Rectangle(Base):
    """defines rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes a rectangle
        args:
        width: width of the new rectangle
        height: height of the new rectangle
        x: x coordinate of rectangle
        y: y coordinate of rectangle
        id: id of new rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    @property
    def width(self):
        """gets width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.width = value

    @property
    def height(self):
        """gets height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.height = value

    @property
    def x(self):
        """gets coordinate (X) of rectangle"""
        return self.x

    @x.setter
    def x(self, value):
        self.x = value

    @property
    def y(self):
        """gets coordinate (y) of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.y = value
