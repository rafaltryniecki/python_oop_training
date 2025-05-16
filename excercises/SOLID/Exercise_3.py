# Objects of a superclass should be replaceable with instances of its subclasses without breaking the program.

# ❌ BROKEN LSP: Subclasses change expected behavior of parent
class Bird:
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("I can't fly!")



# ✅ FIXED LSP: Subclasses behave consistently with the parent
class Bird:
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        print("Flying")

class Ostrich(Bird):
    def move(self):
        print("Running")


# Modify the code below so that it admits to the Liskov's principle

# ❌ BROKEN LSP: Subclasses change expected behavior of parent

class Vehicle:
    def start_engine(self):
        pass

class Bicycle(Vehicle):
    def start_engine(self):
        raise NotImplementedError("Bicycles don’t have engines!")
    