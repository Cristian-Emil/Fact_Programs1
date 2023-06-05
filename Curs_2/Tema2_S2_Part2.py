# """
# Continuarea exercitiilor din folderul / package-ul
# Tema2_S2_Part.py
# punctele 11 la 21
# """
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 11 - S2")
# """
# 11. Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
#  """
# x9 = input ("x9 = ")
# print(x9)
# nr_cifre = len(f"{x9}")
# print(nr_cifre)
# if nr_cifre >= 4 :
#     print (f"numarul are exact {nr_cifre} termeni")
# else:
#     print(f"numarul are mai putin de 4 termeni si anume {nr_cifre} cifre")
# print(" ")
# # -----------------------------------------------------------------------------------------------------------------------
# print("Tema 12 - S2")
# """
# 12.Verifică dacă x are exact 6 cifre
#  """
# x10 = input ("x10 = ")
# print(x10)
# nr_cifre = len(str(x10))
# print(nr_cifre)
# if nr_cifre == 6 :
#     print (f"numarul are exact {nr_cifre} termeni")
# else:
#     print(f"numarul are mai putin sau mai mult de 6 termeni si anume {nr_cifre}")
# print()
#
# # varianta 2
# print("varianta 2")
# if nr_cifre == 6 :
#     print (f"numarul are exact {nr_cifre} termeni")
# elif nr_cifre < 6:
#     print(f"numarul are mai putin de 6 termeni si anume {nr_cifre}")
# else:
#     print(f"numarul are mai mult de 6 termeni si anume {nr_cifre}")
# print(" ")
# # -----------------------------------------------------------------------------------------------------------------------
# print("Tema 13 - S2")
# """
# 13.Verifică dacă x este numar par sau impar
#  """
# x10 = int(input ("x10 = "))
# print(x10)
# r = x10 % 2
# if r >= 1:
#     print ("numarul este impar ca are RESTUL = 1" )
# else:
#     print ("numarul este par ca are RESTUL = 0")
# print(" ")
# -----------------------------------------------------------------------------------------------------------------------
## print("Tema 14 - S2")
# """
# 14. x, y, z (int)
# Afișează care este cel mai mare dintre ele?
#  """
# x11 , y11 , z11 = (input ("x11 = "), input ("y11 = ") , input ("z11 = "))
# # varianta1
# if x11>y11 and x11>z11:
#     print(f"x11 este cel mai mare si are valoarea = {x11}")
# elif x11 == y11 and x11>z11:
#     print(f"x11 si y11 sunt egale si au valoarea = {x11} mai mare ca z11")
# elif x11 == z11 and x11>y11:
#     print(f"x11 si z11 sunt egale si au valoarea = {x11} mai mare ca y11")
# elif y11>x11 and y11>z11:
#     print(f"y11 este cel mai mare si are valoarea = {y11}")
# elif y11 == z11 and y11>x11:
#     print(f"y11 si z11 sunt egale si au valoarea = {y11} mai mare ca x11")
# elif z11>y11 and z11 >x11:
#     print(f"z11 este cel mai mare si are valoarea = {z11}")
# else:
#     print("cele 3 sunt egale")
# print(" ")
#
# # varinata 2
# if x11>=y11>=z11:
#     print ("Varianta 1")
# elif y11>=x11>=z11:
#     print("Varianat 2")
# else:
#     print ("Varianta 3")
# -----------------------------------------------------------------------------------------------------------------------
print("Tema 15 - S2")
"""
15. x, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
 """
x12 , y12 , z12 = (input ("x12 = "), input ("y12 = ") , input ("z12 = "))
# x12, y12, z12 = map(int, input().split())
Suma_unghiuri = int(x12)+int(y12)+int(z12)
print(Suma_unghiuri)
if int(x12)>0 and int(y12)>0 and int(z12)>0 :
    if Suma_unghiuri < 180 :
        print ("Triunghiul nu exista - nu se inchide")
    elif Suma_unghiuri > 180 :
        print ("Nu exista un triunghi cu suma unghiurilor > 180 ")
    else:
        print("Avem un triunghi echilateral" if (x12 == y12 == z12) else "Este un triunghi oarecare")
else:
    print ("Nu este triunghi")
print(" ")

# varianta 2
print("varianta 2")
Suma_unghiuri = int(x12)+int(y12)+int(z12)
if Suma_unghiuri == 180 and int(x12)>0 and int(y12)>0 and int(z12)>0 and ( x12 == 90 or y12 == 90 or z12 == 90 ) :
    print("Este un triunghi dreptunghic")
elif x12 == y12 == z12 and Suma_unghiuri == 180 :
    print("Este un triunghi echilateral")
elif x12 == y12 or x12 == z12 or y12 == z12 and int(x12)>0 and int(y12)>0 and int(z12)>0 and Suma_unghiuri == 180 :
    print("Este un triunghi isoscel")
elif Suma_unghiuri == 180 and int(x12)>0 and int(y12)>0 and int(z12)>0:
    print ("Triunghiul exista oarecare")
elif int( x12 == 90 and y12 == 90 ) or int( x12 == 90 and  z12 == 90 ) or int( y12 == 90 and z12 == 90):
    print ("Nu exista triunghi")
elif Suma_unghiuri < 180 :
    print ("Nu exista triunghi ")
else:
    print("Nu este triunghi")
print(" ")

# varainat 3




# -----------------------------------------------------------------------------------------------------------------------
# print("Tema 16 - S2")
# """
# 16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ●	Citește de la tastatură un int x
# ●	Afișează stringul fără ultimele x caractere
#  """
# text = "Coral is either the stupidest animal or the smartest rock"
# x13 = input ("x = ")
# print (x13)
# x = int(x13)
# text = text[:-x]
# print(text)
# # print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 17 - S2")
# """
# 17. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# Declară un string nou care să fie format din primele x(5) caractere + ultimele y(5).
#  """
# text = "Coral is either the stupidest animal or the smartest rock"
# x14 = input ("x14 = ")
# y14 = input ("y14 = ")
# print (x14)
# print (y14)
# x = int(x14)
# y = int(y14)
# primele_x_caractere = text[:x]
# ultimele_y_caractere = text [-y:]
# text = primele_x_caractere + " '< primele > si < ultimele >' " + ultimele_y_caractere
# print(text)
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 18 - S2")
# """
# 18. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ●	Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
# ●	Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
# ●	output: 'Coral is either the stupidest animal or the smartest'
#  """
#
# text = "Coral is either the stupidest animal or the smartest rock"
# y15 = "rock"                                    # a fost ales cuvantul ROCK din tema
# index_cuvant = text.find(y15)
# print(index_cuvant)
# y = int(index_cuvant)
# primele_y_caractere = text[:y]
# print(primele_y_caractere)
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 19 - S2")
# """
# 19. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random - TOTAL GRESIT
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Ia numărul ghicit de la utilizator
# Verifică și afișează dacă utilizatorul a ghicit
# Vei avea 3 opțiuni
# ●	Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# ●	Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# ●	Ai ghicit. Felicitări! Ai ales x si zarul a fost y, unde x=y.
# """
# import random
# x16 = int(input("x16 ="))
# print (x16)
# nr_random = random.randint (1, 6)
# print (nr_random)
# if x16 < nr_random:
#     print (f"Ai pierdut, nr tau este mai mic x16 = {x16} < nr_random = {nr_random}")
# elif x16 > nr_random:
#     print(f"Ai pierdut, nr tau este mai mare x16 = {x16} > nr_random = {nr_random}")
# else:
#     print(f"Bravo, cele doua numere sunt egale {x16} = {nr_random}")
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 20 - S2")
# """20. Citește de la tastatură un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
# """
#
# text20 ="In toate cazurile apa curge la vale de pe versantul muntelui"
# primul_caracter = text20[0]
# ultimul_caracter = text20[-1]
# assert primul_caracter.lower() == ultimul_caracter.lower() , "caracterele nu sunt identice"
# print (" daca nu am primit mesaj 'AssertionError' atunci caracterele sunt la fel dar nu IDENTICE")
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 21 - S2")
# """ Tema 21 - S2
# Având stringul '0123456789'
# ●	Afișează doar numerele pare
# ●	Afișează doar numerele impare
# (hint: folosește slicing, controlează din pas)
# """
#
# string ="0123456789"
# print(f"Numerele pare sunt = {string [::2]}")
# print(f"Numerele impare sunt {string [1::2]}")
# print(" ")
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ----------------------------------------------------------------------------------------------------------------------
# # ----------------------------------      Exemplu JAVA vs PYTHON      --------------------------------------------------
# #
# # # Exercitiu de testare ------ OPERATORI TERNARI
# #
# # """
# # -Urmatoarele 2 linii de cod din JAVA:
# # int x = 3;
# # System.out.println( x < 11 ? "Este mai mic ca 11": " Nu este mai mare ca 11");
# # """
# #
# #
# # """
# # - in PYTHON se scrie astfel :                                                                                 """
# # x = 13
# # print ("Este mai mic ca 11" if x< 11 else "Este mai mare ca 11")