#!/usr/bin/python3
""" This module has two functions, for serializaion and deserialization """
import pickle


class CustomObject:
    """ Custom Python class """

    def __init__(self, name, age, is_student):
        """method initializes object"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """ Prints the attributes"""
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """ Serialization method """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        """ Deserialization method """
        try:
            with open(filename, "rb") as f:
                res = pickle.load(f)
            return res
        except Exception as e:
            return None
