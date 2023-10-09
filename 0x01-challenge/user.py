#!/usr/bin/python3
"""
 User class
"""


class User():
    """ Documentation """

    def __init__(self):
        """ Itialize class """
        self.__email = None

    @property
    def email(self):
        """ getter method """
        return self.__email

    @email.setter
    def email(self, value):
        """ Setter method """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
