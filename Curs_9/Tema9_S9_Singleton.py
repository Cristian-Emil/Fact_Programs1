""" Singleton
"""
class PresedinteRomania:

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

#In momentul de fata, dacă încercăm să creăm mai multe obiecte din clasa aceasta, vom putea:

a = PresedinteRomania()
b = PresedinteRomania()

print(a)
print(b)
print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')
print( " " )
# # ---------------------------------------------------------------------------------------------------------------------
#
# class PresedinteRomania:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __str__(self):
#         return "Eu sunt presedintele Romaniei"
#
#     def say_hello(self):
#         return f'Salut! {self}'
#
# a = PresedinteRomania()
# b = PresedinteRomania()
#
# print(a)
# print(b)
# print(f'ID(a) = {id(a)}')
# print(f'ID(b) = {id(b)}')
# print(f'Acelasi obiect? {a is b}')
# print( " " )
# # ----------------------------------------------------------------------------------------------------------------------
# #
# class PresedinteRomania:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __init__(self):
#         # Constructorul nu mai este utilizat pentru inițializarea obiectului,
#         # deoarece instanța este creata în metoda __new__
#
#         # Se poate adauga aici orice inițializare specifica doriti
#         pass
#
#     def __str__(self):
#         return "Eu sunt presedintele Romaniei"
#
#     def say_hello(self):
#         return f'Salut! {self}'
#
# a = PresedinteRomania()
# b = PresedinteRomania()
#
# print(a)
# print(b)
# print(f'ID(a) = {id(a)}')
# print(f'ID(b) = {id(b)}')
# print(f'Acelasi obiect? {a is b}')
# print( " " )