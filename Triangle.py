from Shape import Shape

class Triangle(Shape):
    def __init__(self, name, a, b, c, h_to_b):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c
        self.h_to_b = h_to_b

    # override
    def get_area(self):
        return self.h_to_b * self.b / 2.0

    def print_area(self):
        print(f' area = {self.get_area()}')

    def __str__(self):
        return f'[Triangle] a: {self.a} b: {self.b} '+\
            f'c: {self.c} area-{self.get_area()} | ' + super().__str__()
