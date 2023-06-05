"""
Fiecare obiect are comportamentul lui dar ele pot conclucra si fac un features sa lucreze impreuna
"""
class ObservalUser:
    nume = "Observal Utilizator"

    def __init__(self):
        self._observers = []

    def __str__(self):
        return f"Eu sunt {self.name}"

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notifiy(self, *args, **kwargs)

class Observer:
    def __init__(self, observable):
        observable.register_observer(self)

    def notify(self, observable, *args, **kwargs):
        print("Got" , args, kwargs, "from", observable)

subiect = ObservalUser()
observer = Observer(subiect)
subiect.notify_observers("Maria", 12, oras = "Bucuresti")

