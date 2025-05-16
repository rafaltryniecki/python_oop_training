# Clients should not be forced to depend on interfaces they do not use.
# https://www.pythontutorial.net/python-oop/python-interface-segregation-principle/ - use this example

# ❌ BROKEN ISP: Interfaces force unused methods
class Machine:
    def print(self):
        pass

    def scan(self):
        pass

class OldPrinter(Machine):
    def scan(self):
        raise NotImplementedError("No scanner available")


# ✅ FIXED ISP: Segregate interfaces so clients implement only what they need
class Printer:
    def print(self):
        pass

class Scanner:
    def scan(self):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print(self): print("Printing")
    def scan(self): print("Scanning")

class SimplePrinter(Printer):
    def print(self): print("Printing")

# Modify the code below so that it admits to Interface Segregation principle

class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class Robot(Worker):
    def eat(self):
        raise NotImplementedError()


class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self): print("Working")
    def eat(self): print("Eating")

class Robot(Workable):
    def work(self): print("Working")
 
