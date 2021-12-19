import math


class Rectangle(object):
    """Describe a rectangle shape"""
    width = 0.0
    height = 0.0

    def __init__(self, width=0.0, height=0.0):
        self.width, self.height = width, height

    def print_area(self):
        print('Rectangle area:', "{:.3f}".format(self.width * self.height))
pass


class Circle(object):
    """Describe a circle shape"""
    pi = math.pi
    radius = 0.0

    def __init__(self, radius=0.0):
        self.radius = radius

    def print_area(self):
        print('Circle area:', "{:.3f}".format(self.pi * math.pow(self.radius, 2)))
pass


class Triangle(object):
    """Describe a triangle shape"""
    width = 0.0
    height = 0.0

    def __init__(self, width=0.0, height=0.0):
        self.width, self.height = width, height

    def print_area(self):
        print('Triangle area:', "{:.3f}".format((self.width * self.height) / 2))
pass

rectangle = Rectangle(3.45, 8.15)
rectangle.print_area()

triangle = Triangle(4.55, 6.80)
triangle.print_area()

circle = Circle(1.3)
circle.print_area()