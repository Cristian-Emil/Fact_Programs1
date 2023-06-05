from abc import ABC, abstractmethod

class Animal (ABC):

    @abstractmethod
    def sound(self):
        raise NotImplementedError

    @abstractmethod
    def sleep(self):
        raise NotImplementedError

class Dog(Animal):
    def sound(self):
        print(" Ham ham !")

    def sleep(self):
        print("Zzzzzzzzzz")

class Cat(Animal):
    def sound(self):
        print(" Miau miau !")

    def sleep(self):
        print("Zzzzzzzzzz")

# # animal = Animal()
# caine = Caine()
# pisica = Pisica()
#
# # animal.sunet()
# caine.sunet()
# pisica.sunet()