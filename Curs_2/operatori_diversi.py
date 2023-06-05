x = 3
y = 5
z = 7
print()

# operatori aritmetici
w = x + y       # adunare
print(w)

v = z - x       # scadere
print(v)

s = x * y * z   # inmultire ( se poate face inmultire multipla )
print(s)

t = s / x       # impartire
print(t)

r = z%x         # modul - restul impartirii lui s la x
print(r)

p=z**x          # ridicare la putere / exponentiaL
print(p)

z += 7          # adunare cu el insusi
print(z)

y -=5           # scadere cu el insusi
print(y)

x *=3           # inmultire cu el insusi
print(x)

s /=s           # impartire cu el insusi
print(s)

print()

# alti operatori - de comparare
x = 2
y = 4
z = 6
print()
print(x)
print(y)

print()
print(x==y)             # x egal cu y               - False
print(x!=y)             # x diferit de y            - True
print(x>y)              # x mai mare ca y           - False
print(x<y)              # x mai mic ca y            - True
print(x>=y)             # x mai mare sau egal cu y  - False
print(x<=y)             # x mai mic sau egal cu y   - True

print()
print (x<5 and x<3)         # x mai mic ca 5 si 2       - True
print (x<5 and x<2)         # x mai mic ca 5 si 2       - False
print (x<5 and y<10)        # x mai mic ca 5 si y ca 10 - True
print (x<5 and y<4)         # x mai mic ca 5 si y ca 4  - False
print()
print (x<5 or x<3)          # x mai mic ca 5 sau 3      - True
print (x<5 or x<2)          # x mai mic ca 5 sau 2      - True
print (x<1 or y<10)         # x mai mic ca 1 si y ca 10 - True
print (x<1 or y<4)          # x mai mic ca 1 si y ca 4  - False
print()
print (not(x<5 and x<3))     # x mai mic ca 5 sau 3      - False
print (not(x<5 or x<2))      # x mai mic ca 5 sau 2      - False
print (not(x<1 and y<2))     # x mai mic ca 1 si y ca 10 - True
print (not(x<1 or y<4))      # x mai mic ca 1 si y ca 4  - True

