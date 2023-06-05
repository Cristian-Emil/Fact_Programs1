"""Testul contine 19 exercitii
Aici in a doua partea avem exercitiile de la 11 la 19
in Tema5_S5_Part12 avem de la 1 la 10
"""
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
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------
# print("Tema 14 - S5")
# """
# 14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
# """
# def maxim(a,b,c):
#     return max (a,b,c)
# print(maxim(6, -2, 4))
# print
#-----------------------------------------------------------------------------------------------------------------------
# print("Tema 14 - S5")
# """
# 14. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
# Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
# """
# i = 0
# nr = int(input("nr = "))
# def suma_nr(nr):
#     x = 0
#     for i in range (nr+1):
#         x += i
#     return x
# print(suma_nr(nr))
# print
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 16 - S5")
# """
# 16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}
# """
#
# lista1 = [1, 1, 2, 3]
# lista2 = [2, 2, 3, 4]
# print("Returnam lista comuna")
# def nr_comune1 (lista1, lista2):
#     nr = []
#     for numar in lista1:
#         if numar in lista2 and numar not in nr:
#             nr.append(numar)
#     return nr
# print(nr_comune1(lista1, lista2))
#
# print("Returnam set comun")
# def nr_comune2(lista1, lista2):
#     set1 = set(lista1)
#     set2 = set(lista2)
#     nr_com = set1 &set2
#     return nr_com
# print(nr_comune2(lista1, lista2))
# print
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 17 - S5")
# """
# 17.Funcție care să aplice o reducere de preț.
# Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
# Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă
# """
#
# def pret_nou( pret, reducere):
#      if reducere > 100 :
#          print(f"Reducerea nu poate sa de peste 100% , pretul este = {pret}")
#          return pret
#      else:
#          pret_redus = pret * (1- reducere/100)
#          return pret_redus
#
# pret = int(input("Costa = "))
# reducere = int(input("Reducere = " ))
#
# pret_redus = pret_nou(pret, reducere)
# print("Pretul final este : " , pret_redus )
# print
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 18 - S5")
# """
# 18.Funcție care să afișeze data și ora curentă din România.
# (bonus: afișazăi și data și ora curentă din China)
# """
#
# from datetime import datetime
# import pytz
#
# print("Selecțam fusul orar pentru România, cu capitala Bucuresti")
# fus_orar = pytz.timezone('Europe/Bucharest')
#
# data_si_ora = datetime.now(fus_orar)                           # Obțineți data și ora curentă în fusul orarul specificat
#
# format_data_ora = "%d-%m-%Y %H:%M:%S"                          # Formatam și afișam data și ora
# data_si_ora_format = data_si_ora.strftime(format_data_ora)
# print("Data și ora curentă în România:", data_si_ora_format)
# print(" ")
#
# print("Selectam fusul orar pentru China, cu capitala Shanghai")
# fus_orar = pytz.timezone('Asia/Shanghai')
#
# data_si_ora = datetime.now(fus_orar)
#
# format_data_ora = "%d-%m-%Y %H:%M:%S"
# data_si_ora_format = data_si_ora.strftime(format_data_ora)
# print("Data și ora curentă în China:", data_si_ora_format)
# print("")
#-----------------------------------------------------------------------------------------------------------------------
# print("Tema 19 - S5")
# """
# 19.Funcție care să afișeze câte zile mai sunt până Crăciun
# """
# from datetime import date
#
# def rest_zile():
#     ziua_curenta = date.today()
#     an_curent = ziua_curenta.year
#     Craciun = date(an_curent, 12, 25)
#
#     if ziua_curenta > Craciun:
#         an_viitor = an_curent + 1
#         Craciun = date(an_curent, 12, 25)
#
#     nr_zile = (Craciun - ziua_curenta).days
#     return nr_zile
#
# ziua_curenta = str(input("Data curenta, da ENTER"))
#
# nr_zile = rest_zile()
# print("Numar de zile ramase : " , nr_zile )
# print(" ")
#-----------------------------------------------------------------------------------------------------------------------
# print("Tema suplimentara - TO DO")
# """
# Cum calculam numarul total de zile lucratoare dintr-o luna si dintr-un an folosind libraria from calendar
# import monthrange
# """
# from  calendar import monthrange
#
#
# luna = int(input("Luna de verificat = "))
# an = int(input("An de verificat = "))
#
# print(f"Calculam numarul total de zile din luna {luna} a anului {an}")
# def zile_luna(an, luna):
#     _ , zile_luna = monthrange(an, luna)
#     numar_zile_luna = 0
#
#     for zi in range(1, zile_luna + 1):
#         zi_saptamana = monthrange(an, luna)[0]
#
#         if zi_saptamana <= 6:
#             numar_zile_luna += 1
#
#     return numar_zile_luna
#
# zile_luna = zile_luna(an, luna)
# print("Numărul de zile din luna", luna, "este:", zile_luna)
#
#
#
# print(" ")
# print(f"Calculam numarul total de zile lucratoare din luna {luna} a anului {an}")
# def numar_zile_lucratoare_luna(an, luna):
#     _, zile_luna = monthrange(an, luna)
#     numar_zile_lucratoare = 0
#
#     for zi in range(1, zile_luna + 1):
#         zi_saptamana = monthrange(an, luna, zi)[0]
#         if zi_saptamana < 5:                                        # Verifica daca ziua este de luni pana vineri (0-4)
#             numar_zile_lucratoare += 1
#             print(numar_zile_lucratoare())
#     return numar_zile_lucratoare
#
# def numar_zile_lucratoare_an(an):
#     numar_zile_lucratoare_total = 0
#
#     for luna in range(1, 13):
#         numar_zile_lucratoare_total = numar_zile_lucratoare_luna(an, luna, zi) + 1
#
#     return numar_zile_lucratoare_total
#
# umar_zile_lucratoare_luna = numar_zile_lucratoare_luna(an, luna)
# print("Numărul de zile lucrătoare din luna", luna, "este:", numar_zile_lucratoare_luna)
# print(" ")
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#
#
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
