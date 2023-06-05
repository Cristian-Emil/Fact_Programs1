# """
# Exercitiul 1 & 2
# Se poate pune inainte de WITH sau dupa acesta,
#     a = ["Python" , "Java", "Javascript" , "C/C++", "PHP" , "Node.js"]
# functie de tipul de variabila care este utilizata:
# - globala (inainte de WITH)
# - locala (in cadrul comenzii WITH)
# """
#
# # a = ["Python ", "Java ", "Javascript", "C/C++", "PHP", "Node.js"]
# with open("Hello_Colegi.txt", "w+") as f:
#     a = ["Python ", "Java ", "Javascript", "C/C++", "PHP", "Node.js"]
#     f.write("Python \nJava \nJavascript \nC/C++ \nPHP \nNode.js \n\n")
#     # f.write("\n")                    # variantea 2 - se aplica cand de sterge al doilea \n din linia de mai sus
#     f.writelines(linie + "\n" for linie in a)
#     f.seek(0)
#     print(f.read())
# # with open("Hello_Colegi.txt", "r") as f:
# #     print(f.read())

# --------------------------------------------------------------------------------------------------------------
""" Exercitiul 3"""
with open("Hello_Colegi.txt", "w+") as f:
    a = ["Python ", "Java ", "Javascript", "C/C++", "PHP", "Node.js"]
    f.write("Python \nJava \nJavascript \nC/C++ \nPHP \nNode.js \n\n")
    f.writelines(linie + "\n" for linie in a)
    odd_line = [linie.strip() for index, linie in enumerate(a) if index % 2 == 0]
    f.seek(0)
    print(odd_line)
print()
#--------------------------------------------------------------------------------------------------------------
