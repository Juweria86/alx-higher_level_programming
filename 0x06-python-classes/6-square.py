#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
        self.__position = position

    def __string__(self):
        self.my_print()

    @property
    def size(self):
        """retrieves size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets size of square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """retrieve position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets position
        args: value - tuple for 2 positive int
        Raises: TypeError if value is not tuple and != 2 & < 0
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculates area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)

    def print_position(self):
        """returns position spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for i in range(self.position[1]):
            pos += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                pos += " "
            for k in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """prints in stdout the square in position"""
        print(self.print_position(), end='')
