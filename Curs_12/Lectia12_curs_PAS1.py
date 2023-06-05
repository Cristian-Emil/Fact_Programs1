import sqlite3

connection = sqlite3.connect("itf_base.bd")
# connection.execute("DROP TABLE studenti")
# connection.execute("CREATE TABLE studenti ("
#
#                    "nume VARCHAR(50), "
#                    "prenume VARCHAR(50), "
#                    "varsta INTEGER, "
#                    "medie DOUBLE, "
#                    "data_inregistrarii "
#                    ")")
#
#
# connection.execute("INSERT INTO studenti( nume, prenume, varsta, medie, data_inregistrarii) VALUES "
#                    "(\"Nicolae\", \"Pepe\", 23, 8.29, \"2021-09-10\"), "
#                    "(\"Vasile\", \"Ion\", 30, 7.95, \"2021-06-12\"), "
#                    "(\"Ion\", \"Ion\", 32, 9.05, \"2021-03-15\")")

connection.commit()

cursor = connection.cursor()
cursor.execute("SELECT * FROM studenti")

studenti = cursor.fetchall()
print(studenti)

cursor.close()

# connection.execute("INSERT INTO studenti( nume, prenume, varsta, data_inregistrarii) VALUES "
#                    "(\"Badia\", \"Patru\", 23, \"2023-04-11\")")
# Am introdus un alt elev dar care nu are medie. El apare in baza de date fara nota

# connection.commit()                   # se inchide conexiune dupa ce a fost folosita
#
# connection.execute("UPDATE studenti SET medie=8 WHERE nume=\"Badea\" and prenume = \"Patru\" ")
# connection.commit()
#
# # Am facut up-date ca sa-i punem nota si lui Badea lucian
#
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM studenti")
#
# studenti = cursor.fetchall()
# print(studenti)
#
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM studenti")
#
# student1 = cursor.fetchone()
# print(student1)
#
# student2 = cursor.fetchone()
# print(student2)
#
# student3 = cursor.fetchone()
# print(student3)
#
# student4 = cursor.fetchone()
# print(student4)
#
# connection.execute("ALTER TABLE studenti ADD COLUMN id INTEGER PRIMARY KEY AUTOINCREMENET")

# connection.close()