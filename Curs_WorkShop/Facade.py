class App:
    def __init__(self, name):
        self.ion = name

    def login(self):
        return Login()


    def about(self):
        return About()

class Login:
    def user(self, user):
        print(f'ai introdus user {user}')

    def password(self, password):
        print(f'ai introdus parola {password}')

    def submit(self):
        print('Click aici')

    def extra_security(self,token):
        return Security(token)

class About:
    def date_user(self, date):
        print(f'datele sunt {date}')

    def gdpr(self):
        print('Nu uita de taxe')
        return "esti gdprizat"

class Security:
    def __init__(self, token):
        self.token = token

    def refresh_token(self):
        return RefreshToken(self.token)

    def json_token(self):
        return JsonToken(self.token)

class RefreshToken:
    def __init__(self,token):
        self.token = token

    def implement(self):
        print(f'Refresh token {self.token}')

class JsonToken:
    def __init__(self, token):
        self.token = token

    def implement(self):
        print(f'Json token {self.token}')


app = App("soft1")

app.login().user("Mihai")
app.login().password('1235')
app.login().submit()
app.about().date_user('Niste info')
app.about().gdpr()

app.login().extra_security("abc12").json_token().implement()
