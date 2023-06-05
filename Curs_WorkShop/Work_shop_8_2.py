from abc import ABC, abstractmethod

class Vehicul(ABC):
    @abstractmethod
    def porneste(self):
        raise NotImplemented

    @abstractmethod
    def transporta(self):
        raise NotImplemented

    @abstractmethod
    def max_speed(self):
        raise NotImplemented

    @abstractmethod
    def capacitate_maxima(self):
        raise NotImplemented

class Motoreta(Vehicul):
    def porneste(self):
        print('trebuie pusa pe liber si face galagie')

    def transporta(self):
        print('maxim 2 persoane')

    def max_speed(self):
        print('mare')

    def capacitate_maxima(self):
        print('mica')

class MotocicletaCuAtas(Motoreta):

    def transporta(self):
        print('maxim 3 persoane')

    def max_speed(self):
        print('ceva mai mica')

    #metoda individuala
    def numar_roti(self):
        print('are 3 roti')

class Scuter(Motoreta):

    #suprascriem  doar ce ne intereseaza, restul se mosteneste
    def max_speed(self):
        print('merge foarte incet')

    def consum(self):
        print('consuma foarte putin')

class VehiculDeTeren():
    def rezistenta(self):
        print('este foarte rezistent')

    def fiabilitate(self):
        print('speri sa nu se strice')

#aici am facut o mostenire din 2 parinti, asa am pastrat procedurile fiecareia
class VehiculHandMade(MotocicletaCuAtas, VehiculDeTeren):
    def fiabilitate(self):
        print('sigur se strica')

    def cum_arata(self):
        print('arata foarte ciudat')


#daca punem 2 clase cu aceleasi metode suprascrise, sa va lua medota trecuta prima ca parinte
class VehiculFacutAcasa(MotocicletaCuAtas, Scuter):
    pass



moto1 = MotocicletaCuAtas()
moto1.numar_roti()
moto1.transporta()
moto1.porneste()

print()
moto2 = Scuter()
moto2.transporta()
moto2.consum()

print()
chestie = VehiculHandMade()
chestie.porneste()
chestie.rezistenta()
chestie.cum_arata()
chestie.fiabilitate()

print()
moto3 = VehiculFacutAcasa()
moto3.max_speed()