""" Comanda FOR """
## cu pornire de la 0                                                                  - FUNCTIONEAZA
# for x in range(4):
#     if x == 4:
#         break
#     print(x)
# print(" ")
# # cu pornire de la 2 la 4
# for x in range(2 , 4):
#     if x == 4:
#         break
#     print(x)
# print(" ")
#
# # sau cu pasi
# n = int(input())
# for x in range(1, n , 9):
#     print(x)
# print(" ")
#
# """
# ATTENTIE:
# LA LINIA 16 , for x in range(1, n , 9, 12): - DACA SCRIEM 4 ARGUMENTE O SA PRIMIM MESAJ DE EROARE CA
# Traceback (most recent call last)
# File 'c: user\crist\PycharmProjects\project_1\Curs_4\For_comanda.py', line 16, in <module>
# """
# ----------------------------------------------------------------------------------------------------------------------
# # structuri repetitive                                                            - FUNCTIONEAZA
#
# lista1 = [10 , 13 , 53 , 2 , 47 , 51]
#
# print("Varianta 1")
# for element in lista1:
#     print(element)
# print("lista 1")
#
# lista1.pop()
# lista1.append(-32)
#
# print("lista 1 modificata")
# print (lista1)
# # prinatam elementul eliminat
# print(element)
#
# si aplicam varianta 2
# print("Varianta 2")
# for i in range(len(lista1)):
#     print(f"Afisam numarul de elmente din lista = {i}")
#
# print("Mutam comanda la nivelul lui IF si o sa astfel tiparim numarul de elemente din lista ca cifra")
# print(f"Lista2 are {i+1} elemente")
#
# print("Sau avem posibiliatatea sa tiparim pozitia din lista cu numarul atribuit ei")
# for i in range(len(lista1)):
#     print(f"{i}: , {lista1[i]}")
# print("")
#
# si aplicam varianta 3 cand numaram din 2 in 2 elementerle din lista
# print("Varianta 3")
# for i in range (0 , len(lista1) , 2):
#     print(f"{i}: {lista1[i]}")
# print(" ")
# # --------------------------------------------------------------------------------------------------------------------
#cum lucram cu FOR                                                            - FUNCTIONEAZA
# print("Examplul 1")
# lista1 = [63 , 4 , 17 , 98 , 5]
# suma1 = 0
# for i in lista1:
#     suma1 += i
# print (suma1 )
# # len(lista) ne da numarul de elemente din lista
# print(len(lista1))
# media1 = suma1 / len(lista1)
# print(f"Media elementelor din lista este = {media1} ")

# media elementelor pare si impare
# print("Media numerelor pare")
# suma2 = 0
# count = 0
# for i in lista1:
#     if i%2 == 0:
#         suma2 += i
#         count += 1
# print (suma2 )
# media2 = suma2 / count
# print(f"Media elementelor pare din lista este = {media2} ")
# print(" ")
#
# print("Media numerelor impare")
# suma3 = 0
# count = 0
# for i in lista1:
#     if i%2 == 1:
#         suma3 += i
#         count += 1
# print (suma3 )
# media3 = suma3 / count
# print(f"Media elementelor pare din lista este = {media3} ")
# print(" ")
## ---------------------------------------------------------------------------------------------------------------------
# """
# Fie lista de numere
# numere = [25, 11, 13, 21, 49]
# 1) afisati lista si separat numerele din lista
# 2) afisati toate numerele impare pana la primul numar par
#
# """
# numere = [25, 11, 13, 20, 49]
# print (numere)
# for i in numere:
#     print(i)
# print("Am afisat atat lista cat si numerele in mod coloana \n")
#
# print ("Afisati toate numerele impare pana la primul numar par")
# for i in numere:
#     if i% 2 == 0:
#         break
#     print(i)
# print("")

## ---------------------------------------------------------------------------------------------------------------------
# # varaianta de mai sus dar cu BREAK si CONTINUE                                  - FUNCTIONEAZA
# numere = [25, 10, 13, 20, 49]
# print (numere , "\n")
# for i in numere:
#     if i % 2 == 0:
#         continue
#     print(i)                        # am tiparit numerele impare din lista
#
# print("\n" + "ATENTIE : Comanda de mai sus este echivalenta cu :")
# for i in numere:
#     if i % 2 == 1:
#         print(i)
## ---------------------------------------------------------------------------------------------------------------------
# # Varianta fara BREAK - se executa pana la final
# for x in range(10):
#     print(x)
# print(" ")
#
#
# # Varianta cu BREAK - se executa pana la 6, dupa ce trece de al 6 lea element se opreste. Contorizarea incepe de la ZERO
# print("Eecutam varianata cu BREAK si ne oprim la 5 ")
# for x in range(10):
#     if x == 6:
#         break
#     print(x)
# print(" ")
#-----------------------------------------------------------------------------------------------------------------------

# nr = [25, 13, 41 ]
# for x =


#------------------------------------------Variante echivalente --------------------------------------------------------
# # Varianta FOR cu CONTINUE si FARA CONTINUE
# nr = [21, 11, 30, 41]
# i = 0
# print("Varianta cu continue")
# for i in nr:
#     if i%2 == 0:         # afisam toate numerele impara si eliminam pe cele pare
#         continue
#     print(i)
#
# # cea de sus si cea de jos sunt echivalente
# print("\n" + "Varianta fara continue")
# for i in nr:
#     if i%2 == 1:         # afisam toate numerele impara si eliminam pe cele pare
#         print(i)
#-----------------------------------------------------------------------------------------------------------------------
