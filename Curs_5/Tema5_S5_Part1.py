"""Testul contine 19 exercitii
Aici in a doua partea avem exercitiile de la 1 la 10
in Tema5_S5_Part2 avem de la 10 la 19
"""
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 1 - S5")
# """
# 1. Funcție care să calculeze și să returneze suma a două numere
# """
# x = int(input("x = "))
# y = int(input("y = "))
# # def suma_numere(x, y):
# # # Varianat 1
# #     suma = x + y
# #     return suma
# # # Varianta 2
# #     return x + Y
# # print(suma_numere(x, y))
#
# def suma_numere2(*x):
#     return x[0]+x[1]
# print(suma_numere2(x,y,7,5))
# """  Aici X este un TUPLE si cu * despachetam  """
# print(" ")
#
# def suma_numere3(**x):
#     return x["a"] + x["b"]
# print(suma_numere3(a=1 , b=3))
# print(suma_numere3(a=x , b=y))
# """  Aicxi X este un DICTIONAR si cu ** despachetam  """
# print(" ")
#
# """" TO DO - de citi si exersat o functie care are totate tipurile de param.
#  Standard, arbitrar, etc. """
# # -----------------------------------------------------------------------------------------------------------------------
# print("Tema 2 - S5")
# """
# 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
# """
# print("Varianta 1 - cu DEF - IF - ELSE ")
# x = int(input("x = "))
# def numar_par(x)  :
#     if x %2 == 0:
#         return True
#     else:
#         return False
#
# print(numar_par(x))
# print(" ")
# print("Varianta 2 - simplificata ")
# x = int(input("x = "))
# def numar_impar(x):
#     return (x % 2 == 1)
#     print("Numarul este impar")
# print("Numarul este par")
#
# print("Varianta 3 - simplificata ")
# par_impar(int(input))
#
# print(" ")
# # -----------------------------------------------------------------------------------------------------------------------
# print("Tema 3 - S5")
# """
# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
#
# """
#
# # Varianat 1
# prenume = input("prenumele =  ")
# nume = input("numele =  ")
# nume_complet= prenume + nume
# def numele(nume_complet):
#     return len(nume_complet.replace(" "," "))
# print(numele(nume_complet))
# print(" ")
#
# # Varianat 2
# prenume = input("prenumele =  ")
# nume = input("numele =  ")
# nume_complet= prenume + nume
# def total_caractere(nume_complet):
#     count = 0
#     for i in nume_complet:
#         if i==' ':
#             continue
#         else:
#             count+=1
#     return count
# print(total_caractere(nume_complet))


# Vezi inregistrarea la minutul 85
# Varianat 3
# def numar(numecomplet)
#     nume_prenume
#
# print(" ")
# -----------------------------------------------------------------------------------------------------------------------
# print("Tema 4 - S5")
# """
# 4. Funcție care returnează aria dreptunghiului
# """
# l1 = int(input("latura 1 = "))
# l2 = int(input("latura 2 = "))
# def aria_dreptunghi(l1,l2):
#     return l1*l2
# print (aria_dreptunghi(l1,l2))
# print(" ")
# # Varianta 2
# def aria(lungime, latime=None ):
#     if latime != None:
#         return lungime * latime
#     else:
#         return lungime**2
# print(f"aria {aria(3,4)}")
# print(" ")
# # -----------------------------------------------------------------------------------------------------------------------
# print("Tema 5 - S5")
# """
# 5. Funcție care returnează aria cercului
# """
# r1 = int(input("r = "))
# pi = 3.1415
# def aria_cercului1(r1,pi):
#     return pi*(r1**2)
# print (aria_cercului1(r1,pi))
# print(" ")
#
# """ Putem IMPORTA functia MATH si scrie simplificat """
# import math
# r2 = int(input("r = "))
# def aria_cercului2(r2):
#     return math.pi * r2 ** 2
# print (aria_cercului2(r2))
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