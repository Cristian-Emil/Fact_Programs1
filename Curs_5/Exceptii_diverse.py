try:
    lista = [1, 2, 3, 4]
    lista[6]
except IndexError as exc:
    print(exc)
# raise IndexError(f"Limita este")
print(f"Limita listei este de {lista[3]} elemente")
print("Limita listei este de",{lista[3]})
print()
#-----------------------------------------------------------------------------------------------------------------------
""" Ridicam o exceptie in mod intentionat """
try:
    lista = [1, 2, 3, 4]
    lista[3]
except IndexError as exc:
    print(exc)
    raise IndexError(f"Limita listei este de {lista[3]} elemente")
print("Cand intalneste exceptia ne transmite mesajule \n "
      "1) IndexError: list index out of range \n "
      f"2) IndexError: Limita listei este de {lista[3]} elemente")