from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        raise NotImplementedError


class Circle(Shape):
    def draw(self):
        print('Acesta este un cerc')


class Square(Shape):
    def draw(self):
        print('Acesta este un patrat')


class Rectangle(Shape):
    def draw(self):
        print('Acesta este un dreptunghi')


class Factory:
    __shapes = ['cerc', 'patrat', 'dreptunghi']
    __our_shapes = []

    def get_shape(self, shape_type=''):
        if shape_type not in self.__shapes:
            raise Exception('Forma nu exista')

        if shape_type == 'cerc':
            c = Circle()
            self.__our_shapes.append(c)
            return c

        if shape_type == 'patrat':
            s = Square()
            self.__our_shapes.append(s)
            return s

        r = Rectangle()
        self.__our_shapes.append(r)
        return r

    def get_shapes(self):
        return self.__our_shapes


# i = ''
# while i != 'gata':
#     i = input('Ce sa desenez? ')
#
#     if i == 'cerc':
#         c = Circle()
#         c.draw()
#     elif i == 'patrat':
#         p = Square()
#         p.draw()
#     elif i == 'dreptunghi':
#         d = Rectangle()
#         d.draw()
#     elif i == 'gata':
#         break

factory = Factory()
shape_type = input('Ce sa desenez? ')
while shape_type != 'gata':
    try:
        shape = factory.get_shape(shape_type)
        shape.draw()
    except Exception as e:
        print(e)

    shape_type = input('Ce sa desenez? ')

print(factory.get_shapes())
