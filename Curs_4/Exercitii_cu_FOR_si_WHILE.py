""" ----------------------------------------------------------------------------------------------------------------
FOR      FOR-ELSE     FOR-BREAK     FOR-CONTINUE
"""
print("FOR - simplu al unei liste")
numere1 = [1, 2, 3, 4, 5]
for nr1 in numere1:
    print(nr1)

print(" ")
print("FOR - simplu al unei iteratii functie de 'i' ")
for i in range(9):
    print(i)

print(" ")
print("FOR-ELSE - al unei liste")
numere2 = [1, 2, 3, 4, 5, 6, 7]
for nr2 in numere2:
    print(nr2)
else:
    print("Am terminat de iterat")

print(" ")
print("FOR-BREAK - al unei iteratii functie de 'i'")
for i in range(101):
    if i == 5:
        break
    print(i)

print(" ")
print("FOR-CONTINUE - al unei iteratii functie de 'i'")
for i in range(10):
    if i == 6:
        continue
    print(i)

""" ----------------------------------------------------------------------------------------------------------------
WHILE      WHILE-ELSE     WHILE-BREAK     WHILE-CONTINUE
"""