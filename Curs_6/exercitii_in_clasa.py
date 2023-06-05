"""
------------------------------------------------------------------------------------------------------------------------
Exercitii de testare
"""
class Caine:
    rasa = ""
    nume =""
    varsta =0

    def __init__(self, rasa, nume, varsta = 0):
        self.rasa = rasa
        self.nume = nume
        if varsta >= 0:
            self.varsta = varsta
        else:
             raise Exception ("Varsta nu poate sa fie negativa")

caine1 = Caine("labrador" , "Mark" , 2 )
caine2 = Caine("ciobanesc" , "Mike" , 0.1)
caine3 = Caine("buldog" , "Rex" , 3)

caine2.varsta = 2

if caine1.varsta > caine2.varsta and caine1.varsta > caine3.varsta:
    print(f"{caine1.nume} este mai mare")
elif caine2.varsta > caine3.varsta:
    print(f"{caine2.nume} este mai amre")
else:
    print(f"{caine3.nume} este cel mai mare")

nume = input("nume = ")
rasa = input("rasa = ")
varsta = int(input("varsta = "))

caine4 = Caine(rasa , nume , varsta)
print(f"{caine4.nume} este un {caine4.rasa} si are {caine4.varsta} ani")

# print(caine1.varsta())
# print(caine2.rasa() )
