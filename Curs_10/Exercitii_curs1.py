""" Implementam functia STER sau RANGE din FOR"""

def my_range(x, y = None, z = None):
    if y is None and z is None :
        n = 0
        while n < x:
            yield n
            n += 1
    elif z is None:
        n = x
        while n < y:
            yield n
            n += 1
    else:
        n = x
        while n < y:
            yield n
            n += z

for i in range(10):
     print (i)

#  ---------------------------------------------------------------------------------------------------------------------

# for i in range(1, 10, 2):
#     print (i)

"""TO DO sa se faca si pentru cifrele negative si sa fie mai elegant"""