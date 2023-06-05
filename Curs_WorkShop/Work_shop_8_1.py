from abc import ABC, abstractmethod

class TestCase(ABC):

    @abstractmethod
    def setup(self):
        raise NotImplemented

    @abstractmethod
    def execute(self):
        raise NotImplemented

    @abstractmethod
    def quit(self):
        raise NotImplemented



class TestLogin(TestCase):

    def setup(self):
        print("Introdu datele")

    def execute(self):
        print("Executa")

    def quit(self):
        print("Foarte bine")


class TestLogout(TestCase):

    def setup(self):
        print("Gata cu datele")

    def execute(self):
        print("Am terminat de executat")

    def quit(self):
        print("La revedere")


test1 = TestLogin()
test2 = TestLogout()

print(" ")
test1.setup()
test1.execute()
test1.quit()

print(" ")
test2.setup()
test2.execute()
test2.quit()