# A class should have only one reason to change — do one thing and do it well.
# ❌ BROKEN SRP: Class does multiple things (data + validation)
class User:
    def __init__(self, name):
        self.name = name

    def validate_email(self, email):
        return "@" in email  # Business logic + validation in one class
    
# ✅ FIXED SRP: Split responsibilities into separate classes
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class EmailValidator:
    def is_valid(self, email):
        return "@" in email
    
    
# Modify the code below so that it admits to the Single Responsibility principle
# ❌ BROKEN SRP: Class does multiple things (data + validation + I/O)
class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return f"Report: {self.data}"

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.generate())

# ✅ FIXED SRP: Split responsibilities into separate classes

class ReportSaver:
    def save_to_file(self, report, filename):
        with open(filename, "w") as f:
            f.write(report.generate())

class EmailValidator:
    def is_valid(self, email):
        return "@" in email
