# test in clasa - cursul 2

prima_propozitie = 'Am mers la mall.'
a_doua_propozitie = 'Nu am gasit ce cautam.'
a_treia_propozitie = 'Am mers acasa.'

suma_litere = (prima_propozitie + a_doua_propozitie + a_treia_propozitie )
suma_litere = len(suma_litere)
print(f"Numarul total de caractere N = {suma_litere}")
a_patra_propozitie = input("text = ")
print(len(a_patra_propozitie) + suma_litere)
print()

# UPPER CASE in text
str = "buna ziua"
str_upper=str.upper()
print(str_upper)
print()

# LOWER CASE in text
str = "BUNA ZIUA"
str_lower=str.lower()
print(str_lower)


a=3
b=20

suma= a + b
print (f"suma = {suma}")

diferenta= a - b
print (f" diferenta {diferenta}")

produsul = a * b
print (f"produsul {produsul}")

catul = b /a
print (f" catul {catul}")

# partea intreaga a catului :
catul = b//a
print (f" catul {catul}")

print()
# modulul - returnarea restului impartirii
restul = a % b
print (f"restul {restul}")

# ridicarea la putere
putere = b ** a
print(f"putere {putere}")

# Operatori de atribuire
print(f"inainte de scadere :{a}")
a -= 4
print(f"dupa scadere :{a}")

#Operatori de comparare

# Compararea string-urilor
str_1 = "salut"
str_2 = "salut"
str_3 = "buna"
str_4 = "pa"

print(str_1 == str_2)
print(str_3 == str_4)

x = False
y = True
z = False

print ( x == y )
print ( x == z )
print()

# Operatori logici
x = 10
y = 15
z = 5

print( x>z and x<y)
print( x>z and x>y)
print()
print( x>z or x>y)
z=30
print( x>z or x>y)
print()
# si avem operatorul de negatie
print(not( x>z or x>y))

expresie = True
print( not expresie)
print()
t=10
print (x ==t and (x>z or x>y))
print()

x = 10
y = 20
z = 30
t = 10

print(x == t and (x > z or x > y))
print()

# CE FACEM CA SA FIE ADEVARATA
#schimbam pe y sa fie mai mic ca 10
y=8
print(x == t and (x > z or x > y))
print()
# schimbam and cu or
print(x == t or (x > z or x > y))

