"""Testul contine 16 exercitii
Aici in a doua partea avem exercitiile de la 9 la 16
in Tema3_S3_Part1 avem de la 1 la 8
"""
# #-------------------------------------------------------------------------------------------------------
# print("Tema 9 - S3")
# """
# 9.  Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
#
# ATENTIE - elementele unui dictioionar sunt
# dictionar = {"cheie1": "valoare1", "cheie2": "valoare2", "cheie3": "valoare3"}
# """
# dict = {"Ana":8 , "Gigel":10 , "Dorel":5}
# print(dict)
#
# i=0
# for i in dict:
#     print(f"{i} a luat {dict[i]}")
# print("")
# for i in dict.keys():
#     print(f"Numele elevilor sunt = {i}")
# print("")
# for i in dict.values():
#     print(f"Notelee elevilor sunt = {i}")
# print("")
# #-------------------------------------------------------------------------------------------------------
# print("Tema 10 - S3")
# """
# 10. Dorel a făcut contestație și a primit 6
# ●	Modifică nota lui Dorel în 6
# ●	Printează nota după modificare
# """
# dict1 = {"Ana":8 , "Gigel":10 , "Dorel":5}
# print(dict1)
# print("")
# dict1["Dorel"]=6
# print(dict1)
# print("")
# #-------------------------------------------------------------------------------------------------------
# print("Tema 11 - S3")
# """
# 11. Gigel se transferă din clasă
# ●	Căuta o funcție care să îl șteargă
# ●	Vine un coleg nou. Adaugă Ionică, cu nota 9
# ●	Printează noii elevi
# """
#
# dict_0 = {'Ana':8 , 'Gigel':10 , 'Dorel':5 }
# dict_0.pop("Gigel")
# print (dict_0)
#
# dict_0 ["Ionica"] = 9
# print (dict_0)
# #-------------------------------------------------------------------------------------------------------
# print("Tema 12 - S3")
# """
# 12. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
# ●	Declară o Listă cu 5 jucători
# ●	Schimbari_efectuate = te joci tu cu valori diferite
# ●	Schimbari_max = 3
# """
#
# jucatori = [ "jucator1" , "jucator2" , "jucator3" , "jucator4" , "jucator5" ]
# schimb_max = 3
# schimb_efect = 0
# while schimb_efect < schimb_max:
#     jucator_in = input("intra = ").lower()
#     jucator_out = input("iese = ").lower()
#     if jucator_out in jucatori:
#         jucatori.remove(jucator_out)
#         jucatori.append(jucator_in)
#         schimb_efect +=1
#         print(f"A intrat {jucator_in} si a iesit {jucator_out} mai avem {schimb_max - schimb_efect}")
#     else:
#         print (f"Jucatorul nu este in teren, mai ai {schimb_max - schimb_efect} schimburi ")
#
# print (" Meciul a luat sfarsit ")
# #-------------------------------------------------------------------------------------------------------
# print("Tema 13 - S3")
# """
# 13. Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# ●	Adaugă în zilele_sapt ‘luni’
# ●	Afișează zile_sapt
# """
#
# zile_sapt = {"luni" , "marți" , "miercuri" , "joi" , "vineri" , "sâmbăta" , "duminică" }
# weekend = {"sâmbăta" , "duminică" }
# print(zile_sapt)
# print(" ")
# zile_sapt.add ("luni")      # la set nu se pot dubla valorile
# print(zile_sapt)
# print("La set nu se pot dubla valorile , acestea sunt unice. Poti sea fie inteserate de n ori, se afiseaza o singura data")
# print(" ")
# zile_sapt.add("Maria")
# print(zile_sapt)
# print(" ")
# #-------------------------------------------------------------------------------------------------------
# print("Tema 14 - S3")
# """
# 14. Folosește un if și verifică dacă:
# ●	Weekend este un subset al zilelor din săptămânii.
# ●	Weekend nu este un subset al zilelor din săptămânii.
# """
# zile_sapt = {"luni" , "marți" , "miercuri" , "joi" , "vineri" , "sâmbăta" , "duminică" }
# weekend = {"sâmbăta" , "duminică" , "ioana"}
#
# if weekend.issubset(zile_sapt) in zile_sapt:
#     print("Se regaseste")
# else:
#     print("Nu se regaseste")
# print(" ")
#
# if weekend.issubset(zile_sapt):
#     print("Se regaseste")
# else:
#     print("Nu se regaseste")
# print(" ")
# #-------------------------------------------------------------------------------------------------------
# print("Tema 15 - S3")
# """
# 15. Afișează diferențele dintre aceste 2 seturi
# """
# zile_sapt = {"luni" , "marți" , "miercuri" , "joi" , "vineri" , "sâmbăta" , "duminică" , " inca o zi" }
# weekend = {"sâmbăta" , "duminică" , "ioana" }
# print(zile_sapt.difference(weekend))
#
# zile_sapt.difference_update(weekend)
# print(zile_sapt)
#
# zile_sapt.add("Doina")
# print(zile_sapt)
# print(" ")
# #-------------------------------------------------------------------------------------------------------
# print("Tema 16 - S3")
# """
# 16. Afișează intersecția elementelor din aceste 2 seturi.
# """
# zile_sapt = {"luni" , "marți" , "miercuri" , "joi" , "vineri" , "sâmbăta" , "duminică" }
# weekend = {"sâmbăta" , "duminică" }
# zile_sapt.add("Maria")
# print (zile_sapt.intersection(weekend))     # varianta 1
# print (weekend.intersection(zile_sapt))     # varianta 2
# print(" ")
# #-------------------------------------------------------------------------------------------------------
