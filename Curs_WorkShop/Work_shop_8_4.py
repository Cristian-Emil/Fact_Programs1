class Salar:
    def __init__(self, pay):
        self.__pay = pay

    def get_total_salary(self):
        return self.__pay * 12

    def det_total_salary_in_eur(self):
        return self.get_total_salary() / 4.85

class Angajat:
    def __init__(self, pay, bonus):
        self.__pay = pay
        self.__bonus = bonus

    def salariu_anual(self):
        return self.__pay.get_total_salary() + self.__bonus

    def salariu_anual_in_eur(self):
        return self.__pay.det_total_salary_in_eur() + self.__bonus / 4.85

    def __str__(self):
        return (f'{self.salariu_anual()}')

salarIonel = Salar(2000)
#asa am transmis valoarea salarIonel dintr o clasa in alta
#o data cu es am transmis si metodele clasei Salar
#in angajati am folosit procedurile clasei salar, fara aceasta atribuire clasa angajat nu cunoaste acea procedura
angajatIonel = Angajat(salarIonel, 300)
print(angajatIonel.salariu_anual())
print(angajatIonel.salariu_anual_in_eur())