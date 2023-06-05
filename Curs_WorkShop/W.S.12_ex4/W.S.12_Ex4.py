""" Exercitiul 4
Se "fabrica" 26 fisiere
A.txt
B.txt
.
.
.
Y.txt
Z.txt
care sa contina liniile:

"My name is letter "x".
I am the 24th letter of the alphabet."
"""

def find_end(numar):
    if numar == 1:
        return"st"
    elif numar == 2:
        return"nd"
    elif numar == 3:
        return"rd"
    else:
        return"th"

for numar in range(ord("A"), ord("Z") + 1):
    nume_fisier = chr(numar) + ".txt"
    with open(nume_fisier, "w+") as f:
        f.write(f"My name is letter {chr(numar)}\n")
        f.write(f"I am the {numar - ord('A')+1}{find_end(numar - ord('A')+1)} letter of the alphabet \n")

print()
#---------------------------------------------------------------------------------------------------------------------