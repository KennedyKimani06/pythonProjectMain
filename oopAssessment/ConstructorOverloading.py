class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length  # Default to square

    def area(self):
        return self.length * self.width

square = Rectangle(5)
rectangle = Rectangle(5, 10)
print(square.area())
print(rectangle.area())
