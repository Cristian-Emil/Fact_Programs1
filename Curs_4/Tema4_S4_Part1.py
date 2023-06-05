"""Testul contine 15 exercitii
Aici in prima partea avem exercitiile de la 1 la 8
in Tema4_S4_Part2 avem de la 9 la 15
"""
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 1 - S4")
# """
# 1. Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ●	‘Mașina mea preferată este x’.
# ●	Fă același lucru cu un for each = for obiect.
# ●	Fă același lucru cu un while.
# """
#
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# print("Varianta cu FOR ")
# for i in range(0, len(cars)) :
#     print(f"Masina mea preferata este {cars[i]}")
# print(" ")
#
# print("Varianta cu FOR EACH/OBIECT ")
# for obiect in cars:
#     print(f"Masina mea preferata este {obiect}")
# print(" ")
#
# print("Varianta cu WHILE ")
# i = 0
# while i<len(cars):
#     print(cars[i])
#     i +=1
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# print("Tema 2 - S4")
# """
# 2. Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# Folosește un for else
# În for
# -	Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
# În else:
# -	  Printează lista.
#
# """
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# for i,j in enumerate(cars):
#     print(i)
#     print(j)
#     if i !=0 and i != len(cars)-1:
#         j.upper()
#         cars1 = j.upper()
#         cars[i] = j.upper()
#         print(cars1)
#
# else:
#     print(cars)
# # varianta 2
# cars = ['audi', 'volvo', 'bmw', 'mercedes', 'opel' , 'dacia', 'ford']
# cars1 = []
#
# for i,j in enumerate(cars):
#     if i != 0 and i != len(cars) -1:
#         cars[i] = j.upper()
#     cars1.append(cars[i])
# else:
#     print(cars1)
# print(" ")
# #-------------------------------------------------------------------------------------------------------------------
# print("Tema 3 - S4")
# """
# 3. Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Iterează prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
#    Printează ‘am găsit mașina dorită de dvs’
#    Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
#    Printează ‘Am găsit mașina X. Mai căutam
# """
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in cars:
#     if i == "Mercedes":
#         print(f"Am gasit masina dorita {cars}")
#         break
#     else:
#         print ("Am gasit masina dorita x, mai cautam")
# print(" ")
# # -------------------------------------------------------------------------------------------------------------------
# print("Tema 4 - S4")
# """
# 4. Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
# -	Dacă mașina e Trabant sau Lăstun:
#     Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# -	Printează S-ar putea să vă placă mașina x.
#
# """
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in cars:
#     if i == "Trabant" or i == "Lăstun":
#         continue
#     print(i)
# print(" ")
# # -------------------------------------------------------------------------------------------------------------------
# print("Tema 5 - S4")
# """
# 5. Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
# -	Dacă mașina e Trabant sau Lăstun:
#     Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# -	Printează S-ar putea să vă placă mașina x.
#
# """
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for i in cars :
#     if i == "Trabant" or i == "Lăstun":
#         masini_vechi.append(i)
#         cars.remove(i)
#         cars.append("Tesla")
# print(masini_vechi)
# print(cars)
# print(" ")
# # -------------------------------------------------------------------------------------------------------------------
# print("Tema 6 - S4")
# """
# 6. Având lista:
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# Având dictionarul cu valori :
## """
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# for k,v in pret_masini.items():
#     print(k)
#     print(v)
#     if v <= 15000:
#         print(f"Pentru un buget de sub 15.000 avem masinile {k}")
#     else:
#         print(f"Aceste masini {k} nu se incadreaza la sub 15000")
#
# # print(" ")
# # -------------------------------------------------------------------------------------------------------------------
# print("Tema 7 - S4")
# """
# 7. Având lista:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ●	Iterează prin ea.
# ●	Afișează de câte ori apare 3 (nu ai voie să folosești count).
# """
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# print (numere)
# for i in numere:
#     print(i)
# print(" ")
#
# j = 0           # este contorul pt iterartii
# a = 3           # este numarul cautat
# for n in numere:
#     if n == a:
#         j += 1
#         # print(n)
#         # print (f"Sau putem contoriza de cate ori apare numarul {a}")
#         print(f"Numarul {a} apare de {j} ori")
# print(" ")
# # -------------------------------------------------------------------------------------------------------------------
print("Tema 8 - S4")
"""
7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
●	Iterează prin ea.
●	Calculează și afișează suma numerelor (nu ai voie să folosești sum)
"""

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

print (numere)
for i in numere:
    print(i)
print(" ")
j = 0
totalul =0
for n in numere:
     totalul += n
     print(totalul)
print(" ")


numere = [5,7,3,9,3,3,1,0,-4,3]
suma = 0
for i in range(len(numere)):
    if i <= len(numere):
        suma = suma + numere[i]
print(f'Suma este: ',suma)

# # -------------------------------------------------------------------------------------------------------------------
