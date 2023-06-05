a=10
b=20
c=30.5
d=a+b
e=b+c
f=False


print(d)
print(e)

print(type(a))
print(type(d))
print(type(e))
print(type(f))

# g=false     # o sa vedem ca ne atentiooneaza ca "false" nu este boolean definit
# print(type(g))


nume = "MARIME"
lungime = 25

print("Numele este " + nume + " si are lungime de = " + str(lungime))
print()
print(f"Numele este {nume} si are lungime de = {lungime}")

#   Elementele tiparite trebuie sa fie de acelasi tip ca sa poata sa fie concatenate.
print()
print("Numele este " + nume + " si are lungime de = " + nume)
print()
print("Numele este " + str(lungime) + " si are lungime de = " + str(lungime))
print()
print(type(nume))
print(type(lungime))
print()

#Schimbarea tipului de date
print("Exemple de moduri de a schimba tipul de date")
cifra1 = 1
cifra2= "2"
print(cifra1)
print(cifra2)
print(type(cifra1))
print(type(cifra2))

print()
# daca dorim ca sa fie ambele INT atiunci scrie pt cifra 2:
cifra2=int(cifra2)
print(cifra1)
print(cifra2)
print(type(cifra1))
print(type(cifra2))

