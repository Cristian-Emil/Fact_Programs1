iterable = [10, 4, 45, "copac, 2"]       #consideram un set
iterable = {"vali":1, "val2": 10 , 20:4}           # consideram un dictionar

iterator = iter(iterable)

while True:
    try:
        current = next(iterator)
#       operations with current value

        print(current)
    except StopIteration:
        break