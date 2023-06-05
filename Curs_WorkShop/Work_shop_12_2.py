"""
Sa se faca fisiereul student.csv cu liniile urmatoare:
id,fname,lname,age,grade
1,Maria,Popescu,31,7.5
2,Andrei,Ionescu,26,8.0
3,Adriana,Marinescu,21,7.5
4,Matei,Gheorghescu,42,8.5
5,Eusebiu,Pop,33,9.5
6,Ioana,Popa,29,9.0
"""

import csv
with open("student.csv","w+", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "f_name", "l_name", "age", "grade"])
    writer.writerow(["1", "Maria", "Popescu", "31", "7.5"])
    writer.writerow(["2", "Andrei", "Ionescu", "26", "8.0"])
    writer.writerow(["3", "Adriana", "Marinescu", "21", "7.5"])
    writer.writerow(["4", "Matei", "Gheorghescu", "42", "8.5"])
    writer.writerow(["5", "Eusebiu", "Pop", "33", "9.5"])
    writer.writerow(["6", "Ioana", "Popa", "29", "9.0"])

with open("student.csv", "r") as f:
    reader = csv.reader(f)
    print(*reader.__next__())
    print(*reader.__next__())
    print(*reader.__next__())
    print(*reader.__next__())
    print(*reader.__next__())
    print(*reader.__next__())
    print(*reader.__next__())


"""TODO , de customizat tabelul si sa arate frumos , coloane aranjate"""








