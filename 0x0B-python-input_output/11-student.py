#!/usr/bin/python3
"""
Creation of a student class
"""


class Student:
    """ Student object layout
    """
    def __init__(self, first_name, last_name, age):
        """ constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a JSON representation of an obj
        """
        return self.__dict__
