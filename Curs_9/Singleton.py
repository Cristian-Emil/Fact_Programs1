class Singleton:
    __instance = None
    sector = "IT"

    def __init__(self, name):
        self.name = name

    def __new__(cls, *arg , **kargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def greet(self):
        print(f"Salut, {self.name}. Acesta este sectorul {self.sector}")



a = Singleton("Andrei")

# print(a.sector)
# print(a.name)
# print(a)
# print(id(a))
#
m = Singleton("Vasile")
# print(m.sector)
# print(m.name)
# print(m)
# print(id(m))

print("Apelare 'a'")
a.greet()
a.sector = "media"
a.greet()

print("")
print("Apelare 'm'")
m.greet()
a.greet()

""" ID-ul de obiect este acelasi pt ca este aceeasi clasa de obiect"""