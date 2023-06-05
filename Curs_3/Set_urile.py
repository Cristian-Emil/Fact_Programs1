"""
1)  Set-urile pastreaza mai multe valori unice intr-o variabila
2)  Nu sunt ordonate sau indexate
3)  Seturile sunt mutabile (le putem modifica, desi nu putem schimba valoarea unui element)
4)  Se pot doar adauga sau sterge elemente
5)  Putem folosi len() pentru a afla dimensiunea
6)  Elementele unui set trebuie sa fie imutabile (adica nu putem pune list, dict, set in set)
"""

culori = {"alb" , "rosu" , "galben"}
print (culori)
print (len(culori))
print("")

flori = {"ghiocei" , "lalele" , "crizanteme" , "zambile"}
print (flori)
print (len(flori))
print("")

flori.add("trandafir")
print (flori)
print (len(flori))
print("")

flori.remove("lalele")
print (flori)
print (len(flori))
print("")

if "crizanteme" in flori:
    print("Avem crizanteme")
else:
    print("Nu avem crizanteme")

if "margareta" in flori:
    print("Avem margarete")
else:
    print("Nu avem margarete")


