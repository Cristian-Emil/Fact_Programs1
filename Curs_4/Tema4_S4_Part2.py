"""Testul contine 15 exercitii
Aici in a doua partea avem exercitiile de la 9 la 15
in Tema4_S4_Part1 avem de la 1 la 8
"""
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 9 - S4")
# """
# 9. Având lista:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ●	Iterează prin ea.
# ●	Afișază cel mai mare număr (nu ai voie să folosești max).
# """
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# # print (numere)
# # for i in numere:
# #     print(i)
# # print(" ")
# #
# # j = 0           # este contorul pt iterartii
# # for nr in numere:
# #     j = j + nr
# #     print ("Suma numerelor este  = " , j)
#
# max1 = 0
# for i in range(len(numere)):
#     if numere[i] > max1:
#         max1 = numere[i]
# print(f'Cel mai mare numar din lista este: ', max1)
#
# # print(" ")
# # -------------------------------------------------------------------------------------------------------------------
# print("Tema 10 - S4")
# """
# 1 . Având lista:
# # numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# """
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# print (numere)
# # for i in numere:
# #     print(i)
# print(" ")
#
# for i in range (len(numere)):
#     if numere[i] >0:
#         numere[i]=-numere[i]
#     # else:
#     #     numere[i]= numere[i]
# print(" avem noua lista", numere )
# for i in numere:
#     print(i)
# print(" ")          # acest PRINT este ca sa pastram un rand gol cand executam codul si ne este afisat pe display.
# # -------------------------------------------------------------------------------------------------------------------
# print("Tema 11 - S4")
# """
# 11. Avem lista cu numere :
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișează cele 4 liste la final
# """
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
i=0

# print ("lista cu numere impare")
# print ("lista cu numere pare")
# for numere in alte_numere:
#     if numere%2 == 0:
#         numere_pare.append(numere)
#         print(numere_pare)
# print (" ")
# for numere in alte_numere:
#     if numere % 2 == 1:
#         numere_impare.append(numere)
#         print(numere_impare)
# print (" ")
# print ("lista cu numere pozitive")
# for numere in alte_numere:
#     if numere >= 0:
#         numere_pozitive.append(numere)
#         print(numere_pozitive)
# print (" ")
# print ("lista cu numere negative")
# for numere in alte_numere:
#     if numere < 0:
#         numere_negative.append(numere)
#         print(numere_negative)
# print(" ")
#
# for i in alte_numere:
#     if i < 0:
#        numere_negative.append(i)
#     else:
#         numere_pozitive.append(i)
#     if i % 2 != 0:
#         numere_impare.append(i)
#     else:
#         numere_pare.append(i)
# numere_pozitive.sort()
# print(numere_pozitive)
# print(numere_negative)
# print(numere_pare)
# print(numere_impare)
#-----------------------------------------------------------------------------------------------------------------------
# print("Tema 12 - S4")
# """
# 12. Avem lista cu numere :
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# Ordonează crescător lista fară să folosești sort.
# """
# lista = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#
# n = len(lista)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if lista[j] > lista[j+1]:
#             lista[j], lista[j+1] = lista[j+1], lista[j]
#
# print(lista)
#
# # Varianta 2
# lista_sortata = lista.copy()
#
# n = len(lista_sortata)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if lista_sortata[j] > lista_sortata[j+1]:
#             lista_sortata[j], lista_sortata[j+1] = lista_sortata[j+1], lista_sortata[j]
#
# print(lista_sortata)
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 13 - S4")
# """
# 13. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
#    User alege un număr
#    Programul îi spune:
# ●	Nr secret e mai mare
# ●	Nr secret e mai mic
# ●	Felicitări! Ai ghicit!
#
# """
# print("varianta 1 este cu IF - ELIF -ELSE")
# import random
# numar_secret1 = int(input("numar_secret1 = "))
# print (numar_secret1)
# nr_random1 = random.randint (1, 30)
# print (nr_random1)
# if numar_secret1 > nr_random1:
#     print (f"Numarul secret = {numar_secret1 } > nr_random = {nr_random1}")
# elif numar_secret1 < nr_random1:
#     print(f"Numarul secret = {numar_secret1}  < nr_random = {nr_random1}")
# else:
#     print(f"Felicitari, cele doua numere sunt egale {numar_secret1} = {nr_random1}")
# print(" ")
# #-----------------------------------------------------------
# print("Varianta 2 este cu WHILE - BREAK")
# import random
# nr_random2 = random.randint(1, 30)
# numar_ghicit = None
# pasul_i = 0
# while True :
#   pasul_i += 1
#   numar_ghicit = int(input("Introduceti un numar intre 1 si 30 =  "))
#   if numar_ghicit > nr_random2:
#     print(f"Numarul ghicit {numar_ghicit} este mai mare ca numarul aleatoriu {nr_random2}.")
#   elif numar_ghicit < nr_random2:
#     print(f"Numarul ghicit {numar_ghicit} este mai mic ca numarul aleatoriu {nr_random2} ")
#   else:
#     print("Felicitari! Ati ghicit numarul dupa ", pasul_i , " incercari.")
#   break
#   print(nr_random2)
# print(" ")
# # -----------------------------------------------------------------------------------------------------------------------
# print("Tema 14 - S4")
# """
# 14. Scrie un program care să genereze în consolă următoarea piramidă:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# """
# n=7
#
# for i in range(1, n+1):
#     for j in range(i):
#         print(i , end="")
#     print()
# print(" ")
#
#
# print("Varianta 2 - comapacta")
# for i in range(1, n+1):
#     print(f"{i *str(i)}")
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
print("Tema 15 - S4")
"""
15. tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
"""
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
#
# print("Lisat cu numere de la tastatura = " , tastatura_telefon)
# print(" ")
# print("Lista contine" , len(tastatura_telefon) , "subliste si acestea sunt " , "\n" ,
#     tastatura_telefon[0] , "\n" ,
#     tastatura_telefon[1] , "\n" ,
#     tastatura_telefon[2] , "\n" ,
#     tastatura_telefon[3]
# )
#
# print(" ")
# print("Sau aplicam varianta sa tiparim linie cu linie ")
# print(tastatura_telefon[0])
# print(tastatura_telefon[1])
# print(tastatura_telefon[2])
# print(tastatura_telefon[3])
# print(" ")
# ---------------------------------------------------
# print("Varianta 1")
# for sublista in tastatura_telefon:
#     for element in sublista:
#         print(element, end=" ")
#     print("Cifra curenta este aia pe care apasa degetelul tau")
#
# print(" ")
#
# print("Varianta2 - afisam toate numerele din lista")
# i = 0
# j = 0
# for i in range(len(tastatura_telefon)):
#     for j in range(len(tastatura_telefon[i])):
#         print (tastatura_telefon[i][j], end =" ")
#     print(" ")
#
# print(" ")
# print("Varianta 3 - cu IF afisam elementul 'x' care e definit de i si j.\n"
#       "Valorile i si j se specifica pt fiecare numar cu x <= max 4 , y <=max 3")
# i = int(input("Valoarea lui i = "))
# j = int(input("Valaorea lui j=  "))
# for i in range(i):
#     for j in range(j):
#         break
#     print(f"Valoarea lui 'x' este {tastatura_telefon[i][j]}")
#
# print(" ")
#
# print("Varianta 4 - cu WHILE afisam elementul 'x' care e definit de i si j.\n"
#       "Valorile i si j se specifica pt fiecare numar cu x <= max 3 , y <=max 2")
# i = int(input("Valoarea lui i = "))
# j = int(input("Valaorea lui j=  "))
# while i <= 3 and j <= 2:
#     print(f"Valoarea lui 'x' este {tastatura_telefon[i][j]}")
#     break
# else:
#     print("Am terminat exercitiul ca ai introdus o valoare pentru i sau j incorecta")
# print(" ")

# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# for rand in tastatura_telefon:
#     for coloana in rand:
#         print(f'cifra este {coloana}')

"""
TO DO: 

1.  Schimba intre ele elementele de pa diagonala principala si cea secundara  
2.  Schimba randurile cu coloanele 
3. Se considera doar elemenetele 1-9
"""
#-----------------------------------------------------------------------------------------------------------------------