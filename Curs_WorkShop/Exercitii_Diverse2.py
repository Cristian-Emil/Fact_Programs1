"""
Polimorfism
"""
class Tara():
    def teritoriu(self):
        print("Are suprafata mare")
    def limba(self):
        print("Are limba nationala")

class Romania():
    def teritoriu(self):
        print("Romania se intinde de la Nord de Dunare pana dincolo de Cernauti")
    def limba(self):
        print("Limba Romana")

class Tara_lu_Papura(Tara):
    pass

print("")
tari = [Tara(), Romania(), Tara_lu_Papura()]
print("Varianta 1")
for tara in tari:
    print(" ")
    tara.teritoriu()
    tara.limba()


# sau declaram tarile cu un constructor si le implementam
tara1 = Tara()
tara2 = Romania()
tara3 = Tara_lu_Papura()
print("Varianta 2")
for tara in (tara1, tara2, tara3):
    print(" ")
    tara.teritoriu()
    tara.limba()



