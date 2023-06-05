# facem direct o functie:

# try:
#     with open("Curs_WorkShop/Data.txt" , "r") as fisierul_meu:
#         continut = fisierul_meu.read()
#         print("Am tiparit textul")
# finally:
#     fisierul_meu.close()        # acestea inchide fisierul


with open("Data.txt") as fisierul_meu:
    continut = fisierul_meu.read()
    print(continut)


