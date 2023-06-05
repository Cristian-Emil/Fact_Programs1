# """ ----------------------------------------------------------------------------------------------------------------
# CLASE, OBIECTE
# """
# print("Clasa")
# class Masina1:
#     producator = "Ford"
#     model = None
#     anul =  2022
#     culoare = None
#
#     def accelerare(self):
#         print("Luam, viteza")
#     def stop(self):
#         print("Oprim, comanda se termina aici!")
#
#
# print("Obiecte")
# car1 = Masina1()
# car2 = Masina1()
# print(car1.producator)
# print(car2.producator)
# car1.model ="Focus"
# car2.model ="Mustang"
# car1.accelerare()
# car2.accelerare()
# car1.stop()
# car2.stop()
# print(" ")
#
""" ----------------------------------------------------------------------------------------------------------------
CONSTRUCTOR
"""

print("Constructor")
class Masina2:
    producator = "Ford"
    model = None
    anul =  2022
    culoare = None

    def __init__ (self, model, culoare):
        self.model = model
        self.culoare = culoare
car1 = Masina2("Puma" , "Blue")
car2 = Masina2("Fiesta" , "Rosie")
print(car1.producator)
print(car1.model)
print (car1.anul)
print(car1.culoare)
print(" ")
print(car2.producator)
print(car2.model)
print (car2.anul)
print(car2.culoare)
print(" ")