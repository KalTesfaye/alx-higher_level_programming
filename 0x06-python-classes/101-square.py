#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """class square 6"""

    def __init__(self, size=0, position=(0, 0)):
        """initialization method"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter method"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """getter method"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """position setter"""
        if type(value) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) and type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] and value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """return square area"""
        return (self.__size**2)

    def my_print(self):
        """prints to stdout square with the char #"""
        if self.size == 0:
            print()
        else:
            a, b = self.position
            for line in range(b):
                print()
            for line in range(self.size):
                print(' ' * a, end='')
                print('#' * self.size)
    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")

