"""
Cursul 7 - saptamana 4

POLYMORPHISM
"""
# class Tara:
#     def limba(self):
#         print("Nu au limba")
#
# class Romania:
#     def limba(self):
#         print("Romana")
#
# class SUA:
#     def limba(self):
#         print("Engleza")
#
# class Tara_lu_Papura(Tara):         # mosteneste totul de la Tara , cu toate proprietatile DEFAULT
#     pass
#
# tari = [Romania(), SUA(), SUA(), Tara(), Tara_lu_Papura()]
#
# for tara in tari:
#     tara.limba()
# print("")
# #-----------------------------------------------------------------------------------------------------------------------
# # Suma a trei numere pentru polimorfism
# def suma(a,b, c=0 ):                   # suma a trei numere
#     return a+b+c
#
# print(suma(9,7,5))
# print(suma(10,6))
#
#
# def suma(a1, b1, c=0 ):                   # suma a trei numere
#     return a1+b1
# # facem si suma dintre doua puncte
# print(suma((1 ,4),(5, 3)))
# # si el le concateneaza
#
# # ----------------------------------------------------------------------------------------------------------------------
# schimbarea comportamentului - nu le concateneaza, el le aduna
# def suma(a2, b2, c=0 ):                   # suma a 2 numere de tip TUPLE
#     # print(isinstance(a2, tuple))
#     if isinstance(a2, tuple) and isinstance(b2, tuple ):
#         return a2[0]+b2[0], a2[1]+b2[1]
#     return a2+b2
#
# a2=(1, 4)
# b2=(5, 3)
# # facem si suma dintre doua puncte
# print(suma((1 ,4),(5, 3)))
# print(suma(a2, b2))
#
#
# def functie(*args):
#     print(args)
#     print(type(args))
#     print(len(args))
#
# functie(10, "dans" , 45.5)
# # ----------------------------------------------------------------------------------------------------------------------
# """ Clase - POLYMORPHISM """
# class Romania():
#     def language(self):
#         print("Romana")
#
# class USA():
#     def language(self):
#         print("English")
#
# obj_ro = Romania()
# obj_usa = USA()
#
# for country in (obj_ro , obj_usa):
#     country.language()
#
#     def add (x, y, z=80):
#         return x + y+ z
#
#     print(add(2, 3))
#     print(add(2, 3, 4))
#
#     print(len("abc"))
# #    print(len[2, 3, 4])                                     # 'builtin_function_or_method' object is not subscriptable