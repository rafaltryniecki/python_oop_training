from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# TASK: Implement the Rectangle class so it extends Shape and defines area().

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


if __name__ == "__main__":
    # Test
    r = Rectangle(4, 5)
    print(r.area())  # Should print 20