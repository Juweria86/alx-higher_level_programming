#!/usr/bin/python3
"""This module does nothing"""


class BaseGeometry:
    """This class contains a base geometry"""

    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
