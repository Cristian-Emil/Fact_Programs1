"""
---------------------------------------- INHERITANCE = MOSTENIRE -------------------------------------------------------
Definim o clasa CHEF
"""
"""
---------------------------------------- POLYMORPHISM = POLIMORFISM -------------------------------------------------------
Definim 3 clase - Tara , Romania si USA
Si apoi le atribuim caracteristici
"""
class Tara:
    def limba(self):
        print("Oarecare")

class Romania:
    def limba(self):
        print("Romana")

class USA:
    def limba(self):
        print("Engleza")

class Namibia(USA):
    pass

# instantiem cele 2 clase prin 2 variabile
tara_1 = Romania
tara_2 = USA
tara_3 = Tara
# sau putem sa definim o lista in care sa punem cele 2 variabile
# tari = [ Romania(), USA() ]                           # acesta efiseaza limba doar pentru Romania si USA
# tari = [ Romania(), USA() , Tara()]                   # acesta efiseaza limba pentru Romania, USA si Tara
# tari = [ Romania(), USA() , Tara() , USA()]           # acesta efiseaza limba pentru Romania, USA, Tara si USA
tari = [ Romania(), USA() , Namibia() , Tara() ]        # acesta efiseaza limba pentru Romania, USA, Namibia si Tara

# apelam metoda "tara" :
for tara in tari:
     tara.limba()
print(" ")
# ----------------------------------------------------------------------------------------------------------------------

"""Facem aceeasi definire dar pentru numere"""
print("Varianta 1")
# si 3 numere variabile ce trebuie instantiate/apelate
def suma (a1, b1, c1):
    return a1 + b1 + c1

print(suma(10, 20, 30))                 # aici definim numerele pe care trebuie sa le adunam
# print(suma(10, 15))                   # pt ca nu am definit c1 - suma() missing 1 required positional argument: 'c1'
print(" ")

print("Varianta 2")
# si 2 numere variabile ce trebuie apelate/instantiate si o constanta
def suma (a2, b2, c2=5):
    return a2 + b2 + c2

print(suma(15, 25, 35))                 # aici definim numerele pe care trebuie sa le adunam
print(suma(10, 15))                     # pt ca in suma am definit c2=5 - nu da eroare si il aduna pe acesta
print(" ")

#----------------------------------------------------------------------------------------------------------------------
print("Varianta 3")
# si 2 numere variabile ce trebuie apelate/instantiate si o constanta
def suma (a3, b3):
    return a3 + b3

print(suma(15, 25))
print(suma((10, 20), (15, 25)))                 # aici definim un TUPLE si o sa iasa unul concatenat
print("")
#----------------------------------------------------------------------------------------------------------------------
print("Varianta 4")
"""Ca sa nu concateneze cele 2 tuple o sa trebuie sa le adunam ca tuple"""
def suma (a4, b4):
    if isinstance(a4, tuple) is tuple and isinstance(b4, tuple):
        return a4[0] + b4[0], a4[1] + b4[1]

    return a4+ b4

print("Tipul 1 de raspuns")
print(suma((10, 20), (15, 25)))                 # aici definim un TUPLE si o sa iasa unul concatenat

print("Tipul 2 de raspuns")
a4=(20, 40)
b4=(25, 45)
print(suma(a4, b4))

print("")
print("Avem varianta de afisare cand punem orice fel/tip de argumente folosind sintaxa - *args ")
def f(*args, ):
    print(args)
    print(type(args))
    print(len(args))

f(10, "dans", 40, 50)

print("")
print("Avem varianta de afisare cand punem nume - *kargs ")
def f(*kargs, ):
    print(kargs)
    print(type(kargs))
    print(len(kargs))

f("Ion", "Pas", "Marin", "Copac")