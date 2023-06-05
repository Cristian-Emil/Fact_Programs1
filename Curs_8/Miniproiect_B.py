"""
Minioproiect B
-------------------------------------------------------------------------------------------------------------------------
Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori disponibile (set), înmatriculată (bool)
   Culoare = gri - toate mașinile când ies din fabrică sunt gri
   Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
   Culori disponibile = alege tu 5-7 culori
   Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
   Înmatriculată = False
Constructor: model, viteza_maxima
Metode:
descrie() - se vor printa toate atributele, în afară de culori_disponibile
înmatriculare() - va schimba atributul înmatriculată în True
vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua culoare e în opțiunea de culori disponibile,
altfel afișați o eroare
accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e negativă-eroare, dacă viteza e mai mare decât
viteza_max - masina va accelera până la viteza maximă
franeaza() - mașina se va opri și va avea viteza 0
"""






"""------------------------------------------- TODO LIST ---------------------------------------------------------------"""
"""To_do List
    Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor

     Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizează_task(nume) - se va sterge din dict
afișează_todo_list() - doar cheile
afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare. 
Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
Dacă acesta răspunde nu - la revedere
Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict


"""
class Todolist:
    __todo = {}                                         # asa este protected, cu linii dupa el este  ......

#   adauga task-ul cu nume, descriere
    def adauga_task(self, nume, descriere):
        if nume in self.__todo:
            return Exception ("Este in lista")
        self.__todo[nume] = descriere

#   finalizeaza task-ul
    def finalizeaza_task(self, nume):
        if nume not in self.__todo:
            raise Exception("Nu exista in lista")
        del self.__todo[nume]

# afiseaza metoda todolist
    def afiseaza_todo_list(self):
        for i in self.__todo.keys():                         # afiseaza doar cheile
            print(i)

# genereaza metoda det-supl
    def det_supl(self, task):
        if task not in self.__todo:
            a = input("x = ")
            if a == "da":
                descriere = input("Descriere : ")
                self.__todo[task] = descriere
            else:
                print("La revedere")
        else:
            print(self.__todo[task])

    @property
    def todo(self):
        return self.__todo

    @todo.getter                                        # acest decorator poate sa primeasca parametrii prin paranteze
    def todo(self):
        return self.__todo

list1 = Todolist()
list1.adauga_task("alearga", "alearga in parc")
list1.adauga_task("merge", "alearga in parc")
list1.adauga_task("sta", "in gradina")
list1.adauga_task("mananca", "in bucatarie")
# list1.finalizeaza_task("alearga")
# list1.finalizeaza_task("mananca")
# list1.afiseaza_todo_list()
# print(list1.todo)
task = input("denumire = ")
list1.det_supl(task)
# list1.afiseaza_todo_list()

