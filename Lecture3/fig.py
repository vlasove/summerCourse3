import math as m

class Figure:
    def __init__(self, c = "black", w = -1):
        self.color = c
        self.weight = w

    
class Circle(Figure):
    def __init__(self, r = -1):
        super().__init__(self)
        self.radius = r

    def perimeter(self):
        return 2*m.pi*self.radius

    def square(self):
        return m.pi*self.radius**2