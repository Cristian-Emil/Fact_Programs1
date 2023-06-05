class Masina:
    __culoare = "gri"                 # cele doua bare jos spune ca este un PRIVAT

    @property
    def culoare(self):
        return self.__culoare

    @culoare.getter
    def culoare(self):                          #- definirea GETTER
        print("Am returnat culoarea")
        return self.__culoare

    @culoare.setter
    def culoare(self, culoare):                          #- definirea SETTER
        print("Setam culoare")
        if type(culoare) != str:
            raise TypeError("Culoarea trebuie sa fie STRING")
        self.__culoare = culoare

    @culoare.deleter
    def culoare(self):
        self._culoare ="gri"


m = Masina()

print(m.culoare)
m.culoare = 'rosu'
print(m.culoare)

del m.culoare

print(m.culoare)

#-----------------------------------------------------------------------------------------------------------------------
"""
class Masina:
    culoare = 'gri'

    @property
    def culoare(self):
        return self.culoare

    @culoare.getter
    def culoare(self):
        print('Returnam culoarea')
        return self.culoare

    @culoare.setter
    def culoare(self, culoare):
        print('Setam culoarea')
        if type(culoare) != str:
            raise TypeError('culoarea trebuie sa fie string')
        self.culoare = culoare

    @culoare.deleter
    def culoare(self):
        print('Stergem culoarea')
        self.__culoare = 'gri'


m = Masina()

print(m.culoare)
m.culoare = 'rosu'
print(m.culoare)

del m.culoare

print(m.culoare)
"""