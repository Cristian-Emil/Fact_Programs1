print("Tema 15 - S2")
"""
15. x, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
 """
# Varianta 1
x12 , y12 , z12 = (input ("x12 = "), input ("y12 = ") , input ("z12 = "))
# x12, y12, z12 = map(int, input().split())
Suma_unghiuri = int(x12)+int(y12)+int(z12)
print(Suma_unghiuri)
if int(x12>0) and int(y12>0) and int(z12>0) :
    if Suma_unghiuri < 180 :
        print ("Triunghiul nu exista - nu se inchide")
    elif Suma_unghiuri > 180 :
        print ("Nu exista un triunghi cu suma unghiurilor > 180 ")
    else:
        print("Avem un triunghi echilateral" if (x12 == y12 == z12) else "Este un triunghi oarecare")
else:
    print ("Nu este triunghi")
print(" ")

# varianta 2
print("varianta 2")
Suma_unghiuri = int(x12)+int(y12)+int(z12)
if Suma_unghiuri == 180 and int(x12>=y12>=z12>0):
    print ("Triunghiul exista oarecare")
elif ( x12 == 90 and y12 == 90 ) or ( x12 == 90 and  z12 == 90 ) or ( y12 == 90 and z12 == 90):
    print ("Nu exista triunghi")
elif x12 == y12 == z12 and Suma_unghiuri == 180 :
    print("Este un triunghi echilateral")
elif x12 == y12 or x12 == z12 or y12 == z12:
    print("Este un triunghi isoscel")
elif x12 == 90 or y12 == 90 or z12 == 90 :
    print("Este un triunghi dreptunghic")
elif Suma_unghiuri < 180 :
    print ("Nu exista triunghi ")
else:
    print("Nu este triunghi")
print(" ")

# ----------------------------------------------------------------------------------------------------------------------
"""
Varianta cu raspunsuri bune dar si dublate
"""
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

suma_unghiuri = x + y + z

# Verificarea ca este triunghi.
# Trebuie ca toate sa fie fiecare in parte mai mare ca 0, nu conteaza care e ordinea intre ele.
# Nu putem folosi scurtatura x >= y >= z > 0 pentru ca inpune o ordine intre unghiuri.
if suma_unghiuri == 180 and x > 0 and y > 0 and z > 0:
    print('Este triunghi.')

    # acum verificam cazurile particulare in functie de masura maxima a unghiului
    if x > 90 or y > 90 or z > 90:
        print('Triunghiul este obtuzunghic.')
    elif x == 90 or y == 90 or z == 90:
        print('Triunghiul este dreptunghic.')
    else:
        print('Triunghiul este ascutitunghic.')

    # acum verificam cazurile particulare in functie de relatia dinre unghiuri
    if x == y == z:
        print('Triunghiul este echilateral.')
    elif x == y or y == z or x == z:
        print('Triunghiul este isoscel.')
    else:
        print('Triunghiul este oarecare.')
else:
    print('Nu este triunghi')