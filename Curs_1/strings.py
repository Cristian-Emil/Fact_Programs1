"""Sirurile de caractere se definesc intre 3 ghilimele - docstring
Avantajul acestora este ca se pot scrie pe mai multe randuri """

" alte variante sunt ca cele din JAVA adica ghilimele duble "
' si mai avem varianta de ghilimele simple'
# Rand comentat

"Pentru afisarea in consola ne folosin de functia - print()"
"sistemul ne afiseaza si ce valaore trebuie sa completam intre paranteze"

print('Bine ai venit la "Curs de Python!"')
print("Bine ai venit la 'Curs de Python'")
print()
# Diezul - iti comenteaza toata linia si doar textul dintre ghilimele

# In Python ne folosim de operatori pentru a realiza concatenarea de texte sau elemente
print('Acesta este un text ... ' + ' ... compus din doua parti ')
print("Acest text este " + "de" + " programare si se numeste PYTHON")
print()

"Pentru a afla lungimea unui caractere ne folsoim de sintaxa -  len() "
print(len("Acestea este un " + "curs de Python , program care seamana cu Java"))
print()

# sau puterm sa numaram elementele introduse de la tastatura utilizand comanda "len"
prenume = input("Prenume = ")
nume = input ("Nume = ")
print(f"Numele complet este {prenume} {nume}")
nume_complet=len(prenume + nume)
print(f"Numele complet are x = {nume_complet} caractere")