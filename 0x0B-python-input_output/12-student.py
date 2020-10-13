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
        dict_cpy = {}
        if attrs:
            if attrs != []:
                for n, m in self.__dict__.items():
                    if n in attrs:
                        dict_cpy[n] = m
        else:
            dict_cpy = self.__dict__
        return dict_cpy
