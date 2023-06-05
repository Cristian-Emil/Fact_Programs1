"""
Cursul 7 - saptamana 4

ABSTRACTION - ABSTRACTIZAREA
"""
# from abc import ABC, abstractmethod
#
# class Animal(ABC) :
#     # @abstractmethod
#     def sunet(self):
#         raise NotImplementedError
#         print("Sunat de animal")
#
#     def culoare(self):
#         print("Nu are culoarea definita")
#
#     @abstractmethod
#     def culoare(self):
#         print("Are culoarea maro")
#
# class Caine(Animal):
#     def sunet(self):
#         super().sunet()
#         print("Ham ham")
#
#
# class Pisica(Animal):
#     def sunet(self):
#         print("Miau miau")
#         print("Are culoarea ")
#
# # # am definit metoda SUNET
# # # am obligat clasa COPIL sa implementeze sunet dar clasa PARINTE nu are comportament default
# #
# animal = Animal()
# caine = Caine()
# pisica = Pisica()
#
# animal.sunet()
# caine.sunet()
# pisica.sunet()
#
# # print(caine)



#
# ----------------------------------------------------------------------------------------------------------------------
# class A:
#     def __init__(self, a , b , c):
#         self.param_a = a
#         self._param_b = b
#         self.__param_c = c
#
#     def afiseaza_c(self):
#         print(self.__param_c)
#
# class B(A):
#     # def afiseaza_b(self):
#     #     print(self._param_b)
#
#      def afiseaza_c(self):
#         print(self.__param_c)
#
#
#
# a = A(10,20,30)
# print(a.param_a)
# print(a._param_b)
# # print(a.__param_c)             # deci da eroare ca e clasa protected
# # a.afiseaz_b()
#
# b = B (100, 200, 300)
# print(b._param_b)
# print(a._param_b)
# # b.afiseaza_b()
# # b.afiseaza_c()
# print(" ")
# ----------------------------------------------------------------------------------------------------------------------
# class Vietate():
#     def sunet(self):
#         print("Sunet de vietate")
#
# class Lup():
#     def sunet(self):
#         print("Auuuuuuuu")
#
# class Urs():
#     def sunet(self):
#         print("mooooorrrrrrr")
#
# vietate = Vietate()
# lup = Lup()
# urs = Urs()
#
# vietate.sunet()
# lup.sunet()
# urs.sunet()
# print(" ")
# ----------------------------------------------------------------------------------------------------------------------
"""Deci nu exista un sunet general astfel incat clasa animal are sunt default si am obligat clasa copil sa implementeze 
un sunt.
Clasa parinte nu are un comportamane DEFAULT
Atunci importam biblioteca ABC care simbolizeaza ca aceasta este o clasa abstracta si obligam clasa parinte sa ia 
valorile din clasa abstracta ABC si mai avem si ABSTRACTMETHOD

- Am primit mesaj ca : Can't instantiate abstract class Vietate with abstract method sunet - ceea ce inseamna ca avem 
o functie/un decorator care nu are implementare
Pentru a face implementare se comenteaza linia raise NotImplementedError si se pune linia print("Sunete scoase") 
Ca sa definim pentru lup si urs un sunte e nevoie se comentam liniile:
# vietate = Vietate()
# vietate.sunet()
si putem rula programul.

Cat timp linia de abstractmethod este valida nu putem sa apelam clasa VIETATE.
Comentam linia de @abstractmethod se poate sa rulam codul fara sa comentam liniile precizate m mai sus

Daca nu comentam linia de @abstractmethod atunci pune in linia de URS un super().sunet ca la aceasta linie sa 
apara linia din Vietate cu sunetele scoase de vietati.
 """
from abc import ABC, abstractmethod

class Vietate(ABC):
    @abstractmethod
    def sunet(self):
#        raise NotImplementedError
        print("Sunete scoase de vietati")


class Lup(Vietate):
    def sunet(self):
        print("aaauuuuuuuu")

class Urs(Vietate):
    def sunet(self):
        super().sunet()
        print("mooooorrrrrrr")

# vietate = Vietate()
lup = Lup()
urs = Urs()

# vietate.sunet()
lup.sunet()
urs.sunet()
print(" ")