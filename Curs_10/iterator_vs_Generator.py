def my_gen():
    n = 1
    print("Pasul 1")
    yield n

    n += 1
    print("Pasul 2")
    yield n

    n += 1
    print("Pasul 3")
    yield n

iterable = my_gen()

iterator = iter(iterable)

# while True:
#     try: current = next (iterator)
#
#     print(curent)

# vezi in curs minutul in jur de 42 cu plusa -minus 5 minute