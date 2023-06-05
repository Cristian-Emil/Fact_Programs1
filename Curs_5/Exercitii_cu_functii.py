"""
Functiile se definesc cu DEF
"""

def functie():
    print("Tiparim ce defineste o functie")

"""apelarea functiei imi tipareste direct continutul din print-ul definit"""
functie()
print(" ")
"""------------------------------------------------------------------------------------------------------------------"""
"""
Functiile cu parametru
"""
def functie(parametru):
    print(f"Tiparim un parametru =>  {parametru} este parametrul")

""""apelam functiei care necesita un parametru - aici scriem = ANDREI"""
functie("ANDREI")
print(" ")
"""------------------------------------------------------------------------------------------------------------------"""
"""
Functiile cu parametru si return
"""
def functie( numar ):
    if numar >= 0:
        return (f"Numarul este natural si are valoarea {numar}")
    else:
        return ("Numarul nu este natural")

rezultat = functie(8)
print(rezultat)
print(" ")
"""------------------------------------------------------------------------------------------------------------------"""


