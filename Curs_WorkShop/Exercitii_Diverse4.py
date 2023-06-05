"""
Incaplsulare
"""
# class Motor():
#     __culoare = "gri"
#
#     def get_culoare(self):
#         return self.__culoare
#
#     def set_culoare(self, alta_culoare):
#         self.__culoare = alta_culoare
#
#     def __ascunsa(self):
#         pass
#
# m = Motor()
# print("Afisam culoare default , cea definita initial")
# print(m.get_culoare())
#
# print("Definim noi o noua culoare")
# m.set_culoare = "rosu"
# print(m.get_culoare())
# print(" ")
# ----------------------------------------------------------------------------------------------------------------------

class Masinutza:

    def __init__(self, culoare):
        self.__culoare = culoare

    @property
    def culoare(self):
        return self.__culoare

    @culoare.getter
    def culoare(self):
        print(f"Getter: culoarea este {self.__culoare}")
        return self.__culoare

    @culoare.setter
    def culoare(self, culoare):
        print(f"Getter: culoarea este {self.__culoare}")
        self.__culoare

    @culoare.deleter
    def culoare(self):
        print(f"Getter: culoarea este {self.__culoare}")
        self.__culoare

masina = Masinutza(" ")
masina.culoare = "rosie"
masina.culoare
