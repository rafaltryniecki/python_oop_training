# Clients should not be forced to depend on interfaces they do not use.
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
