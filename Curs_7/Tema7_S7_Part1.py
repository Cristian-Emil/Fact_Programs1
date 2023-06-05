"""Testul contine 4 exercitii
Avem execitiil de la 1 la 4
"""
# #----------------------------------------------------------------------------------------------------------------------
# print("Tema 1 - S7")
# """
# ABSTRACTION
# # Clasa abstractă FormaGeometrica
# # Conține un field PI=3.14
# # Conține o metodă abstractă aria (opțional)
# # Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’
# # """
# print(" ")
# from abc import ABC, abstractmethod
#
# class Forma(ABC):
#     PI = 3.14                               # este un field unde este definit PI
#
#     @abstractmethod
#     def aria(self):
#        pass
#        # raise NotImplemented
#
#     @staticmethod
#     def descriere(self):
#         print("Cel mai probabil am colturi")
#
#
# Forma.aria("self")
# Forma.descriere("self")
#
# print(" ")
# # #----------------------------------------------------------------------------------------------------------------------
# # print("Tema 2 - S7")
# # """
# # INHERITANCE - MOSTENIRE
# # Clasa Pătrat - moștenește FormaGeometrica
# # constructor pentru latură
# # """
# # from abc import ABC, abstractmethod
# #
# # class Forma(ABC):
# #     def __init__(self):
# #         pass
# #     print("Forme Geometrice")
#
# class Patrat(Forma):
#     def __init__(self, latura):
#         self.latura = latura
#
#     def descr(self):
#         print("Este forma cu colturi")
#
#     def aria(self):
#         return self.latura**2
#
#     def perimetru(self):
#         return self.latura*4
#
# patrat = Patrat(7)
# print("")
# patrat.descr()
# patrat.aria()
# patrat.perimetru()
# print(f"Are suprafata de {patrat.aria()}")
# print(f"Are perimetrul de {patrat.perimetru()}")
# print(" ")
# #----------------------------------------------------------------------------------------------------------------------
print("Tema 3 - S7")
"""
ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar
dacă ai ales să implementezi metoda abstractă aria)
"""

print(" ")
class Forma:
    __latura = "latura"
    PI = 3.14

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print("Latura are minim o dimensiune - lungime")

    @latura.setter
    def latura(self, latura):
        print("Definim dimensiunea 'lungime latura'")
        self.__latura = latura

    @latura.deleter
    def latura(self):
        self.__latura = "latura"

l = Forma()

l.latura
l.latura = "A"

class Cerc(Forma):
    __raza = "raza"
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print("Raza este o caracteristica a cercului")

    @raza.setter
    def raza(self, raza):
        print("Definim dimensiunea 'lungime raza'")
        self.__raza = raza

    def aria_cercului(self, raza):
        return self. PI * raza**2

    @raza.deleter
    def raza(self):
        self.__raza ="raza"

c = Cerc("")
print("")
c.raza
# c.aria_cercului(5)
print(f"Aria cercului este {c.aria_cercului(5)}" )
print(" ")
#----------------------------------------------------------------------------------------------------------------------
print("Tema 4 - S7")
"""
POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Pătrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui

"""
print(" ")
class Forma:
    def descrie(self):
        print("Eu nu am colturi")

class Patrat:
    def propr(self):
        print("Am cele 4 laturi egale si un unghi de 90 grd ")

    def aria_patrat(self, latura):
        return latura**2


patrat = Patrat()


patrat.propr()
print(patrat.aria_patrat(5))
print("\nPutem sa scriem si prin introducerea unei variabile 'arie'")
arie = patrat.aria_patrat(7)
print(arie)
# print(" ")
# #----------------------------------------------------------------------------------------------------------------------
#
# print("__ private, _ protected, public")
# print("__ private , este doar in clasa in care a fost definita")
# print("_ protected, este in clasa in care a fost definita si in cele care o mostenesc ")
# print("__ private, este vizibila in toate clasele")