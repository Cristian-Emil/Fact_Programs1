"""Testul contine 16 exercitii
Aici in prima partea avem exercitiile de la 1 la 8
in Tema3_S3_Part2 avem de la 9 la 16
"""
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 1 - S3")
#"""
# 1. 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ●	Afișeaz-o.
# ●	Inversează ordinea folosind slicing și suprascrie această listă.
# ●	Printează varianta actuală (inversată).
# ●	Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea.
#     Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
# ●	Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.
#"""
#
# lista = ["do" , "re" , "mi" , "fa" , "sol" , "la" , "si" , "do"]
# print (lista)
#
# print ( "varianta 1 - inversare")
# lista_inversa = lista [::-1]
# print (lista_inversa)
#
# print ( "variant 2 - inversare")
# lista_inversata = list(reversed(lista))
# print (lista_inversata)
#
# print ( "varianta 3 - inversare")
# lista.reverse()
# print (lista)
#
# print("Suprascriem lista")
# lista = lista
# print (lista)
#
# print ("Revenim la lista initiala folosind una din variantele de mai sus - alegem varianta 3 ")
# print ( "varianta 4 - revenire la lista initiala")
# lista.reverse()
# print (lista)
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 2 - S3")
# """
# 2. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ●	Afișeaz-o.
# ●	De câte ori apare ‘do’?
# """
# lista = ["do" , "re" , "mi" , "fa" , "sol" , "la" , "si" , "do"]
# print (lista)
# contorizeaza = lista.count("do")
# print(f"'do' apare in lista de {contorizeaza} ori")
# print(" ")
#
# for cuvant in lista:
#     print(cuvant)
#     if cuvant == "do":
#         print(f"Avem {cuvant} pe aceasta pozitie")
#         print("")
#     else:
#         print ("Nu avem 'do' pe aceasta pozitie")
#         print("")
#
# # print(f"Spargem lista in cuvinte individuale = {cuvant}")
#
# cuvinte = " ".join([word for word in lista if word.lower() == "do"])
# print(f"Afiseaza toti 'do' din lista = {cuvinte}")
#
# t_note= [i for i in lista if i == "do"]
# print (len(t_note))
#
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 3 - S3")
# """
# 3. Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
#    Găsește 2 variante să le unești într-o singură listă.
# """
# lista1 = [3 , 2 , 0 , 1]
# lista2 = [6 , 5 , 4]
#
# print("Varianta 1")
# lista_completa = lista1 + lista2
# print(lista_completa)
#
# print("Aranjam lista")                              # folosim denumirea de la varianat1
# lista_aranjata_crescator = sorted(lista_completa)
# print(lista_aranjata_crescator)
# lista_aranajata_descrescator = sorted(lista_completa, reverse=True)
# print (lista_aranajata_descrescator)
#
# print ("Varainta 2")
# lista1.extend(lista2)
# print(lista1)
# # In acest caz avem neajunsul ca lista1 acum este suprascrisa si nu mai avem lista1 initiala , cea cu 4 elemente
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 4 - S3")
# """
# 4.	Sortează și afișează lista generată la exercițiul anterior.
# ●	Sortează numărul 0 folosind o funcție.
# """
# lista1 = [3 , 2 , 0 , 1]
# lista2 = [6 , 5 , 4]
#
# lista_completa = lista1 + lista2
# print(lista_completa)
#
# print("Aranjam lista")                              # folosim denumirea de la varianat1
# lista_aranjata_crescator = sorted(lista_completa)
# print(lista_aranjata_crescator)
# lista_aranjata_descrescator = sorted(lista_completa, reverse=True)
# print (lista_aranjata_descrescator)
#
# # eliminam numarul 0 din lista compusa si afisam noua lista
# lista_completa.remove(0)
# print (lista_completa)
#
# #sau daca alegem lista aranjata crescator / descrescator alegem pozitia care se elimina
# del lista_aranjata_crescator[0]
# print(lista_aranjata_crescator)
# del lista_aranjata_descrescator[-1]
# print(lista_aranjata_descrescator)
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 5 - S3")
#"""
# 5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
# ●	Lista este goală.
# ●	Lista nu este goală.
#"""
# lista1 = [3 , 2 , 0 , 1]
# lista2 = [6 , 5 , 4]
#
# lista_completa = lista1 + lista2
# print(lista_completa)
# lista_aranjata_crescator = sorted(lista_completa)
# print(lista_aranjata_crescator)
# nr_elem=len(lista_completa)
# if lista_aranjata_crescator == 0:
#     print ("Lista nu are nici un element")
# else:
#     print (f"Lista are = {nr_elem} elemente")
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 6 - S3")
# """
# 6.	Folosește o funcție care să șteargă lista de la exercițiul 3 - rezolvat anterior.
# """
# lista1 = [3 , 2 , 0 , 1]
# lista2 = [6 , 5 , 4]
#
# print("Varianta 1")
# lista_completa = lista1 + lista2
# print(lista_completa)
# lista_completa.clear()
# print (lista_completa)
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 7 - S3")
# """
# 7.  Copy paste la exercițiul 5, facut anterior. Verifică încă o dată.
#     Acum ar trebui să se afișeze că lista e goală.
# """
# lista1 = [3 , 2 , 0 , 1]
# lista2 = [6 , 5 , 4]
#
# lista_completa = lista1 + lista2
# print(lista_completa)
# lista_completa.clear()
# print(lista_completa)
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 8 - S3")
# """
# 8.  Având dicționarul dict = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
#     Folosește o funcție că să afișezi Elevii (cheile)
# """
# dict_0 = {"Ana" : 8, "Gigel" : 10, "Dorel" : 5}
# print(f"Elementele din DICT sunt {dict}")
# print(" ")
#
# """
# Extindem dictionarul cu inca un  element si il redenumim DICT1
# Prima data definim un dictionar gaol in care apoi adaugam elementul / elementele doirite
# """
# print ("Varianta 1 pt DICT1")
# dict1 ={}
# dict1["Ionel"] = 6                         # adaugam elementul IONEL in DICT1
# dict1 = dict_0 | dict1                      # noul dictionar DICT1 este realizat prin unirea lui DICT cu DCIT1
# print(dict1)                                # si avem noul dictionar cu 4 elemente
#
# """
# Varianta 2 este cu dict1 sa contina deja un element si apoi saii adaugam elementele din dict_0
# """
# print ("Varianta 2 pt DICT1")
# dict1 = {"Ionel" : 6}
# dict1 = dict_0 | dict1
# print(dict1)                                # si avem noul dictionar cu 4 elemente
#
#
# print(dict1.keys())
# print(f"Ana a luat nota {dict1['Ana']}")
# print(f"Gigel a luat nota {dict1['Gigel']}")
# print(f"Dorel a luat nota {dict1['Dorel']}")
# print(f"Ionel a luat nota {dict1['Ionel']}")
# print(" ")
#
# # varianta 2
# print("Varianta 2")
# print(f"Ana a luat nota {dict1.get('Ana')}")
# print(" ")
#
# print ("varianta 3")
# for key in dict1:
#     print (key, dict1[key])
# lista_crescatoare = sorted(dict1)     # sortam numele in ordine alfabetica
# print(f"Lista in ordine alfabetica =  {lista_crescatoare} ")
# print(" ")
#
# print("Varianta - dict2 - este lista initiala din enuntul problemei")
# dict2 = dict(Ana = 5 , Gigel = 7 , Dorel = 5 )
# print(dict2)
#
# print ("varianta2")
# for key,value in dict2.items():
#     print(key, value)
#
# print ("afisam doar cheile pentru dict1 si dict2 ")
# print("dict1")
# for value in dict1.values():
#     print(value)
#
# print("dict2")
# for value in dict2.values():
#     print(value)
#
# print(" ")
# print("Moduri de afisare -  atentie la sintaxa textului de tiparit")
# print(dict2)
# print(dict2.keys())
# print("")
# #-----------------------------------------------------------------------------------------------------------------------