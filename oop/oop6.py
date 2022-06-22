from abc import ABC, abstractmethod


# interface
class JSONify(ABC):
    @abstractmethod
    def to_json(self):
        pass

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calc_area(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius
    
    def calc_area(self):
        return 3.14 * (self.radius ** 2)

    def to_json(self):
        return f"{{\"circle\" : {str(self.calc_area())}}}"


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calc_area(self):
        return self.side * self.side

# g = GraphicShape()

c = Circle(10)
print(c.calc_area())
print(c.to_json())

s = Square(12)
print(s.calc_area())