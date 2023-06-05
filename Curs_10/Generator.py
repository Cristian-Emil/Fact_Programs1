""" GENERATOR - Este o functie care genereaza un iterator, unde nu avem RETURN dar avem functia YIELD"""

def my_gen():
    n = 1
    print("Pasul 1")
    yield n

    n += 1
    print("Pasul 2")
    yield n

    n += 1
    print("Pasul 3")
    yield n

for i in my_gen():
    print(i)



