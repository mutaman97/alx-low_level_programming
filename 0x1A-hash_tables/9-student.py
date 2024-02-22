#!/usr/bin/python3
"""Defines class Student"""


class Student:
    """Represent student"""

    def __init__(self, first_name, last_name, age):
        """Initialize new Student

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get dictionary representation of the Student"""
        return self.__dict__
