""" Tema 2 - S2
 2. Verifică și afișează dacă x este număr natural sau nu.
"""
x = int(input("introdu numarul = "))
if x > 0 :
    print("numarul este natural")
else :
    print("numarul nu este natural")
print()

""" Tema 3 - S2
3. Verifică și afișează dacă x este pozitiv, negativ sau neutru.
"""
x = int(input("introdu numarul = "))
if x > 0 :
    print("numarul este pozitiv")
elif x< 0:
    print("numarul este negativ")
else :
    print("numarul nu este neutru")
print()

""" Tema 4 - S2
4. Verifică și afișează dacă x este intre -2 si 13.
"""

x = int(input("introdu numarul = "))
if -2 <= x <= 13:
    print ("Numarul este in interval")
else :
    print("Numarul nu este in interval")
print()

""" Tema 5 - S2
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5
"""
x = input("x = ")
y = input("y = ")

z = x - y
if z < 5:
    print(f"Diferenta este mai mica ca 5 , x-y = {z}")
else:
    print(f"Diferenta este mai marte ca 5 , x-y = {z}")

""" Tema 6 - S2
6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
"""
#varianta 1
x = int(input ())
print(x)
if not( 5 <= x) :
    print(f" este mai mic sau egal cu 5, x= {x}")
elif not( x <= 27):
    print (f" este mai mare sau egal cu 27, x= {x}")
else :
    print (f" este intre 5 si 27 , x = {x}" )

# varianta 2
x = int(input ("x = "))
if not(5 <= x<= 27):
    print (f"nu este intre 5 si 27, x= {x}")
else:
    print (f"este inte 5 si 27 , x = {x}" )

""" Tema 7 - S2
7.x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
"""
""" avem valori fise definite 
x , y = 4 , 7 """
# sau varianta cu intrducere de la tastatura :

x4 = input ("x4 = ")
y4 = input ("y4 = ")
if x4 == y4:
    print (f"cele doua sunt egale ")
elif x4>y4:
    print (f"x4 este mai mare ce y4" )
else:
    print(f"y4 este mai mare ce x4")

# sau se poate scrie simplficat
x5 , y5 = (input ("x5 = "), input ("y5 = "))
if x5 == y5:
    print (f"x5 si y5 sunt egale ")
else:
    print("x5 este mai mare" if x5 > y5 else "y5 este mai mare ca x5")


""" Tema 10 - S2 10. Transforma Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 5 => E
4 sau mai mic  => F """

nota = 10
if nota >9:
    print("A")
elif nota >8:
    print("B")
elif nota >7:
    print("C")
elif nota >6:
    print("D")
elif nota >5:
    print("E")
else:
    print("F")
print()


""" Tema 21 - S2
Având stringul '0123456789'
●	Afișează doar numerele pare
●	Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)
"""

string ="0123456789"
print(f"Numerele pare sunt = {string [::2]}")
print(f"Numerele impare sunt {string [1::2]}")