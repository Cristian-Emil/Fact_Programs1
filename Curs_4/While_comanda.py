# # utilizarea lui WHILE
# print(" Varianta cu < ne afiseaza fara ultimul element")
# i = 0
# while i < 3:
#     print (i)
#     i += 1
# print(" Varianta cu <= ne afiseaza si ultimul element precizat")
# i = 0
# while i <= 3:
#     print (i)
#     i += 1
#
# """ daca rulam programul fara conditie i+=1 o sa ruleze la infinit si ca ne afiseze ZERO
#     atunci trebuie saimpunem o conditie care sa intrerupa ciclul - vezi mai jos"""
#
# #-----------------------------------------------------------------------------------------------------------------------
# """ WHILE cu BREAK """                                                                  # FUNCTIONEAZA
# print("Apasati ENTER ca sa calculeze : ")
# n = input()
# lista1 = [12, 16, 22]
# i =0
# while i < len(lista1):
#     print(2 * lista1[i])
#     i += 1
#
#
# print("Apasati ENTER ca sa calculeze : ")
# lista2 = [12, 16, 21]
# i =0
# while i < len(lista2):
#     if lista2[i] % 2 == 1:
#         break
#     print(2 * lista2[i])
#     i += 1
# #-----------------------------------------------------------------------------------------------------------------------