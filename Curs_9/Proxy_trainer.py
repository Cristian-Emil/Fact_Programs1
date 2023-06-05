from abc import ABC, abstractmethod


class AbstractCar(ABC):
    @abstractmethod
    def drive(self):
        raise NotImplementedError


class Car(AbstractCar):
    def drive(self) -> None:
        print('Am condus masina')


class Driver:
    def __init__(self, age):
        self.age = age


class ProxyCar(AbstractCar):
    __driver = None

    def __init__(self, driver: Driver):
        self.__car = Car()
        self.__driver = driver

    def drive(self):
        if self.__driver.age < 18:
            print('Nu poate conduce')
        else:
            self.__car.drive()


d = Driver(15)
car = ProxyCar(d)
car.drive()
