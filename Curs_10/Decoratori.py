import time
from functools import wraps


def timp_exe(funct):
    @wraps(funct)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = funct(args, kwargs)
        t2 = time.time() - t1
        print(f"Functia {funct.__name__} s-a executat de la {t1} in {t2} secunde")
        return result

    return wrapper

@timp_exe
def afisare_info(nume, varsta):
    time.sleep(1)                                       # intarzie afisarea o secunda
    print(f"Am terminat de lucrat {nume} , {varsta}")

print("Aici avem raspunsurile")
afisare_info("Ion" , 45)
print("")
afisare_info("Vasilica de la gaze" , 59)

print("")
print(afisare_info("Popica de la curent" , 37))

print("")
new_funct = timp_exe(afisare_info)
print(afisare_info("Ioniuca de la apa" , 38))