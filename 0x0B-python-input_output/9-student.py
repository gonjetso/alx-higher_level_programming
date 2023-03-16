#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize new student

        Args:
            first_name (str): The first name of the new student
            last_name (str): The last name of the new student
            age (int): The age of the new student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary representation of the new student"""
        return self.__dict__
