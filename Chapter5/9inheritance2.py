class Shape:
    def __init__(self, x, у):
        self.x = x
        self.у = у
        
    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.у = self.у + delta_y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side

    def __str__(self):
        return super().__str__() + f', side: {self.side}'