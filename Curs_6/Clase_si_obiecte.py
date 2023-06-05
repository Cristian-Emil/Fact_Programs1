"""
Cum se defineste o clasa si cum se utilizeaza
"""

class Carbonara:
    oua = 2
    bacan_gr = 150
    spagheti_gr = 100

    def taie_bacon(self):
        print("Am taiat baconul")

    def amesteca(self):
        print ("Am amestecat toate ingredientele")

print("Portia tip 1")
carbonara1 = Carbonara()
print(carbonara1.oua)
print(carbonara1.bacan_gr)
print(carbonara1.spagheti_gr)

carbonara1.taie_bacon()

print(" ")

print("Portia tip 2")
carbonara2 = Carbonara()
carbonara2.oua = 3
carbonara2.spagheti_gr = 70

print(carbonara2.oua)
print(carbonara2.bacan_gr)
print(carbonara2.spagheti_gr)

print(" ")

class Triunghi:
    a=10
    b=20
    c=18
    def perimetrul(self):
        a = "salut"
        print(self.a)                       # este un atribut
        return self.a + self.b + self.c

print("Triunghiul 1")
t1 = Triunghi()
t1.perimetrul()
print(t1.perimetrul())

print(" ")

print("Triunghiul 2")
t2 = Triunghi()
t2.b = 22
print(t2.perimetrul())

print(" ")

print("Valorile lui b pentru t1 si t2")
print(t2.b)
print(t1.b)


class Triunghi1:
    a_1=10
    b_2=20
    c_3=18
    def perimetrul(self, multiplicare=1):
        a_1 = "salut"
        print(self.a_1)                                             # este un atribut
        return multiplicare * (self.a_1 + self.b_1 + self.c_1)

#print(t2. perimetrul(2))


#-----------------------------------------------------------------------------------------------------------------------

class Car:
    marca = "Dacia"
    model = None
    year = 2022
    color = None

    def accelerare(self):
        print("Am crescut viteza")

car = Car()
print(car.marca)

car.marca = "Renault"
print(car.marca)

print("")
# ----------------------------------------------------------------------------------------------------------------------
""" deci putem sa initializam o alta valoare pentru clasa  """

class Car1:
    marca1 = " "
    model1 = None
    year1 = 2021
    color1 = None

    # def __init__(self, marca1):
    #     self.marca1 = marca1

    def accelerare1(self):
        print("Am crescut viteza")

car1 = Car1()                  # aceasta linie n-o sa mearga atat timp cat avem definit __init__
#car1 = Car1("Audi")           # aceasta linie n-o sa mearga atat timp cat am comentat __init__
print(car1.marca1)

car1.marca1 = "Volvo"
print(car1.marca1)

#-----------------------------------------------------------------------------------------------------------------------