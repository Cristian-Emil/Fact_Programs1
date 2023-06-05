"""
Cursul 7 - saptamana 4

ENCAPSULATION - INCAPSULAREA
"""
class Masina:
    __color = "gri"                 # cele doua bare jos spune ca este un PRIVAT

    # def __init__(self):
    def arata_culoare(self):                            # metode GETTER -
        return self.__culoare

    def seteaza_culoare(self, culoare):                 # metode SETTER -
        if type(culoare) != str:
            raise TypeError ("Culoarea trebuie sa fie string")
        self.__culoare = culoare


masina = Masina()
print(masina)               # este protejat si ne da mesaj de protectie

masina.culoare = 32
# masina.seteaza_culoare(123)


print(masina)               # este protejat si ne da mesaj de protectie
masina.__culoare = 35
print(masina.__culoare)
masina.seteaza_culoare("roz")
print(masina.seteaza_culoare("culoare"))