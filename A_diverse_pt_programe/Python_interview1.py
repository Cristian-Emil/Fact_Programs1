""" Se da o lista de numere si un numar 'x'.
Sa se tipareasca toate numere din lista a caror suma sa fie egala cu numaru 'x' specificat
"""
numere = [6, 4, 7, 9, 3, 5, 12, 16]
x = 9

for i in range (len(numere)):
    for j in range(len(numere)):
        if numere[i] != numere[j]:
            if numere[i] + numere[j] == x:
                print([numere[i], numere[j]])


