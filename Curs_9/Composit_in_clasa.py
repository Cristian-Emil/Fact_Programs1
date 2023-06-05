# from abc import ABC, abstractmethod
#
# class Component(ABC):
#     @abstractmethod
#     def operation(self):
#         raise NotImplementedError
#
#
# class Box(Component):
#     components = []
#
#     def operation(self):
#         print('Ai deschis cutia')
#
#         print(len(self.components))
#         if len(self.components) > 0:
#             for c in self.components:
#                 if id(c) == id(self):
#                     raise Exception('aici')
#                 c.operation()
#
#     def add(self, component: Component):
#         if component not in self.components:
#             self.components.append(component)
#
#     def remove(self, component: Component):
#         if component in self.components:
#             self.components.remove(component)
#
#
# class Product(Component):
#     def init(self, name = ''):
#         self.name = name
#
#     @property
#     def name(self):
#         return self.name
#
#     @name.getter
#     def name(self):
#         return self.name
#
#     def operation(self):
#         print(f'Pordus: {self.name}')
#
#
# big_box = Box()
#
# toy = Product("jucarie darguta")
# little_box = Box()
#
# screwdriver = Product('surubelnita')
# key = Product('cheie')
# little_box.add(screwdriver)
# little_box.add(key)
#
# little_box.operation()
# big_box.add(toy)
# big_box.add(little_box)
#
# big_box.operation()

#-----------------------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Box(Component):
    def init(self):
        self.components = []

    def operation(self):
        print('Ai deschis cutia')
        print(len(self.components))

        for c in self.components:
            c.operation()

    def add(self, component: Component):
        if component not in self.components:
            self.components.append(component)

    def remove(self, component: Component):
        if component in self.components:
            self.components.remove(component)


class Product(Component):
    def init(self, name=''):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def operation(self):
        print(f'Produs: {self.name}')


big_box = Box()

toy = Product('jucarie darguta')
little_box = Box()

screwdriver = Product('surubelnita')
key = Product('cheie')
little_box.add(screwdriver)
little_box.add(key)

little_box.operation()
big_box.add(toy)
big_box.add(little_box)

big_box.operation()