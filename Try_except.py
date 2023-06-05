# """
# TRY-CATCH sau in python se numeste TRY-EXCEPTION
# """
# cuvant = "Arbore"
# numar = 10
# valoare = 0
# print(cuvant + " " + str(numar))
# print("")
#
# try:
#     print(cuvant + " " + numar)
#     valoare = 1
# except Exception as exc:
# # aici Exception este clasa la general , cea care le inglobeaza pe toate
#     print(exc)
# else:
#     print("Nu a aparut nici o eroare")
#
# print(valoare)
# print("Aici se inchide codul nostru")

# Ne anunta ca avem in linia 10 o concatenare de INT cu STR.  Deci linia 11 cu valoare= 1 a fost sarita.

# sau alte variante avem :
# cuvant = "Arbore"
# numar = 10
# valoare = 0
# dictionar ={ "a" : 10}
#
# try:
#     print(dictionar["b"])
#     print(cuvant + " " + numar)
#     valoare = 1
# except TypeError as exc1:
#     print("Eroare de tip")
# except KeyError as exc2:
#     print(f"Key-ul {exc2} este inexistent")
# except Exception as exc3:
#     print(exc3)
# else:
#     print("Nu a aparut nici o eroare")
#
# print(valoare)
# print("Aici se inchide exercitiul")
#
# # sau alte variante avem :
# cuvant = "Arbore"
# numar = 10
# valoare = 0
# dictionar ={ "a" : 10}
#
# try:
#     print(dictionar["b"])
#     print(cuvant + " " + numar)
#     valoare = 1
# except TypeError as exc1:
#     print("Eroare de tip")

#-----------------------------------------------------------------------------------------------------------------------
""" Exemple din slide-uri"""

def divide(x, y):
    try:
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally:
        print('This is always executed')            # ce este in FINALLY se executa indiferent si se afiseaza la final
print("")
print("Pentru cazul 1")
divide(3, 2)                                        # impartirea // da rezultat cu valoare fixa- numar intreg fara rest
print("")
print("Pentru cazul 2")
divide(10, 0)
