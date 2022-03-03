class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        self.length = l

    def get_area(self):
        return self.length**2

S1=Square(2)
print(S1.get_area())