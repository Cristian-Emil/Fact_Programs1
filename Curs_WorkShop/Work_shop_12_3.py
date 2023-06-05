"""
Sa se scrie tabelul in format JSON:
id	fname		lname		age	grade
---------------------------------------------------
1	Maria		Popescu		31	7.5
2	Andrei		Ionescu		26	8.0
3	Adriana		Marinescu	21	7.5
4	Matei		Gheorghescu	42	8.5
5	Eusebiu		Pop			33	9.5
6	Ioana		Popa		29	9.0

"""


import csv
import json

data = []

with open("student.csv", "r") as f:
    reader = csv.DictReader(f)
    for rand in reader:
        data.append(rand)

with open("student.json", "w") as f:
    json.dump(data, f, indent=4)

#-----------------------------------------------------------------

""""
instalalrea unor pachete

pip install selenium
pip freeze > requirements.txt
"""