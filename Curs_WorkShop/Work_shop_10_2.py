from random import randint as rand

def loto_prono():
    for numere in range(6):
        yield rand(1,49)

nr_castigatoare= list(loto_prono())
print(f"Numere castigatoare : {nr_castigatoare}")

#TO DO": La final sa se afiseze un singur numar de noroc format din 7 cifre (int)