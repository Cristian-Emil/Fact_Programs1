# -----------------------------------------------------------------------------------------------------------------------
# print("Tema 6 - S5")
# """
# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
# """
# print(" Varianta 1")
# a = input("Text = ")
# def caracter_strain(x,a):
#     if x in a:
#          return True
# #     else:
# #         return False
# #     print(False)
# # print(True)
# #
# # print(" ")
# print("Varianta 2")
# x = 'x'
# a = "Acesta e un text"
# if caracter_strain(x, a):
#     print(f"Caracterul '{x}' se gaseste in stringul '{a}'")
# else:
#     print(f"Caracterul '{x}' nu se gaseste in stringul '{x}'")

# cauta rezolvare la minutul 100
#-----------------------------------------------------------------------------------------------------------------------
# print("Tema 7 - S5")
# """
# 7. Funcție fără return, primește un string și printează pe ecran:
# ●	Numărul de caractere lower case este x
# ●	Numărul de caractere upper case exte y
#
# """
# x = 0
# y = 0
# def lower_upper(string:str):
#     for i in string:
#         if i.isupper():
#             x += 1
#         if i.islower():
#             y += 1
#     print(f"stringul ar : {x} caractere upper si {y} caractere lower")

# DE CONTINUAT CONF. VIDEO - MINUTUL 106
#-----------------------------------------------------------------------------------------------------------------------
# print("Tema 8 - S5")
# """
# 8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.
# """
# def gasire_nr_poz(numere):
#     return[x for x in numere if x>0 ]
# lista_nuumere= 12, 14, -9, 85, -6
# print(gasire_nr_poz(lista_nuumere))
# print(" ")
#-----------------------------------------------------------------------------------------------------------------------
# print("Tema 9 - S5")
# """
# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
# ●	Primul număr x este mai mare decat al doilea număr y
# ●	Al doilea număr y este mai mare decat primul număr x
# ●	Numerele sunt egale.
# """
#
# def comparare(x,y):
#     if x == y:
#         print(f"Numerele sunt egale {x} = {y}" )
#     elif x > y:
#         print(f"{x} > {y}")
#     else:
#         print(f"{x} < {y}")
#
# comparare (7 , 10)
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 10 - S5")
# """
# 10. Funcție care primește un număr și un set de numere.
# ●	Printează ‘am adaugat numărul nou în set’ + returnează True
# ●	Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
# """
# def adaug_nr(set_nr:set, x:int):
#     if x in set_nr:
#         return False
#     else:
#         return True
# a=1
# numere = {10, 5, 6, 45, 60}
#
# print(adaug_nr(numere, a))
# print(numere)
# print(type(numere))
#
# print("Tipuri de ..... ")
# numere1 = {10, 5, 6, 45, 60}
# print(type(numere1))
# numere2 = [10, 5, 6, 45, 60]
# print(type(numere2))
# a = (1 , )
# print(type(a))
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 11 - S5")
# """
# 11. Funcție care primește o lună din an și returnează câte zile are acea lună.
# """
# from calendar import monthrange
#
# def zile_luna (m, y = 2023):
#     return monthrange(y, m)[1]
# print(zile_luna(8))
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------

"""
TO DA
Cum calculam numarul total de zile lucratoare dintr-o luna si dintr-un an folosind libraria from calendar
import monthrange"""
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 12 - S5")
# """
# 12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.
#
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ●	print("Suma: ", a)
# ●	print("Diferenta: ", b)
# ●	print("Inmultirea: ", c)
# ●	print("Impartirea: ", d)
# """
#
# def calc (x,y):
#     return x+y , x-y , x*y , x/y
# print(calc(4,8))
# print()
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 12 - S5")
# """
# 13. Funcție care primește o listă de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
# """
#
# def nr (lista:list):
#     my_dict = {}
#     for i in lista:
#         if i in my_dict:
#             my_dict[i] += 1
#         else:
#             my_dict[i] = 1
#     return my_dict
# x = [1, 3, 1, 5, 9, 7, 7, 5, 5]
# print (nr ( x ) )
# # ca sa tiparim sub forma de dictionar
# import pprint
# pprint(print (nr ( x ) ))
# print()
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 14 - S5")
# """
# 14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
# """
# def maxim(a,b,c):
#     return max (a,b,c)
# print(maxim(6, -2, 4))
# print
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 1 - S6")
# """
# 1.     Atribute: rază, culoare
#     Constructor pentru ambele atribute
#     Metode:
# ●	descrie_cerc() - va PRINTA culoarea și raza
# ●	aria() - va RETURNA aria
# ●	diametru()
# ●	circumferinta()
#
# """
# import math
#
# class Cercuri:
#     # raza = " "
#     # culaore =" "
#     def __init__(self, raza, culoare, greutate = "9"):
#         self._raza = raza
#         self._culoare = culoare
#         self._greutate = greutate
#
#     def descr_cerc(self):
#         print(f"raza = {self._raza} si  culoare = {self._culoare} si greutate = {self._greutate} ")
#
#     def aria(self):
#         print(f"Aria cercului este  = { math.pi * self._raza** 2 } ")
# # facem metoda statica
#     @staticmethod
#     def definitie_cerc():
#         print(f"Cercul e rotund")
#
#
#     def def_cerc(self , custom_pi):
#         print(f"Cercul cu raza:  {self._raza}  este rotund si are valoarea lui pi {custom_pi}")
#
#
# cerc = Cercuri (10, "albastru")
# cerc.definitie_cerc()
# cerc.def_cerc(4)
