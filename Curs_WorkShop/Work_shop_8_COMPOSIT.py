#compozitie
class Salar:
    def __init__(self, pay):
        self.__pay = pay

    def get_total_salary(self):
        return self.__pay * 12

    #putem apela metoda unei clase in clasa respectiva
    def det_total_salary_in_eur(self):
        return self.get_total_salary() / 4.85

class Angajat:
    def __init__(self, pay, bonus):
        #am folosit valoarea unei variabile din cealalta clasa
        #Salar(pay) valoarea lui pay din clasa Salar
        self.__pay = Salar(pay)
        self.__bonus = bonus

    def salariu_anual(self):
        #am apelat o procedura din clasa Salar
        return self.__pay.get_total_salary() + self.__bonus

    def salariu_anual_in_eur(self):
        return self.__pay.det_total_salary_in_eur() + self.__bonus / 4.85

    def __str__(self):
        return (f'{self.salariu_anual()}')



angajatIonel = Angajat(2000, 500)
print(angajatIonel.salariu_anual())
print(angajatIonel)
print(angajatIonel.salariu_anual_in_eur())