import math
import json

with open("Puncte.json", "r") as f:
    puncte = json.load(f)

print(puncte["A"])
print(puncte["B"])

dista = math.dist([puncte["A"]["X"], puncte["A"]["Y"]], [puncte["B"]["X"], puncte["B"]["Y"]])

print(dista)

puncte["distanta"] = dista

with open("Puncte.json", "w") as f:
    json.dump(puncte, f)



"""
{
  "A" : { "X": 0 , "Y" : 0 },
  "B" : { "X" : 1, "Y" : 1 }
}
"""