#!/usr/bin/env python3
""" An abstract base class"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Dog class, subclass of Animal"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class, subclass of Animal"""

    def sound(self):
        return "Meow"
