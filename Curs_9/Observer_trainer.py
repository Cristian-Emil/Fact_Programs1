"""Cum lucreaza un OBSERVER"""

class ObservableAddUser:
    name = 'ObservableAddUser'

    def __init__(self):
        self.observers = []

    def __str__(self):
        return f"Eu sunt {self.name}"

    def reg_obs(self, observer):
        self.observers.append(observer)

    def notify_obs(self, *args, **kwargs):
        for obs in self.observers:
            obs.notify(obs, args, kwargs)


class Observer:
    def __init__(self, observable):
        observable.reg_obs(self)

    def notify(self, observable, *args, **kwargs):
        print('Got', args, kwargs, 'from', observable)


observable = ObservableAddUser()
observer = Observer(observable)
observer2 = Observer(observable)
observable.notify_obs('Maria', 12, oras='Oradea')
