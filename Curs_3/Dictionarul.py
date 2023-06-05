"""
1) Dictionarele pastreaza date de tip cheie : valoare
2)  Dictionarurile sunt ordonate
3)  Dictonarurile sunt mutabile, deci valorile pot fi schimbate
4)  Cheile sunt unice, nu putem avea chei duplicate, ar crea confuzie
5)  Cheile unui dictionar trebuie sa fie imutabile (deci nu list, dict, set)
6)  Cheile sunt ca niste porecle pentru index-uri
7)  Putem folosi len() pentru a afla dimensiunea


"""

thisdict = {
    "brand" : "Hyundai",
    "model" : "I30",
    "year" : 2021 ,
    "cutie" : "manuala"
    }

print(thisdict)
print(thisdict["brand"])
print(thisdict["model"])
print(len(thisdict))

print(f"Informatii masina : \n- brand : {thisdict['brand']} \n- model : {['model']}\n- year : {thisdict['year']}\n- cutie : {thisdict['cutie']}")
del thisdict["year"]
print(thisdict)

if "brand" in thisdict:
    print(f"brandul este {thisdict['brand']}")
else:
    print ("Nu avem brand")

if "greutate" in thisdict:
    print(f"greutatea este {thisdict['greutate']}")
else:
    print ("Nu avem greutate")

# Definim elemente de tip dictionar
    elev_1 = {
        "Romana": 8,
        "Matematica": 10,
        "Fizica": 6
    }

    elev_2 = {
        "Romana": 9,
        "Matematica": 7,
        "Fizica": 9
    }

    medie_elev1 = (elev_1["Romana"] + elev_1["Matematica"] + elev_1["Fizica"]) / 3
    medie_elev2 = (elev_2["Romana"] + elev_2["Matematica"] + elev_2["Fizica"]) / 3
    print(medie_elev1)
    print(medie_elev2)


    if medie_elev1 == medie_elev2 :
        print (F"elev_1 are aceeasi medie generaL ca elev_2, MEDIE = {medie_elev1} vs {medie_elev2}" )
    else :
        print(f"mediile difera, MEDIE1 = {medie_elev1} vs  MEDIE2={medie_elev2}")