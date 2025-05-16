# Polymorphism is a principle that says that if something is yellow, quacks like a duck and leaves a footprint like a duck
# it probably is duck.
# To be more precise, if a method/function requires a class, it cannot fail if it is given a class that inherits from that class
# Polymorphism allows objects of different classes to be treated through the same interface, typically by overriding methods.
# uv run python -m exercises.polymorphism


from typing import List

from excercises.inheritance import Animal, Dog

class Cat(Animal):
    def speak(self):
        print("Meow")

if __name__ == "__main__":
    animals:List[Animal] = [Dog(), Cat()]
    for animal in animals:
        animal.speak()  # Each class defines its own version of `speak()`
