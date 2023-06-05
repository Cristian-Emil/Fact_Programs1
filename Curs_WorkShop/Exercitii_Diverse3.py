"""
Abstractizare
"""
from abc import ABC, abstractmethod

class Vietate(ABC):
    @abstractmethod
    def respira(self):
        raise NotImplementedError

    @abstractmethod
    def mananca(self):
        raise NotImplementedError

class Patruped(Vietate):
    def respira(self):
        print("Huuummm")
    def mananca(self):
        print("Hap, hap")

class Biped(Vietate):
    def respira(self):
        print("Puf, puf")
    def mananca(self):
        print("Mammm , mammm")

patruped = Patruped()
biped = Biped()

print(" ")
patruped.respira()
biped.respira()

print(" ")
patruped.mananca()
biped.mananca()

