# atentie - numaratoarea incepe de la ZERO- primul element are numarul ZERO de intentare

alfabet ="abcdefgh"
print(alfabet[1:3])
# citeste pozitiile 1 si 2

propozitie =" as merge la piata "
print(propozitie[3:7])
# citeste de la pozitia 3 pana la 7, exclusiv cifra 7 si ia in calcul toate caracterele si spatiile existente

alfabet ="abcdefghijklmnoprstuvxyz"
print(alfabet[1:15:2])
# citeste pozitiile de la al 2 element din 2 in 2



#exercitii in clasa

str_sir = "vreau niste apa"
# afisam doar textul "vreau apa"
print(str_sir[0:5] + " " + str_sir[12:15])
# daca avem primul si ultimul element ca limite se poate definii direct fara limitele din paranteze
print(str_sir[:5] + " " + str_sir[12:])