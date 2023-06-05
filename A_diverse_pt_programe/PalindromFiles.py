"""
Cum stim daca un sir este palindrom?
"""

def palindrom (string):
    revers_string = string[::-1]
    if string == revers_string:
        return True
    else:
        return False

cuvant = "level"
if palindrom(cuvant):
    print(f"Este '{cuvant}' palindrom")
else:
    print(f"Cuvantul '{cuvant}' nu este palindrom")