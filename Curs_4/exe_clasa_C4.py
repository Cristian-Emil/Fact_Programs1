# # Introducti valori pana spuneti STOP                                           - FUNCTIONEAZA
# x = input(" ")
# print("Introdu cuvantul stop")
# while x != "stop":
#     print(x)
#     x=input()
# print("citirea se incheie aici")
#
#
# # avem o lista care are 6 elemente
# lista1 = [30, 40, 25, 71, 80, 10]
# suma =0
# x = sum(lista1)
# print (x)
#
# for i in lista1:
#     if i % 2 == 0:              #   adunam doar elementele pare
#         suma += i
# #        countor += i
# media = suma / len(lista1)
# print(suma)
# print(f"Media este {media}")
#
# print("")
# #---------------------------------------------------------------------------------------------------------------------
# Se primesc comenzi                                                                - FUNCTIONEAZA - de imbunatatit
# print("Se primesc comenzi")
# user = input(f"Introducem numerul de comanda = " )
# total=0
# cap_max = 100
# while user != "stop":
#     if total + int(user) >= cap_max:
#         break
#     total += int(user)
#     user = input(f"Introducem numerul de comanda = ")
# print(f"Avem un numar de x = {total} comenzi")
#
# print("")
# #---------------------------------------------------------------------------------------------------------------------
#   Exrcitiu pentru lista, cautati elementul care e mai scurt de 5 elemente         - FUNCTIONEAZA
# lista2 = ["rosu" , "albastru" , "galben" ,  "alb" , "galben" , "gri" ]
# i = -1                              # se face -1 ca sa ia si primul element
# while i < len(lista2):                                       # deci indexul parcurge toata lista . LEN ne spune lungimea listei
#     i += 1
#     if i >= len(lista2):
#         break
#     if len(lista2[i]) >= 5:          # este lungimea elementul cautat , mai mare sau egal ca 5
#         print(lista2[i])
#         continue
#     print("")
#     print(lista2[i])

# print("")
# #---------------------------------------------------------------------------------------------------------------------
# avem o lista de numere introduse de la tastatura                                  - FUNCTIONEAZA
# lista_nr =[]                    # ESTE O LISTA GOALA
# nr = input(" ")
# while nr != "stop":
#     print (f"Avem numarul = {nr}")
#     lista_nr.append(int(nr))
#     nr = input()
# print(lista_nr)
#
# suma = 0
# for i in lista_nr:
#     if i % 2 == 1 or i < 20:
#         suma += i
# print (suma)
# #---------------------------------------------------------------------------------------------------------------------
