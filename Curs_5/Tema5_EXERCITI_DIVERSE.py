# """ ----------------------------------------------------------------------------------------------------------------
# Functii
# """
# print("Aici avem o functie care tipareste de n ori acelasi text")
# def functie():
#     print("Salut !")
#
# functie()
# functie()
# functie()
# print(" ")
#
# """ ----------------------------------------------------------------------------------------------------------------
# Functii cu parametru
# Functia poarta numele de functie
# Parametrul poarta numele de parametru
#
# Parametrii subt niste variabile declarate dar neinitializate
# Ei trebuie sa fie initializati si afisati. Se vor initializate (adica vor primi valori), la apelarea functiei
# """
# print("Aici avem o functie cu parametru care tipareste texte diferite")
# def functie(parametru):
#     print(f"Salut de la un {parametru}")
#
# functie("Andrei")
# functie("Alexandra")
# functie("Geta")
# functie("Cristian")
# print(" ")
#
# """ ----------------------------------------------------------------------------------------------------------------
# RETURN-ul la o functie se foloseste cand ne afiseaza si un raspuns
# Raspunsul se salveaza in variabila
#
# In general RETURN este ultimul din functie. El iese din functie si ofera si un raspuns
# In general avem un singur return la final .
# Exceptie face IF-ELSE care poate sa contina return pe fiecare ramura
# """
# def functie(numere):
#     if numere >= 0:
#         return ("Numerele sunt naturale")
#     else:
#         return ("Numerele nu sunt naturale")
# raspuns = functie(-3)
# print(raspuns)
# print(" ")
#
# """ ----------------------------------------------------------------------------------------------------------------
# EXCEPTII
#
# Acestea sunt situatii cnad codul nu poate sa execute nici o instructiune.
# Atunci transmite o exceptie
#
# Au sintaxa TRY/EXCEPT
# """
# try:
#     lista = [-1, 3, -4, 2, 7, -5 , 8 ]
#     lista[7]
# except IndexError as exceptie:
#     print(exceptie)
#
# print(" ")
# def se_divide(x, y):
#     try:
#         result = x // y
#     except ZeroDivisionError:
#         print("Scuze ! Incerci diviziunea prin zero? Asa ceva NU E POSIBIL ")
#     else:
#         print("Da ! Raspunsul este :", result)
#     finally:
#         print("Aceasta linie de incheiere se afiseaza mereu \n")
# se_divide(3, 2)
# se_divide(3, 0)
# print(" ")
# """ ---------------------------------------------------------------------------------------------------------------- """
