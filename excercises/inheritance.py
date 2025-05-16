# Inheritance lets a class (child) inherit attributes and methods from another class (parent). Composiotion over inheritance.
class Animal:
    # def __init__(self):
    #     print("I'm an animal!")
    def breathe(self):
        print("Breathe in, breathe out.")

    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

# TASK: Complete the class Cat so it inherits from Animal and overrides the speak() method.

class Cat:
    pass  # <-- Inherit from Animal and override speak()

if __name__ == "__main__":
    husky = Dog()
    husky.speak()
    husky.breathe()