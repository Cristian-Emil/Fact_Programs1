# print("Tema 1 - S2")
""" Tema 1 - S2
 1. Cum funcționează un if else.
Un "if-else" este o structură de control de flux în majoritatea limbajelor de programare, care permite programatorilor
să execute anumite acțiuni în funcție de o condiție specifică
Structura de bază a unui if-else este următoarea:

if (conditie) {
  //Blocul de cod care se va executa daca conditia este adevarata
} else {
  //Blocul de cod care se va executa daca conditia este falsa
}
Condiția este o expresie care poate fi evaluată ca fiind adevărată sau falsă. Dacă condiția este adevărată, blocul de
cod din interiorul primei acolade va fi executat, iar dacă condiția este falsă, blocul de cod din interiorul celei de-a
doua acolade va fi executat

Deci IF-ELSE este de genul unui macaz si mergem pe o linie sau alta in functie de modul in care a fost schimbat macazul.
"""
#-----------------------------------------------------------------------------------------------------------------------
print("Tema 2 - S2")
""" 
 2. Verifică și afișează dacă x este număr natural sau nu.
"""
x = int(input("introdu numarul = "))
if x > 0 :
    print("numarul este natural")
else :
    print("numarul nu este natural")
print(" ")
#-----------------------------------------------------------------------------------------------------------------------
print("Tema 3 - S2")
""" 
3. Verifică și afișează dacă x este pozitiv, negativ sau neutru.
"""
x = int(input("introdu numarul = "))
if x > 0 :
    print("numarul este pozitiv")
elif x< 0:
    print("numarul este negativ")
else :
    print("numarul nu este neutru")
print(" ")
#-----------------------------------------------------------------------------------------------------------------------
print("Tema 3 - S2")
""" 
4. Verifică și afișează dacă x este intre -2 si 13.
"""
x = int(input("introdu numarul = "))
if -2 <= x <= 13:
    print ("Numarul este in interval")
else :
    print("Numarul nu este in interval")
print(" ")
#-----------------------------------------------------------------------------------------------------------------------
print("Tema5 - S2")
""" 
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5
"""
x1 = input ("x1 = ")
y1 = input ("y1 = ")
z = x1 - y1
if z < 5:
    print (f"Diferenta este mai mica ca 5 , x1-y1 = {z}")
else:
    print(f"Diferenta este mai marte ca 5 , x1-y1 = {z}")
print(" ")
#-----------------------------------------------------------------------------------------------------------------------
print("Tema 6 - S2")
""" 
6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
"""
# varianta 1
x2 = int(input ())
print(x2)
if not( 5 <= x2) :
    print(f" este mai mic sau egal cu 5, x= {x2}")
elif not( x2 <= 27):
    print (f" este mai mare sau egal cu 27, x= {x2}")
else :
    print (f" este intre 5 si 27 , x = {x2}" )

# varianta 2
x3 = int(input ("x = "))
if not(5 <= x3<= 27):
    print (f"nu este intre 5 si 27, x3 = {x3}")
else:
    print (f"este inte 5 si 27 , x3 = {x3}" )
print(" ")
#-----------------------------------------------------------------------------------------------------------------------
print("Tema 7 - S2")
"""
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
print(" ")
#-----------------------------------------------------------------------------------------------------------------------
print("Tema 8 - S2")
"""
8. x , y , z sunt laturile unui triunghi .
"""
x6 , y6 , z6 = 2 , 2 , 2
if x6 == y6 == z6:
    print ("Triunghi echilateral")
else:
    print("Triunghi oricare")

x7 , y7 , z7 = 2 , 3 , 3
if x7 == y7 or x7==z7 or y7==z7 :
    print ("Triunghi isoscel")
else:
    print("Triunghi oricare")
print(" ")
#-----------------------------------------------------------------------------------------------------------------------
print("Tema 9 - S2")
""" 
9. Verifica daca e vocala sau consoana .
"""
x8 = "a"
if x8.lower() in ("a", "e" , "i" , "o" , "u"):
    print ("Sunt vocale")
else:
    print("Sunt consoane")
print(" ")
#-----------------------------------------------------------------------------------------------------------------------
print("Tema 10 - S2")
""" 10. 
Transforma Peste 9 => A
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
print(" ")
#-----------------------------------------------------------------------------------------------------------------------

"""
Continuarea exercitiilor , punctele 11 la 21 sunt in folderul/package

Tema2_S2_Part2.py

"""