# """ Definirea unei functii  - minutul 10 din inregistrare"""                                          # - FUNCTIONEAZA -
# def salve():
#     print("Salve!")
#
# salve()
# salve()
# salve()
# #---------------------------------------------------------------------------------------------------------------------
# """ Definirea unei parametru - pentru functia noastra este ca o variabila - minutul 20 din inregistrare"""
# def salve (utilizator):
#     print(f"Salut {utilizator}!")
#
# salve("Maria")
# salve("Popa")
#
# """ Definirea unei parametru multiplu """
# def salve ( prenumele , numele):
#     print(f"Salut { prenumele} {numele}!")
#
# salve("Maria" , "Popescu")
# salve("Ion" , "Popa")
# prenume = "Andrei"
# nume = "Zidarescu"
# salve(prenume , nume)
# print(" ")
#
# # sau avem varianta in care definim
# print ("Definirea doar un parametru, al doilea primeste o valoare fixa din conditiea ")
# def salve ( prenumele , numele = "Pop"):
#     if not numele == "":
#         print(f"Salut { prenumele} {numele}!")
#     else:
#         print(f"Salut {prenumele}")
#
# salve("Maria" , "Popescu")
# salve("Ion" , "Popa")
# # si cu trecere pe ramura ELSE unde numele e predefinit = POP
# print("toate ce se tiparesc pe ramura ELSE au numele de familie POP")
# salve("Vasile")
# salve("Costica")
print ("Daca definim o valoare implicita , tot ce vine dupa el trebuie sa fie cu valaore implicta ")
def salve ( prenumele , numele = "Pop" , varsta = 25):
    if not numele == "":
        print(f"Salut { prenumele} {numele} !")
    else:
        print(f"Salut {prenumele} {varsta}")
    print(f"Varsta este de {varsta} ani")

salve("Maria" , "Popescu")
salve("Ion")
salve("Mihai")


# print(" ")
#-----------------------------------------------------------------------------------------------------------------------
# """ Afisam patratul unui numar introdus """                                          # - FUNCTIONEAZA -
# def afisare_patrat(x):
#     print(f"Patratul lui {x} = {x * x} ")
#
# afisare_patrat(19)
# afisare_patrat(25)
# print(" ")
#-----------------------------------------------------------------------------------------------------------------------
# """ RETURN in cadrul unei functii, ce e dupa el nu se executa """                   # - FUNCTIONEAZA
#
# def salutare_return(prenume , nume = "Pop"):
#     if not nume == " ":
#         return (f"Salut, {prenume} {nume}")
#     else:
#         return(f"Salut, {prenume}")
#
# rezultat = salutare_return("Ion" , " " )
# print (rezultat)
#
# # sau avem varianta cu PRINT
#
# def salutare_return(prenume , nume = "Pop"):
#     if not nume == " ":
#         return (f"Salut, {prenume} {nume}")
#     else:
#         print(f"Salut, {prenume}")
#     print()
#
# rezultat = salutare_return("Mihai" , "10" )
# print (rezultat)
# print (type(rezultat))
# de la aceasta linie o sa primim None ca nu se ajunge nicaieri
#print(" ")







#-----------------------------------------------------------------------------------------------------------------------

# """ Facute individual ca sa inteleg cum functioneaza"""
#
# def functie():
#     print("Salutare")
#
# functie()
# functie()
# functie()
#
# x = 10
# text = "Buna"
# y = 12.5
# boolean = True
# print(" ")
# print(x)
# print(text)
# print(y)
# print(boolean)