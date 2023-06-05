from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        raise NotImplementedError


class Box(Component):
    __components = []                       # este un gen de CLASS FIELD

    def __init__(self):
        self.__components = []

    def operation(self):
        print('Ai deschis cutia')

        if len(self.__components) > 0:
            for c in self.__components:
                if id(c) != id(self):
                    c.operation()

    def add(self, component: Component):
        if component not in self.__components:
            self.__components.append(component)

    def remove(self, component: Component):
        if component in self.__components:
            self.__components.remove(component)


class Product(Component):
    def __init__(self, name=''):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.getter
    def name(self):
        return self.__name

    def operation(self):
        print(f'Pordus: {self.__name}')


big_box = Box()

toy = Product('jucarie draguta')
little_box = Box()

screwdriver = Product('surubelnita')
key = Product('cheie')
little_box.add(screwdriver)
little_box.add(key)

# little_box.operation()

big_box.add(toy)
big_box.add(little_box)

big_box.operation()

# #  ---------------------------------------------------------------------------------------------------------------------
# """ Deci un proces normal o sa mearga ca mai jos. Dasca folosim compositul o sa mearga ca mai sus"""

# class MyClass:
#     prop ="Salut"
#
#     def __init__(self, prop_val=" "):
#         self.prop = prop_val
#
# c1 = MyClass ("Ce faci")
# c2 = MyClass ("Bine")
#
# print(c1.prop)
# print(c2.prop)
# c2.prop = "C.f."
#
# print(c1.prop)
# print(c2.prop)
# print(MyClass.prop)
