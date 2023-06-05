"""
Cursul 7 - saptamana 4

INHERITANCE - MOSTENIRE
"""
class Chef:
    def __init__(self, exp):
#        pass                                                    # este un constructor DEFAULT care nu ia nici o valoare
        self.experienta = exp
#        self.experienta = 5

    def fa_salata(self):
        print('salata')

    def fa_cartofi(self):
        print('cartofi')


class JapaneseChef(Chef):   # pentru ca am definit clasa Chef in clasa JAPONEZ_CHEF el o sa mosteneasca tot din CHEF
    def __init__(self, exp , nume):
        super().__init__(exp)
        self.nume = nume
        print(f"Sunt sef japonez cu numele {nume}")

    def fa_sushi(self):
        print('sushi')


class ItalianChef(Chef):    # pentru ca am definit clasa Chef in clasa ITALIAN CHEF el o sa mosteneasca tot din CHEF
    def fa_pizza(self):
        print('pizza')


print('*' * 10 + ' chef 1 ' + '*' * 10)
chef = Chef(5)
chef.fa_salata()
chef.fa_cartofi()
print(str(chef.experienta) + " ani")

print('*' * 10 + ' chef 2 ' + '*' * 10)
jchef = JapaneseChef(4, "Marcel")
jchef.fa_sushi()
jchef.fa_salata()
jchef.fa_cartofi()
print(str(chef.experienta) + " ani")

print('*' * 10 + ' chef 3 ' + '*' * 10)
ichef = ItalianChef(6)
ichef.fa_pizza()
ichef.fa_salata()
ichef.fa_cartofi()
print(str(chef.experienta) + " ani")
print(" ")
"""
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
"""
# print("Avem mai multe clase care se mostenesc una din alta")
#
# class A:
#     def f(self):
#         print("Clasa A")
#
# class B(A):                     # B mosteneste clasa A
#     def f(self):
#         print("Clasa B")
#
# class C(B):
#     def f(self):
#         print("Clasa C")
#
# class D(C):
#     pass
#
# c = C()
# c.f()
# print(" ")
"""
------------------------------------------------------------------------------------------------------------------------
"""