from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def print_area(self):
        pass

    def __str__(self):
        return f'[Shape] name: {self.name}'

