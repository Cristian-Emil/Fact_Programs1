
rf = open("../Fisiere/Data.txt", "r")                       # astfel deschiden fisierul pt citire

try:
    data= rf.read()
    print(data)
finally:

    rf.close()

wf = open ("../Fisiere/Data.txt", "w")
try:
    wf.write("Hai sa iesim la plimbare \n")
finally:
    wf.close()

af = open ("../Fisiere/Data.txt", "a")
try:
    af.write("Salut . Ce mai faci \n"
         "Iesim undeva impreuna? \n"
         "Unde?")
finally:
    af.close()