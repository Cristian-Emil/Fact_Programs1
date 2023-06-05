import csv

with open("elevi.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=" ")

    print("header: ")
    header = next(csv_reader)
    print(header)

    print("lines: ")
    for line in csv_reader:
        print(line)


import pandas as pd
content = pd.read_csv("elevi.csv")
lines = pd.DataFrame(content)
print(content)
print(lines.values)                     # ne tipareste sub forma de matrice
print(lines.columns.values)             # ne tipareste numele

