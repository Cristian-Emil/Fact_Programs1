# """ FOR si BREAK """
# for i in range (10):                        # acesta incepe de la ZERO si merge pana al 9 , fara 10 cu pas de 1
#     if i == 7:
#         break
#     print(i)                                # pentru ca am pus break la 7 o sa scrie toate valorile de la 0 la 6, fara 7
#
# print()
# #------------------------------------------------------------------------
# """ FOR si CONTINUE """
# for i in range (1, 10,2):                   # acesta incepe de la 1 si merge pana al 9, fara 10, cu pas de 1
#     if i == 7 :                             # pentru ca am pus conditia i == 7 o sa sara peste 7 si tipareste restul
#         continue
#     print(i)                                # o sa tipareasca toate cifrele din 2 in 2 incepand de la 1 la 10 si sare peste 7
#
# print()
#
"""---------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------"""
# """ WHILE si BREAK """
# while True:
#     numar1 = int(input("Introduceti orice nr. exceptand 0 : "))
#     if numar1 == 0:
#         print ("Gata cu tastarea, ai introdus 0")
#         break
#     print("Numarul este = ", numar1)
#
# print()
# #------------------------------------------------------------------------
# """Varianta 2 WHILE si CONTINUE """
#
# numar3 = 0
# while numar3 < 9:
#     numar3 += 1
#     if numar3 % 2 == 0:
#         continue                # aici avem conditia ca daca este numar impar se printeaza si daca e numar par va
#                                 # trece la urmatorul pas pana ajunge la valoarea maxima a numar3, cel definit in WHILE
#     print(numar3)
# else:
#     print("Iteratia se termina aici")
# print()
# #------------------------------------------------------------------------ Cel de mai jos a fost cu chin mare de tot
# """ WHILE si CONTINUE """
# numar2 = 0
# while numar2 <= 5:
#     print("Numarul tau curent este = " , numar2)
#     numar2 = numar2 + 1
#     print ("Ai tasta un nr mai mic sau egal cu 5" , numar2)
#     continue                # este conditia ca daca ajunge la valoarea lui numar2 din conditia while sa opreasca iteratia
# else:
#     print("Numarul tau a ajuns la 5" )
#
# print()
# #-----------------------------------------------------------------------------------------------------------------------
# """ WHILE si CONTINUE """
# numar2 = 0
# while numar2 <= 5:
#     print("Numarul tau curent este = " , numar2)
#     numar2 = numar2 + 1
#     print (f"Noul nr este mai mic sau egal cu {numar2}")
#     continue                # este conditia ca daca ajunge la valoarea lui "numar2" din conditia while sa opreasca iteratia
# else:
#     print(f"Numarul tau a ajuns la {numar2}" )
#
# print()

