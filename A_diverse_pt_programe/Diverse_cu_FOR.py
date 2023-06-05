""" FOR simplu """
for i in range (4):                         # acesta incepe de la ZERO si merge pana al 4 , fara 4 cu pas de 1
    print(i+2)                              # pentru ca am scris i+2 o sa afiseze de la 0+2= 2 pana la 3+2= 5

print()                                     # aici tiparim un rand liber
#------------------------------------------------------------------------
fructe =["mere" , "pere" , "prune" , "caise" , 23, 45]
for fruct in fructe:
     print({fruct})                         # acesta o sa ne afiseze numele fructului sau cifra intre acolade si cu ghilimele
     print(f"{fruct}")                      # acesta o sa ne afiseze numele fructul sau cifra
     print(f"Avem fructele {fruct}")        # acesta o sa ne afiseze "Avem fructele " urmat numele fructului sau cifra

print()
"""------------------------------------------------------------------------------------------------------------------"""
""" FOR cu ELSE """
for i in range (0,9):                     # acesta incepe de la ZERO si merge pana al 9 , fara 9 cu pas de 1
    print(i)
else:
    print("Am terminat iteratia")

print()
#-------------------------------------------------------------------------
for i in range (1,8,2):                     # acesta incepe de la UNU si merge pana al 8 , fara 8 cu pas de 2
    print(i)
else:
    print("Am terminat iteratia")

print()
#-------------------------------------------------------------------------
""" FOR cu ELIF si ELSE """