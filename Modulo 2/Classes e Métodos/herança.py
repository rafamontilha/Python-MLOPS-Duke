class Pet:

    def eat(self):
        self.food = self.food - self.appetite
        print(f"Ate {self.appetite} of food, have {self.food} left.")

class Parakeet(Pet):

    def __init__(self):
        
        self.food = 100
        self.appetite = 1

class Dog(Pet):

    def __init__(self):
        
        self.food = 400
        self.appetite = 7

perry = Parakeet()
rufus = Dog()

perry.eat()
rufus.eat()



#cenários de testes unitarios

import unittest

class Testing(unittest.TestCase):

    pass

tests = Testing()

for atribute in dir(tests):
    if atribute.startswith("__"):
        continue
    print(f"Testing has the attribute: {atribute}")

