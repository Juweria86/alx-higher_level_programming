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
