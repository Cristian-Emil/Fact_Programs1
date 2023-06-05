"""Testul contine 5 exercitii
Aici avem execitiil de la 1 la 5
"""
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 1 - S6")
# """
# 1. Atribute: rază, culoare
#     Constructor pentru ambele atribute
#     Metode:
# ●	descrie_cerc() - va PRINTA culoarea și raza
# ●	aria() - va RETURNA aria
# ●	diametru()
# ●	circumferinta()
#
# """
# import math
#
# class Cercuri:
#     # raza = " "
#     # culaore =" "
#     def __init__(self, raza, culoare, greutate = "9"):
#         self._raza = raza
#         self._culoare = culoare
#         self._greutate = greutate
#
#     # def descr_cerc(self):
#     #     print(f"raza = {self._raza} si culoare = {self._culoare} si greutate = {self._greutate} ")
#     #
#     # def aria(self):
#     #     print(f"Aria cercului este  = { math.pi * self._raza** 2 } ")
# # facem metoda statica
#     @staticmethod
#     def definitie_cerc():
#         print(f"Cercul e rotund")
#
#
#     def def_cerc(self , custom_pi):
#         print(f"Cercul cu raza:  {self._raza}  este rotund si are valoarea lui pi {custom_pi}")
#
#
# cerc = Cercuri (10, "albastru")
# cerc.definitie_cerc()
# cerc.def_cerc(4)
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 2 - S6")
# """
# 2. Clasa Dreptunghi
#      Atribute: lungime, lățime, culoare
#      Constructor pentru toate atributele
#      Metode:
# ●	descrie()
# ●	aria()
# ●	perimetrul()
# ●	schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și
# va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().
# """
#
# class Dreptunghi:
#     def __init__(self,lungime, latime, culoare , greutate = "9"):
#         self._lungime = lungime
#         self._latime = latime
#         self._culoare = culoare
#         # self._greutate = greutate
#
#     def descr_dreptunghi(self):
#          print(f"lungime = {self._lungime} si latime = {self._latime} si culoare = {self._culoare} ")
#
#     def arie(self):
#         print(f"Aria dreptunghiului este  = { self._lungime * self._latime} ")
#
#     def perimetrul(self):
#         print(f"Perimetrul dreptunghiului este  = { 2*(self._lungime + self._latime) } ")
#
#     def culoare(self):
#         print(f"Culoare dreptunghiului este {self._culoare}")
#
#
# # rezolvare --------------------------------------------------------
#     @staticmethod
#     def definitie_dreptunghi():
#         print(f"Dreptunghiul este forma geometrica cu laturile egale 2 cate 2 si un unghi de 90 grd")
# #
#     def dimensiuni_dreptunghi(self ):
#         print(f"Dreptunghiul are lungimea de = {self._lungime} si latimea de = {self._latime}")
#
#     def arie_dreptunghi(self):
#         print(f"Aria dreptunghiului este  = { self._lungime * self._latime} ")
#
#     def perimetru_dreptunghi(self):
#         print(f"Perimetrul dreptunghiului este  = {2 * (self._lungime + self._latime)} ")
#
#     def culoare_dreptunghi(self):
#         print(f"Culoarea dreptunghiului este  = {self._culoare} ")
#
# dreptunghi = Dreptunghi( 50 , 25 , "" )                             # aici am definit dimensiunile dreptunghiului
#
# dreptunghi.definitie_dreptunghi()
# dreptunghi.dimensiuni_dreptunghi()
# dreptunghi.arie_dreptunghi()
# dreptunghi.perimetru_dreptunghi()
# dreptunghi.culoare_dreptunghi()
# print("")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 3 - S6")
# """
# 3. Clasa Angajat
#      Atribute: nume, prenume, salariu
#      Constructor pentru toate atributele
#      Metode:
# ●	descrie()
# ●	nume_complet()
# ●	salariu_lunar()
# ●	salariu_anual()
# ●	marire_salariu(procent)
# """
#
# class Angajat:
#     def __init__(self,prenume, nume, salariu , marire ):
#         self._prenume = prenume
#         self._nume = nume
#         self._salariu = salariu
#         self._marire = marire
#
#     @staticmethod
#     def angajat():
#          print(f"Angajatul are prenume, nume si un salariu.")
#
#     def descriere_angajat(self):
#          print(f"Angajatul are prenumele {self._prenume}, numele {self._nume} si are salariu lunar de {self._salariu} lei")
#
#     def nume_complet(self):
#         print(f"Numele complet este {self._prenume} {self._nume} ")
#
#     def salariul_lunar(self):
#         print(f"Salarul net lunar este  = {self._salariu} lei ")
#
#     def salariul_anual(self):
#         print(f"Salariul net anual =  {12*self._salariu} lei")
#
#     def marire_salariu(self):
#         print(f"Marierea de salariu la fiecare 6 luni este de {self._marire}")
#
# # rezolvare --------------------------------------------------------
# angajat = Angajat( "Mihai" , "Pop" , 7500 , "7%")                                          # aici am definit angajatul
#
# angajat.angajat()
# angajat.descriere_angajat()
# angajat.nume_complet()
# angajat.salariul_lunar()
# angajat.salariul_anual()
# angajat.marire_salariu()
#
# print("")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 4 - S6")
# """
# 4. Clasa Cont
#    Atribute: iban, titular_cont, sold
#    Constructor pentru toate atributele
#    Metode:
# ●	afisare_sold() - Titularul x are în contul y suma de n lei
# ●	debitare_cont(suma)
# ●	creditare_cont(suma)
#
# """
# class Cont:
#     def __init__(self, iban, titular_cont, sold , debitare_cont , creditare_cont ):
#         self._iban = iban
#         self._titular_cont = titular_cont
#         self._sold = sold
#         self._debitare_cont = debitare_cont
#         self._creditare_cont = creditare_cont
#
#     @staticmethod
#     def cont():
#          print(f"Contul are cod IBAN si este al unei persoane numita TITULAR si are soldul de X lei")
#
#     def IBAN (self):
#         print(f"IBAN-ul contului este {self._iban} ")
#
#     def nume_titular(self):
#         print(f"Numele titularului este {self._titular_cont} ")
#
#     def sold_cont(self):
#         print(f"Numitul {self._titular_cont } are in contul curent {self._sold} lei")
#
#     def debit_cont(self):
#         print(f"Contul de debit este de {10/100*self._sold} lei")
#
#     def credit_cont(self):
#         print(f"Contul de credit este de {15/100*self._sold} lei")
#
# # rezolvare --------------------------------------------------------
# cont = Cont( "RO10RCNC123400001" , "Ion Pop" , 750000 , 0.1 , 0.15)                             # aici am definit contul
#
# cont.cont()
# cont.IBAN()
# cont.nume_titular()
# cont.sold_cont()
# cont.debit_cont()
# cont.credit_cont()
# print("")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 5 - S6 -  varianta personala")
# """
# Varianta personala
#
# Clasa Factură
#      Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr,
#      nume_produs, cantitate, pret_buc
#      Constructor: toate atributele, fără serie
#      Metode:
# ●	tipareste_cantitatea(cantitate)
# ●	tipareste_prețul(pret)
# ●	tipareste_nume_produs(nume)
# Data: generează automat data de azi
# |      7       |       700       | 49000
# """
#
# from datetime import date
#
# today = date.today()
#
#
# class Factura:
#     def __init__(self, Seria_X101, numar, nume_produs, cantitate, pret_buc):
#         self._Seria = Seria_X101
#         self._numar = numar
#         self._nume_produs = nume_produs
#         self._cantitate = cantitate
#         self._pret_buc = pret_buc
#
#     @staticmethod
#     def factura():
#         print(f"Factura are serie , numar si contine date despre produse")
#
#     def numar(self):
#         print(f"Factura are numar de identificare {self._numar} ")
#
#     def nume_produs(self):
#         print(f"In factura sunt trecute numele produselor {self._nume_produs} ")
#
#     def cantitate(self):
#         print(f"In factura este trecuta cantitatea {self._cantitate}")
#
#     def pret_buc(self):
#         print(f"In factura este trecuta pretul unitar {self._pret_buc} ")
#
#
# # rezolvare --------------------------------------------------------
# factura = Factura("Seria_X101", "Nr. 235146", "Nume produs", 100, 10)  # aici am definit factura
#
# factura.factura()
# factura.numar()
# print("")
# factura.nume_produs()
# factura.cantitate()
# factura.pret_buc()
# print("Data facturii este: ", today)
#
# print("")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 5 - S6")
# """
#  Clasa Factură
#      Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr,
#      nume_produs, cantitate, pret_buc
#      Constructor: toate atributele, fără serie
#      Metode:
# ●	schimbă_cantitatea(cantitate)
# ●	schimbă_prețul(pret)
# ●	schimbă_nume_produs(nume)
# ●	generează_factura() - va printa tabelar dacă reușiți
#
# Factura seria x număr y
# Data: generează automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon |      7       |       700       | 49000
# """
#
# from datetime import date
# today = date.today()
#
# class Factura:
#     def __init__(self, Seria_X101, numar, nume_produs, cantitate, pret_buc):
#         self._seria = Seria_X101
#         self._numar = numar
#         self._nume_produs = nume_produs
#         self._cantitate = cantitate
#         self._pret_buc = pret_buc
#
#     @staticmethod
#     def factura():
#         print(f"Factura are serie , numar si contine date despre produse")
#
#     def numar(self):
#         print(f"Factura are numar de identificare - {self._numar} ")
#
#     def nume_produs(self, nume_nou):
#         print(f"In factura sunt trecute numele produsului = {nume_nou} ")
#
#     def cantitate(self, cantitate_noua):
#         print(f"In factura este trecuta cantitatea = {cantitate_noua}")
#
#     def pret_buc(self, pret_nou):
#         print(f"In factura este trecuta pretul unitar = {pret_nou} ")
#
#     def factura_completa(self, numar , cantitate, pret, total ):
#         print(f"Factura  {self._seria} , Numarul {numar}")
#         print(" Produs | Cantitate | pret/buc |  Total ")
#         total = pret*cantitate
#         print(f" Visine |    {cantitate}    |    {pret}    |  {total}")
#
# # rezolvare --------------------------------------------------------
# factura = Factura( "Seria_X101" , "Nr.235146" , "Nume produs"  , 100 , 10)                    # aici am definit factura
#
# factura.factura()
# factura.numar()
# print("")
#
# """ Pentru numele nou, cantitatea nou si pretul nou completam aici valorile"""
#
# factura.nume_produs("Visine")
# factura.cantitate(1000)
# factura.pret_buc(20)
# print(" ")
# print("Data factura : ", today)
# factura.factura_completa( "235146" , 9000, 22, " ")
#
# print("")
# # #-----------------------------------------------------------------------------------------------------------------------
