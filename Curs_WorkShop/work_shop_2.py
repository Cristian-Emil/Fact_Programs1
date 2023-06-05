"""
Artificii pentru un text

string  = a  l  a  b  a  l  a

"""

"""Tema 8 & 9 _ S1
Având stringul: 'Coral is either the stupidest animal or the smartest rock':
-	afișează de câte ori apare cuvântul 'the'
 """
text = "Coral is either the stupidest animal or the smartest rock"
cuvinte = text.split()
print(f"Contine cuvintele sparte in bucati")
cuvant =text.split("the")
print(f"Eliminare THE din text = {cuvant}")
print (len(cuvant)-1)

print(text.count("the"))
print(text.count(" the "))
print (text.find("the"))

"""Tema 10 _ S1
Având stringul: 'coral is either the stupidest animal or the smartest rock':
-	●	Folosește un assert ca să verifici dacă acest string conține doar numere
 """
text = "coral is either the stupidest animal or the smartest rock"
# assert text.isnumeric()
assert text.islower()
print(" ")


"""Tema 11 _ S1
-	citește de la tastatură un string de dimensiune impară ( cuvant sau propozitie );
-	afișează caracterul din mijloc.
 """
cuvant = input("introdu un cuvant: ")
print(cuvant[len(cuvant)//2])
print(" ")

"""tema 12 _ S1:
Cu o singură linie de cod - citește un string de la tastatură - salvează fiecare cuvânt într-o variabilă - printeaza variabilele
textul utilizat este --- 'alabala portocala'
"""
a,b = input("introdu o propozitie :  ").split()
print (a,b)
print(f"{a} {b}")
print(" ")

"""tema 13 _ S1:
Cu o singură linie de cod - citește un string de la tastatură - salvează fiecare cuvânt într-o variabilă - printeaza variabilele
textul utilizat este --- 'alabala portocala'
"""
fraza = input("introdu o fraza: ")
x = fraza[0]
y = fraza[-1]            # -1 la string se duce la coada
final_fraza = x + fraza[1:-1].replace(x, x.capitalize()) + y  # face prima litera mare - cu capitalize sau upper
print(final_fraza)

# ca sa facem toate literele mari se face :
fraza_finala = fraza.upper()
print(fraza_finala)

# ca sa facem doar prima literea mare se face :
fraza_finala = fraza.capitalize()
print(fraza_finala)


"""Tema 14 _ S1
-	citește un user de la tastatură;
-	citește o parolă;
-	afișează: 'Parola pt user x este ***** și are x caractere';
-	***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
 """

user = input("introdu userul = ")
parola = input("introdu o parola = ")
print(f"parola userului: {user} este: {len(parola)*'*'} si are o lungime de {len(parola)} caractere")

