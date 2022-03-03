class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def get_area(self):
        return self.length**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    
    def get_area(self):
         return self.length * self.width

S1=Square(2)
print(S1.get_area())
R1=Rectangle(2, 3)
print(R1.get_area())
