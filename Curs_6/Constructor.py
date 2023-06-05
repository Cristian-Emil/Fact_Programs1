"""
Un constructor este o metodă special definita intr-o clasa pentru a initializa obiectele de tipul respectiv.
Constructorul are acelasi nume ca si clasa si este invocat automat atunci cand se creeaza o instanța nouă a clasei.
Un constructor este reprezentat de metoda __init__(). Aceasta metoda poate avea parametri opționali prin care
se pot transmite argumente in momentul crearii obiectului.
"""

class Individ:
    def __init__(self, nume, inaltime, aspect):
        self.nume = nume
        self.inaltime = inaltime
        self.aspect = aspect

    def afisare_date(self):
        print("Nume:", self.nume)
        print("Inaltime:", self.inaltime)
        print("Aspect:", self.aspect)

# Crearea unei instanțe a clasei Individ
pers1 = Individ("Andrei", 183, "Caucazian")

# Apelam metoda "afisare_date" pentru a afișa informațiile despre individ
pers1.afisare_date()

"""
În exemplu de mai sus, clasa INDIVID are un constructor __init__() care primește doi parametri: nume și inaltime. 
Acești parametri sunt utilizați pentru a inițializa atributele 'name' și 'age' ale obiectului. Apoi, clasa are o metodă 
'afisare_date()' care afișează informațiile despre persoană.
La crearea unei instanțe a clasei 'Individ(pers1)', se specifică argumentele pentru nume și inaltime, care sunt apoi 
utilizate în constructor pentru a inițtializa atributele respective. Apelarea metodei 'afisare_date()' o sa afișeze 
informațiile despre persoana (pers1): numele și inaltimea.
"""