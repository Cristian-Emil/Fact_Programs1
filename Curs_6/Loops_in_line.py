"""Cum putem utiliza LOOPS pentru a ascrie un text de mai multe ori"""

for numar1 in range(4):
    print("Asteptare", numar1)
#   Acesta o sa tipareasca de atatea ori cat indica numarul de la RANGE plus 1 , ca incepe de la ZERO

print(" ")

for numar2 in range(4):
    print("Asteptare", numar2, (numar2 + 1) * ".")
#   Acesta o sa tipareasca de atatea ori cat indica numarul de la RANGE plus 1 , ca incepe de la ZERO si cu stelutze
#   dupa el cu 1 mai mult ca nuamrul przezentar

print(" ")
for numar3 in range(4):
    print("Asteptare", numar3, numar3 * ".")
#   Acesta o sa tipareasca de atatea ori cat indica numarul de la RANGE plus 1 , ca incepe de la ZERO si cu atatea stelutze

print(" ")
succesful = True
a = int(input("a = "))
for numar4 in range(a):
    print("Asteptare", numar4)
    if succesful:
        print("Succes total")
        break
else:
    print(f"A asteptat {a} perioade si a picat")
