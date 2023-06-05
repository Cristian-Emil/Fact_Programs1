# Cea mai simpla metoda de implementare Pattern Factory
class APP:
    def __init__(self, nume):
        self.nume = nume

    def create(self, componenta):
        if componenta == "login":
            return Login()
        elif componenta == "about":
            return About()
        else:
            raise NotImplementedError

class Login:
    def enter_user(self, nume_1):
        print(f"{nume_1} nu exista")

    def enter_pass(self, pass_1):
        print(f"{pass_1} nu este corecta")

    def enter_click(self):
        print("Face click")

class About:
    def data_user(self, nume_2):
        print(f"{nume_2} este adaugata")

    def gdpre(self, GDP):
        print(f"{GDP} a fost implementata")

app = APP("Vasilica")

app.create("login").enter_user("Ion")
app.create("login").enter_pass("Creanga")
app.create("login").enter_click()
app.create("about").data_user("El")
app.create("about").gdpre("GDP")
print("")

