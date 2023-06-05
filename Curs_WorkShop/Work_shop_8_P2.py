from abc import ABC, abstractmethod

class Vehicul(ABC):
    @abstractmethod
    def porneste(self):
        raise NotImplemented

    @abstractmethod
    def transporta(self):
        raise NotImplemented

    @abstractmethod
    def viteza_max(self):
        raise NotImplemented

    @abstractmethod
    def capacitate_max(self):
        raise NotImplemented


class Motoreta(Vehicul):
    def porneste(self):
        print("Trebuie pusa pe liber")

    def transporta(self):
        print("Transporta maxim 2 persoane")

    def viteza_max(self):
        print("Foarte mare si periculoasa")

    def capacitate_max(self):
        print("Este mica capacitatea de transport")

class Motocicleta_cu_atas(Motoreta):
    def transporta(self):
        print("Transporta maxim 3 persoane")

    def viteza_max(self):
        print("Este ceva mai lenta")

# avem o metoda individuala
    def numar_roti(self):
        print("Are 3 roti si una de rezerva")

moto1 = Motocicleta_cu_atas()

moto1.porneste()
moto1.transporta()
moto1.viteza_max()
moto1.capacitate_max()
moto1.numar_roti()
print()


class Scuter(Motoreta):
    def viteza_max(self):
        print("Este si mai lenta")

    def consum(self):
        print("Consuma foarte putin comparativ cu restul")

moto2 = Scuter()

moto2.porneste()
moto2.transporta()
moto2.viteza_max()
moto2.capacitate_max()
moto2.consum()
print()

# aici avem o mostenire din 2 clase definite - una anterior Motocicleta_cu_atas  si alta Vehicul_de_teren
class Vehicul_de_teren():
# avem o metoda individuala
    def rezistenta(self):
        print("Rezista pe teren accidentat")

# avem o metoda individuala
    def fiabil(self):
        print("Este fiabila in conditii extreme")

off_road = Vehicul_de_teren()
off_road.rezistenta()
off_road.fiabil()
print()

class Vehicul_facut_de_mana(Motocicleta_cu_atas, Vehicul_de_teren):
    def fiabil(self):
        print("Este ceva mai putin fiabil")

    def aspect(self):
        print("Are aspect ciudat")

    def transporta(self):
        print("Nu definit numar de locuri ")

chestie_facuta = Vehicul_facut_de_mana()
chestie_facuta.fiabil()
chestie_facuta.aspect()
chestie_facuta.transporta()

print()
"""" Conteaza foarte mult cum sunt definite metodele, o sa le citeasca din stanga spre dreapta.
Deci o ia pe prima din stanga si o citeste spre dreapta

ATENTIE:
Se poate face o clasa si nu trebuie sa definim ceva in ea: se scrie clasa si apoi sa scrie pass
"""
class Vehicul_de_mana( Motocicleta_cu_atas, Scuter):
    pass

vehicul3 = Vehicul_de_mana()

vehicul3.viteza_max()
# O sa ia valorea primului citit din lista, aici de la Motocicleta_cu_atas