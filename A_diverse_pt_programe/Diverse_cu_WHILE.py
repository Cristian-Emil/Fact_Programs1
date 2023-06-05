""" WHILE simplu """
# diferenta fata de FOR este ca la WHILE trebuie sa initializam contorul si sa-lpunem sa itereze

i = 0
while i <=4 :
    print(i)
    i = i+1                     # sau putem scrie i += 1
# daca nu se pune itertia i = i+1 o sa intre in ciclu infinit si o sa ne afiseze 0 la infinit
print()
#------------------------------------------------------------------------
""" WHILE cu ELSE """

i = 0
while i <= 5 :
    print(i)
    i += 1
else:
    print(" Am terminat de iterat")
# la final, indiferent cat o sa itereze o sa afiseze linia de text de la ELSE.
print()