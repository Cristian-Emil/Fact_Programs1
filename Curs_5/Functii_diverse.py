# def functie():
#     print("Text afisat la apelarea functiei definite in 'def'")
#
# # pentru a fisa ce este in functia definita se scrie:
# functie()
# functie()
# functie()
# print()
#-----------------------------------------------------------------------------------------------------------------------
""" Functia cu PARAMETRU are nevoie de date ca sa poata functiona.
Datele se introduc la apelarea functiei iar o functie poate sa aiba oricati parametri.
Parametri sunt optionali si daca avem mai multi, ei se despart dcu virgula.
Practic sunt niste variabile declarate dar neinitializate si se vor fi initializate (adica vor primi valori), la
apelarea functiei.
"""
def functie(parametru):
    print(f"Afisam : acesta este - {parametru}")

functie("parametru1")
functie("parametru2")
functie("parametru3")
print()
# ----------------------------------------------------------------------------------------------------------------------
""" Functia cu RETURN 
Se foloseste cand dorim ca functia sa ne expuna un raspuns (output)
Acest raspuns se poate salva in variabile. 
Return e optional. In general avem un singur return.
Exceptie cand folosim if else, atunci putem avea mai multe, dar oricum la rulare se va ajunge doar la un singur caz
"""
def functie(nr_natural):
    if nr_natural >= 0:
        return (f"Numarul {nr_natural} este natural")
    else:
        return (f"Numarul {nr_natural} nu este natural")

rezultat = functie(-5)

print(rezultat)