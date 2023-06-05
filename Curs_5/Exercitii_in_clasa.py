# def nr(numar):
#     if numar >0 :
#         print (f"Este pozitiv {numar}")
#     else:
#         print (f"Este negativ {numar}")
#
#     if numar%2 == 0:
#         print (f"Numarul este par {numar}")
#     else:
#         print(f"Numarul este impar {numar}")
#
# a = int(input())
# nr(a)

#-----------------------------------------------------------------------------------------------------------------------
#
# def functie(propozitia_din_control):
# # spargem propozitia in cuvinte
#     cuvinte = propozitia_din_control.split()
#     return len(cuvinte)
# print(functie("Ana are mere"))
#
#
# def functie(propozitia_din_control):
# # spargem propozitia in cuvinte si cuvintele in litere
#     cuvinte = propozitia_din_control.split()
#     lista_goala =[]
#     for litere in cuvinte:
#         lista_goala.append(len(litere))
#     return lista_goala
# print(functie("Ana are mere frumoase"))
# print(" ")
#-----------------------------------------------------------------------------------------------------------------------
def f(x):
    dublul = 2 * x
    return dublul
print (f(10))                   # aici ii dam valoare lui f(x) sa fie egal cu 10

dublul = 15
print(dublul)
print(" ")

# alta varianta
print ("Avem noua varianta")
factor = 3
print (factor)

def f(x):
    factor = 10
    produs = factor * x         # aici avem inmultire intre factor si x care o sa ia functi f(x)
    return produs

produs = 20
print (f(10))                   # aici ii dam valoare lui f(x) sa fie egal cu 10
print(produs)


sir = [5,8]


# atribuim termenul de la indexul i unei variabile intermediare
a = sir[1]

# # suprascriem termenul de la indexul i cu termenul de la indexul j
# sir[1] = sir[2]

# # suprascriem termenul de la indexul j cu variabila intermediară
# sir[2] = a

# afișăm noul șir
print(sir)




lista = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

n = len(lista)
for i in range(n):
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print(lista)