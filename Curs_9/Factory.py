from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def draw(self):
        print("Este un cerc")

class Square(Shape):
    def draw(self):
        print("Este un patrat")

class Rectangle(Shape):
    def draw(self):
        print("Este un dreptunghi")

# p = Square()
# c = Circle()
# d = Rectangle()
#
# p.draw()
# c.draw()
# d.draw()

class Factory:
    __shape = ["cerc" , "patrat" , "dreptunghi"]
    __our_shapes= []

    def get_shape(self, shape_type= " "):
        if shape_type in self.__shape:
            raise Exception ("Forma nu exista")

        if shape_type == "cerc":
            c = Circle()
            return c

        if shape_type == "patrat":
            p = Square()
            return p

        if shape_type == "dreptunghi":
            d = Rectangle()
            return d


# din cauza liniilor de mai sus codul de mai jos se modifica
# i = ""
# while i != "gata":
#     i = input("Ce se deseneaza ?")
#
#     if i == "cerc":
#         c = Circle ()
#         c.draw()
#     elif i == "patrat":
#         p = Square ()
#         p.draw()
#     elif i == "dreptunghi":
#         d = Rectangle()
#         d.draw()
#     elif i == "gata":
#         break

factory = Factory()
shape_type = " "

while shape_type != "gata":
    shape_type = input("Ce se deseneaza ?")

    try:
        shape = factory.get_shape(shape_type)
        shape.draw()
    except Exception as e:
        print(e)

    shape_type = input ("Ce sa desenez ? ")

print(factory.get_shape())

