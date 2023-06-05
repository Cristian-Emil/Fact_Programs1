""" FISIERE CSV sunt fisiere EXCEL dar mai simple"""
import csv

with open ("../Curs_11/elevi.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    print("header : ")
    header = next(csv_reader)
    print(header)

    print("lines : ")

    for line in csv_reader:
# urmatoarea linie ne afiseaza toata linia di fisier
        print(line)
        print()

# aici ne afiseaza element cu element pe fiecare linie
        print(line[1])
        print(line[2])
        print(line[3])


""" line , cand sparge CSV-ul o sa faca pentru fiecare rand un LIST"""