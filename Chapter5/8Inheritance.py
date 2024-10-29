class Square1:
    def __init__(self, side=1, x=0, y=0):
        self.side = side
    
class Circle1:
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius

# two classes below makes a lot of double codes
class Square2:
    def __init__(self, side=1, x=0, y=0):
        self.side = side
        self.x = x
        self.y = y

class Circle2:
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius
        self.x = x
        self.y = y

# so here is inheritance comes in
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y       

class Square3(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side
    
class Circle3(Shape):
    def __init__(self, radius=1, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius
