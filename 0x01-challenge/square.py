#!/usr/bin/python3
""" Module for class square
"""


class Square():
    """ Class Square that represents a square
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ initialize Square class
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Get perimeter of a square
        """
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """ Return string representation of a Square
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
