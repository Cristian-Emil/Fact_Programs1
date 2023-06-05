"""
Variabilele au o structura
numele = valoare
si ia o singura valoare
"""
a = "ceva"
print (a[0])
# tipareste prima litera "c"

#----------------------------------------------------------------------------------------------------------------------

#   LISTE
"""
Listele de date au urmatoarele proprietati:
1)  Listele pastreaza mai multe valori intr-o singura variabila - sub forma de lista , termenii fiind separati prin virgula
2)  In Python, putem pastra diferite tipuri de date in aceeasi lista
3)  Fiecare element din lista, are index, incepand de la 0 (ca si string-ul)
4)  Lista este ordonata, cand adaugam un element nou, acesta se va pune la final
5)  Lista este mutabila, adica putem adauga, sterge sau schimba elemente din ea
6)  In lista putem pune valori duplicate
7)  len() ne va da dimensiunea listei (Cate elemente avem in lista?)
"""
lista_1= ["abc" , 34, True, "male" , "female" , 56]
print (lista_1)
print (lista_1[0])       # acesta tipareste primul termen
print (lista_1[1])
print (lista_1[2])
print (lista_1[-1])      # acesta tipareste ultimul termen indiferent de numarul de termeni din lista
print (len(lista_1))
print (f"lista_1 are {len(lista_1)} elemente ")
print(" ")

# adaugam un termen nou
lista_1.append(20)      # am extins lista cu inca un termen . Acesxta devine ultimul termen
print (lista_1)
print (lista_1[-1])     # acesta tipareste ultimul termen indiferent de numarul de termeni din lista - chiar cel adaugat nou
print(" ")

# mai adaugam inca un termen
lista_1.append("Maria")      # am extins lista cu inca un termen . Acesxta devine ultimul termen
print (lista_1)
print (lista_1[-1])     # acesta tipareste ultimul termen indiferent de numarul de termeni din lista - chiar cel adaugat nou
print (f"lista_1 are {len(lista_1)} elemente ")
print(" ")

# eliminam un termen anume din lista - termenul True
lista_1.remove("female")      # am elimina termenul FEMALE din lista - dupa nume
print (lista_1)
print (f"lista_1 are {len(lista_1)} elemente ")

#   eliminan o valoare de pe o anumite pozitie


print(" ")

# Exercitii cu liste

fructe =["pere" ,  "mere" , "alune" , "cirese"]
print(fructe)
fructe.insert(3 , "caise")      # am insearta dupa alune valoare caise
print(fructe)
print("____")


# inseram acum caise dupa alune indiferent unde sunt alunele in lista
fructe =["pere" , "alune" , "mere" , "cirese" , "alune"]
print(fructe)
index = fructe.index ("alune")
print(fructe)
fructe.insert(index+1, "caise")
print(fructe)

lista_mea = list("sirul meu de caractere")
print (lista_mea)

sirul_meu= "aeiou"
print(sirul_meu[1:4])

lista1= [12, "mere" , "masa" , 15 , 20, "suc" , "pere"]
print(lista_mea[2:5])
print(lista_mea[3:-1])




