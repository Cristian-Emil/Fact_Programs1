"""
Minioproiect A
-------------------------------------------------------------------------------------------------------------------------
Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori disponibile (set), înmatriculată (bool)
   Culoare = gri - toate mașinile când ies din fabrică sunt gri
   Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
   Culori disponibile = alege tu 5-7 culori
   Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
   Înmatriculată = False
Constructor: model, viteza_maxima
Metode:
descrie() - se vor printa toate atributele, în afară de culori_disponibile
înmatriculare() - va schimba atributul înmatriculată în True
vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua culoare e în opțiunea de culori disponibile,
altfel afișați o eroare
accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e negativă-eroare, dacă viteza e mai mare decât
viteza_max - masina va accelera până la viteza maximă
franeaza() - mașina se va opri și va avea viteza 0
"""


class Masina:
    __marca = 'Dacia'
    __model = ''
    __viteza_maxima = 0
    __culoare = 'gri'
    __culori_dispponibile = {'rosu', 'albastru', 'negru', 'alb', 'verde'}
    __inmatriculata = False
    __viteza_actuala = 0

    def __init__(self, model, viteza_maxima):
        self.__model = model
        self.__viteza_maxima = viteza_maxima

    @property
    def viteza_maxima(self):
       return self.__viteza_maxima

    @viteza_maxima.setter                                                                          # aici este setter-ul
    def viteza_maxima(self, viteza):
        self.__viteza_maxima = viteza

    @viteza_maxima.getter                                                                          # aici este getter-ul
    def viteza_maxima(self):
        return self.__viteza_maxima

    @viteza_maxima.deleter                                                                        # aici este deleter-ul
    def viteza_maxima(self):
        self.__viteza_maxima = 0


    def __str__(self):                                                                  #functie built-in pentru afisare
        return (f' Marca:{self.__marca}\n Model:{self.__model}\n Culoare:{self.__culoare}\n Viteza maxima:{self.__viteza_maxima}\n'
                f' Viteza actuala:{self.__viteza_actuala}\n Inmatriculata:{self.__inmatriculata}')


# înmatriculare() - va schimba atributul înmatriculată în True
# __inmatriculata = False

    def inmatriculare(self):
        self.__inmatriculata = True


 # __culori_dispponibile = {'rosu', 'albastru', 'negru', 'alb', 'verde'}

    def vopseste(self, culoare):
        if culoare in self.__culori_dispponibile :
            self.__culoare = culoare
        else:
            raise Exception ("Nu avem in paleta de culori")


# accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e negativă-eroare, dacă viteza e mai mare decât
# viteza_max - masina va accelera până la viteza maximă
    def accelereaza(self,viteza):
        if viteza < 0:
            raise Exception('Viteza nu poate fi mai mica de 0')
        elif viteza > self.__viteza_maxima:
            self.viteza_actuala = self.__viteza_maxima
        else:
            self.viteza_actuala = viteza

# franeaza() - mașina se va opri și va avea viteza 0
    def franeaza(self):
        self.__viteza_actuala = 0


m = Masina('accelereaza', 150)
# m.viteza_maxima = 180
# print(m.viteza_maxima)
# del m.viteza_maxima
# # print(m.viteza_maxima)
# print(m)
# m.inmatriculare()
m.vopseste("alb")
print(m)
