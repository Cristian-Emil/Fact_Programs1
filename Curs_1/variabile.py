"Variabilele sunt zone din memeorie unde sunt stocate diferite valori"

""" Reguli pentru scrierea variabilelor
1) Numele variabiulelor incep cu o litera sau underscore (_)
Inceperea cu o cifra nu este permisa ( kla fel ca in Java)

2)Numele variabilelor nu pot contine caractere speciale
Ele pot contine litere, numere si undescore ( adica minus jos = _ )
"""

nume = "Program Python"
numar = 101

print(nume)
print(numar)
print("")

""" Acum tiparesc o variabila """
varsta = 28
print(varsta)
print( type(varsta))
print("")
""" Acum tiparim un string """
varsta = "28"
print(varsta)
print( type(varsta))

""" La tiparire se observa ca prima variabila VARSTA e INT iar a doua variabila este STRING. """
""" Asta pt ca sunt definite diferit """

print("")
x=12.3
y=15.1
z=x+y
""" Se pot scrie in ambele feluri """
print(x+y)
print(z)

print("")

str_1 = "Este sirul 1"
str_2 = "Este sirul 2"
nr=101

#sau putem scrie un rand gol cu nimic intre paranteze
print()
#tiparim diferite texte
print(str_1 + " " + str_2 + "  =  " + str(nr))
"""sau"""
nr=str(nr)
print(str_1 + " " + str_2 + "  =  " + nr)

#exemple de variabile :
print("")
x,y,z = "Portocale" , "Banane" , "Visine"
a=b=c= "Mere"

print(x)
print(y)
print(z)
print("")
print(a)
print(b)
print(c)