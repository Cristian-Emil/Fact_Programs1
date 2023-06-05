"""
1)  Pastreaza mai multe valori imbutabile intr-o singura variabila
2)  Valorile sunt ordonate, incep de la index 0
3)  Valorile sunt imutabile, odata definite, asa raman. Nu se mai pot adauga/sterge valori
4)  Accepta valori duplicate
5)  Putem folosi len() pentru a afla dimensiunea

"""

thistuple = ("mere" , "banane" , "cirese")
print(thistuple)
print(len(thistuple))
print("  ")


echipe = ("Real Madrid" , "Barcelona" , "Juventus" , "Ajax" , "Barcelona")
print(echipe)
print(echipe[0])
print(echipe[1])
print(echipe[2])
print(echipe[3])
print(echipe[4])
print(len(echipe))

#echipa[1] = Ajax -     # se observa ca daca incercam sa insseram o valoare pe o anumita pozitie nu se poate, da eroare




# exercitiu si gimnastica de degete:
numere = (12 , 35, 43, 11, 31)
print(numere)
print(numere[1:-1])
subsir= numere[1:-1]        # este un tuple care nu are numerele 12 si 31
if subsir [0] > subsir[-1]:
    print("Primul numar este mai mare")
else:
    print ("Ultimul numar este mai mare")
