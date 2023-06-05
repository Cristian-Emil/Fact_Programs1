# Cea mai simpla metoda de implementare Pattern Factory
class APP:
    def __init__(self, nume):
        self.ion = nume

    def login(self):
        return Login()

    def about(self):
        return About()

class Login:
    def enter_user(self, nume_1):
        print(f"{nume_1} nu exista")

    def enter_pass(self, pass_1):
        print(f"{pass_1} nu este corecta")

    def enter_click(self):
        print("Face click")

    def extra_security(self, token):
        return Security(token)

class About:
    def data_user(self, nume_2):
        print(f"{nume_2} este adaugata")

    def gdpr(self, GDP):
        print(f"{GDP} a fost implementata")


class Security:
    def __init__(self,token):
        self.token = token

    def refr_token(self):
        return RefreshToken(self.token)

    def jason_token(self):
        return JasonToken(self.token)

class RefreshToken:
    def __init__(self, token):
        self.token = token

    def implement(self):
        print(f"Refresh token {self.token}")

class JasonToken:
    def __init__(self, token):
        self.token = token

    def implement(self):
        print(f"Jason token {self.token}")


app = APP("Vasilica")

app.login().enter_user("Mihai")
app.login().extra_security("Stop")
app.login().enter_pass("1234")
app.login().enter_click()
# app.login().submit()
app.about().data_user('Niste info')
app.about().gdpr()

# app.create("login").enter_user("Ion")
# app.create("login").enter_pass("Creanga")
# app.create("login").enter_click()
# app.create("about").data_user("El")
# app.create("about").gdpre("GDP")
# print("")