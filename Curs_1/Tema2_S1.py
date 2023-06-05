# print()
# # cautati si gasiti unde este cuvantul MERGE, pe ce pozitie se afla in fraza urmatoare
# text = "Ulciorul nu merge de multe ori la apa"
# pozitie = text.find("merge")
# print(f"Cuvantul MERGE incepe de pe pozitia Z = {pozitie}" )
# print()

# tema S1 punctul 8 si 9
# La stringul "'Coral is either the stupidest animal or the smartest rock" gasiti cuvantul the si il afisati

text = "Coral is either the stupidest animal or the smartest rock"
#sparge textul in cuvinte
cuvinte = text.split()
print(f"Spargem textul in cuvinte individuale = {cuvinte}")
cuvinte1 = text.split("the")
print(f"Elimina THE din si dintre cuvintele afisate = {cuvinte1}")
cuvinte2 = " ".join([word for word in cuvinte if word.lower() == "the"])
print(f"Afiseaza 'THE' dintre cuvintele frazei = {cuvinte2}")
print()

# pe ce pozitie apare primul "the"
pozitie = text.find("the")
print (f"Pe ce pozitie se afla primul 'the'. Incepe de pe pozitia x = {pozitie}")
print()

# pe ce pozitie de cuvant apare primul "the"
a = cuvinte.index("the")
print(a)
a = cuvinte.index("the", 4)
print(a)


#de cate ori apare "the" in text
contorizeaza = text.count("the")
print(f"De cate ori apare cuvantul 'the' in propozitia data ? Apare de y = {contorizeaza} ori")
print("Aici se termina S1 punctele 8 & 9")
print()

# # tema S1 punctul 10
# """Având stringul: 'coral is either the stupidest animal or the smartest rock':
# -	●	Folosește un assert ca să verifici dacă acest string conține doar numere
#  """
# text = "coral is either the stupidest animal or the smartest rock"
# #assert text.isnumeric()
# assert text.islower()
# print("Aici se termina S1 punctul 10")
# print()
#
#
# # tema S1 punctul 11:
# # citeste de la tastatura un string de dimensiune impara si afiseaza cuvantul din mijloc
# # propozitia intrdusa este  = "Am mers singur la piata sa fac cumparaturile zilnice"
#
# fraza = input("text = ")
# cuvinte = fraza.split()
# lungimea_frazei = len(cuvinte)
# cuvant_din_mijloc = cuvinte[lungimea_frazei //2]
# print(cuvant_din_mijloc)
# print("Aici se termina S1 punctul 11")
# print("")
#
# # pentru cuvant - cuvantul intrdusa este  = "Maria"
# cuvant = input("introdu un cuvant: ")
# print(cuvant[len(cuvant)//2])
#
#
# # tema S1 punctul 12:
# # Cu o singură linie de cod - citește un string de la tastatură - salvează fiecare cuvânt într-o variabilă - printeaza variabilele
# # textul utilizat este --- 'alabala portocala'
#
# fraza = input("text = ")
# cuvinte = fraza.split()
# print(cuvinte)
# cuvant1 = cuvinte[0]
# cuvant2 = cuvinte[1]
# print(cuvant1)
# print(cuvant2)
#
# #cuvant1, cuvant2 = input("Enter a sentence: ").split(maxsplit=1)
# print(cuvant1)
# print(cuvant2)
# print("Aici se termina S1 punctul 12")
# print("")
#
# # tema S1 punctul 13:
# # citeste un string de la tastatura
# # salveaza primul caracter intr-o variabila
# # capiatalizeaza acest caracter peste tot din mijloc
#
# string = "alabala portocala"
# x,y = string[0],string[-1]
# final_string = (x + string[1:-1]).replace (x,x.capitaliize()) +y
# print(final_string)
# print("Aici se termina S1 punctul 13")
# print("")
#
#
# #tema 13 _ S1:
# #Cu o singură linie de cod - citește un string de la tastatură - salvează fiecare cuvânt într-o variabilă - printeaza variabilele
# #textul utilizat este --- 'alabala portocala'
#
# fraza = input("introdu o fraza: ")
# x = fraza[0]
# y = fraza[-1]            # -1 la string se duce la coada
# final_fraza = x + fraza[1:-1].replace(x, x.capitalize()) + y  # face prima litera mare - cu capitalize sau upper
# print(final_fraza)
#
# # ca sa facem toate literele mari se face :
# fraza_finala = fraza.upper()
# print(fraza_finala)
#
# # ca sa facem doar prima literea mare se face :
# fraza_finala = fraza.capitalize()
# print(fraza_finala)
# print("")
#
#
# #Tema 14 _ S1
# #	citește un user de la tastatură;
# #	citește o parolă;
# #	afișează: 'Parola pt user x este ***** și are x caractere';
# #	* se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
#
# user = input("introdu userul = ")
# parola = input("introdu o parola = ")
# print(f"parola userului: {user} este: {len(parola)*'*'} si are o lungime de {len(parola)} caractere")
