"""Ce este un SINGLETON si cum lucreaza acesta """

class SingletonClass:
    __instance = None
    sector = 'IT'

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def greet(self):
        print(f'Salut, {self.name}! Acesta este sectorul {self.sector}.')


a = SingletonClass('Andrei')
# print(a.sector)
# print(a.name)
# print(a)
# print(id(a))

a.greet()
a.sector = 'Media'
a.greet()

m = SingletonClass('Mihai')
# print(m.sector)
# print(m.name)
# print(m)
# print(id(m))

a.greet()
m.greet()