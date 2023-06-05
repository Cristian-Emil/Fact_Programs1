""" Decoratorii"""
import psutil as psutil


def logger(msg):
    def log_worning():
        print(f"Loging memory data {msg}")

        def is_debugg_mode_on():
            print(f"Debugging is active")

        is_debugg_mode_on()

    log_worning()

    def log_errors():
        print("Error ecoured")

    log_errors()


logger(72)


def get_virtual_memory():
    return psutil.virtual_memory().percent


logger(get_virtual_memory())


def print_logs_with_threshold(msg):
    treshold = 90

    def extra_logging():
        print(f"Logging meme este {msg}. It should be {treshold}")

    return extra_logging


print_logs_with_threshold(get_virtual_memory())()


# -------------------------------------------------------------
# accesam decoratoreul care este o functie ce altereaza alta functie

def text_logger(func):  # apeleaza functia FUNC
    def wrapper(a):
        print("Unit test pentru valoarea 'a' o sa fie convertit la un rezultat neasteptat.")
        func(a)
        print("testul a luat sfarsit")

    return wrapper
# a fost implementat decoratorul si facem niste teste , care sunt functii

@text_logger
def test_one(a):
    assert a in [1, 2, 3, 4, 5]

print(test_one(3))


@text_logger
def test_two(a):
    assert (a + 5) == 7

print(test_two(2))
