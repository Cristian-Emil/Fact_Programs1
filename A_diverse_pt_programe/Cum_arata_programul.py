A = 5                               # aceasta este o constanta = A
B = 2.5                             # aceasta este o constanta = B
a = int(input("a = "))              # aceasta este o variabila si trebuie s-o introducem de la tastatura a =
b = float(input("b = "))            # aceasta este o variabila si trebuie s-o introducem de la tastatura b =

def suma(a,b):                      # subprogramul 1 cu functia SUMA
    return a+b

def produs(a,b):                    # subprogramul 2 cu functia PRODUS
    return a*b

var1 = "valoare variabila"          # se atribuie valoarea "valoare variabila" variabilei "var1"

if var1 == "x":                     # acesta este programul principal
    suma(a,b)
    produs(a, b)

print (suma(A,a))                   # afisam rezulatele executiei functiilor SUMA si PRODUS
print (produs(A,a))
print (suma(A,b))
print (produs(A,b))
print (suma(a,B))
print (produs(a,B))
print (suma(b,B))
print (produs(b,B))
print (suma(a,b))
print (produs(a,b))
print (suma(A,B))
print (produs(A,B))