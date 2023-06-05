# Tema 1 - partea S1
print("S1- TEMA DE CASA ")
print()

# tema de casa S1 punctul 1
print(" O variabila este “UN OBIECT” care poate sa ia o anumita valoare la un anumit moment, ea este definita/asignata in"
      " acest mod.Poate sa fie cosidera ca fiind un NUME sau ETICHETA utilizata pentru a face referire la o anumita valoare"
      " sau locatie din memoria programului in care este definita.")

# tema de casa S1 punctele 2 si 3
nume1: str = "STRING"
numar2: int = 2
numar3: float = 3.14
boolean: bool = True

print()
print(type(nume1))
print(type(numar2))
print(type(numar3))
print(type(boolean))
print()

# tema S1 punctul 4
numar3 = round(numar3)
print(numar3)
print()

# tema S1 punctul 5
print(f"Acesta este un SIR " + nume1)
print(f"Acesta este un SIR {nume1}")
#print(f"Acesta este un INTREG/INTEGER " + numar2)
print(f"Acesta este un INTREG/INTEGER {numar2}")
#print(f"Acesta este un NUMAR CU VIRGULA/CU ZECIMALE" + numar3)
print(f"Acesta este un NUMAR CU VIRGULA/CU ZECIMALE {numar3}")
#print(f"Acesta este un boolean" + boolean)
print(f"Acesta este un {boolean}")
print(f"Acesta este un SIR {nume1}, Acesta este un INTREG/INTEGER {numar2} , Acesta este un NUMAR CU VIRGULA/CU ZECIMALE {numar3}, "
      f" Acesta este un {boolean}")
print()

# tema S1 punctul 6
prenume = input("Prenume = ")
nume = input ("Nume = ")
print(f"Numele complet este {prenume} {nume} ")
nume_complet = (prenume + nume)
nume_complet=len(nume_complet)
print(f"Numele complet are X = {nume_complet} caractere")
print()

# tema S1 punctul 7
lungimea: float = 39.5
latimea: float = 9.75
aria = lungimea * latimea
print (f"Aria dreptunghioului este X = {aria}" )
lungime1 =int(input("Lungime  = "))
latime1 =int(input("Latime  = "))
aria1 = lungime1 * latime1
print (f"Aria dreptunghioului este X = {aria1}" )