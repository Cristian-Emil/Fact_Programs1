"""
Mostenire
"""
class Bucatar_Chef():
    def prepara_1(self):
        print("Diverse verdeturi de 2 stele Micheline")
    def prepara_2(self):
        print("Diverse carne de 2 stele Micheline")


# aici definim clasa copil si mostenim clasa CHEF prin inserarea intre paranteze a acesteia
class Bucatar1(Bucatar_Chef):
    def prepara_3(self):
        print("Prepare verdeturi de 1 stea Michelina")

class Bucatar2(Bucatar_Chef):
    def prepara_4(self):
        print("Prepare carne de 1 stea Michelina")


print(" ")
print('*' * 10 + ' bucatar1 ' + '*' * 10)
bucatar = Bucatar_Chef()
bucatar.prepara_1()
bucatar.prepara_2()

print(" ")
print('*' * 10 + ' bucatar 2 ' + '*' * 10)
bucatar1 = Bucatar1()
bucatar1.prepara_1()
bucatar1.prepara_2()
bucatar1.prepara_3()

print(" ")
print('*' * 10 + ' bucatar 3 ' + '*' * 10)
bucatar2 = Bucatar2()
bucatar2.prepara_1()
bucatar2.prepara_2()
bucatar2.prepara_4()
