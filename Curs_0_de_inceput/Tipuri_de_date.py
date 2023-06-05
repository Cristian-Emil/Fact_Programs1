# #Intreg
# cifra = 9
# print (cifra)
# print( "Pentru a putea concatena partea de text/string cu numarul intreg si apoi sa-l tiparim trebuie sa  "
#        "transformam intregul in string astfel incat sa concatenam doua valori de acelasi fel  => aici "
#        "string cu string ")
# print("Este un numar intreg" + str(cifra))
#
# print(" ")
#
# #Float
# float = 8.5
# print (float)
# print( "Pentru a putea concatena partea de text/string cu float si apoi sa-l tiparim trebuie sa transformam "
#        "float-ul in string astfel incat sa concatenam doua valori de acelasi fel  => aici string cu string ")
# print ("Este un numar cu zecimale" + str(float))
# print(" ")
#
# #String
# string = "sir de caractere"
# print("Este un - " + string)    # acesta nu necesita schimbarea de tip pt ca concatenam 2 string-uri.
# print(" ")
#
# #Boolean
# boolean = True
# print(boolean)
# print(" ")
# #-----------------------------------------------------------------------------------------------------------------------
# """ Schimbarea formei datelor cand sunt introduse de la tastatura"""
#
# nume = input("Ma numesc : ")
# print (nume)
#
# varsta = int(input("Am varsta de :"))
# print (varsta)
# print (" ")
# print (f"Numele meu este {nume } si am varsta de {varsta}")
#
# #-----------------------------------------------------------------------------------------------------------------------

sir1 = "Ana are mere, Maria are pere"
print (sir1)
print(len(sir1))
print(sir1.upper())
print(sir1.lower())
print(sir1.replace("mere" , "pere"))

# Putem contoriza un element din sirul nostru
a = sir1.count("a")
print (a)
print(f"Litera 'a' se geseste in sir de {a} ori" )
