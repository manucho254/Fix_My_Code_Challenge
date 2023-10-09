#!/usr/bin/python3
""" class Square
"""


class Square():
    """ class Square that respresents a square.
    """
    width = 0

    def __init__(self, *args, **kwargs):
        """ Initialize class
        """
        if "width" in kwargs:
            setattr(self, "width", kwargs.get("width"))

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ get perimeter of a circle
        """
        return (self.width * 4)

    def __str__(self):
        """ String representation of Square class
        """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
