#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Class Square"""

    def __init__(self, size=0):
        """method to initiate"""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method to initalize value"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """class method to return current square area"""
        return (self.__size**2)
    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
