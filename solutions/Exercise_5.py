# Dependency Inversion - Depend on abstractions, not on concrete implementations.

# ❌ BROKEN DIP: High-level class depends on low-level details
class FileLogger:
    def log(self, msg):
        print(f"Logging to file: {msg}")

class AuthService:
    def __init__(self):
        self.logger = FileLogger()  # Hard-coded dependency




# ✅ FIXED DIP: Depend on abstractions
class Logger:
    def log(self, msg):
        pass

class FileLogger(Logger):
    def log(self, msg):
        print(f"Logging to file: {msg}")

class AuthService:
    def __init__(self, logger: Logger): # We explicitly state the dependency and pass it as dependency
        self.logger = logger
        self.logger.log("Auth started")

# ❌ BROKEN DIP: High-level class depends directly on low-level implementations
class EmailService:
    def send(self, to, message):
        print(f"Sending Email to {to}: {message}")

class SMSService:
    def send(self, to, message):
        print(f"Sending SMS to {to}: {message}")

class NotificationSender:
    def __init__(self, method):
        self.method = method  # e.g., "email" or "sms"

    def notify(self, to, message):
        if self.method == "email":
            service = EmailService()
            service.send(to, message)
        elif self.method == "sms":
            service = SMSService()
            service.send(to, message)
        # Adding new methods requires modifying this class — violates DIP


# ✅ FIXED DIP: High-level class depends on an abstraction
# Abstraction
class MessageService:
    def send(self, to, message):
        pass

# Concrete implementations
class EmailService(MessageService):
    def send(self, to, message):
        print(f"Sending Email to {to}: {message}")

class SMSService(MessageService):
    def send(self, to, message):
        print(f"Sending SMS to {to}: {message}")
# High-level class depends on abstraction
class NotificationSender:
    def __init__(self, service: MessageService):
        self.service = service

    def notify(self, to, message):
        self.service.send(to, message)

# Usage
email_sender = NotificationSender(EmailService())
sms_sender = NotificationSender(SMSService())

email_sender.notify("alice@example.com", "Welcome!")
sms_sender.notify("+123456789", "OTP: 1234")

#Now if we want to add 3rd notification service, we can add it without modifying Notification sender

class SlackService(MessageService):
    def send(self, to, message):
        print(f"Sending Slack message to {to}: {message}")

slack_sender = NotificationSender(SlackService())
slack_sender.notify("@devteam", "Build failed!")



# Modify the code below so that it admits to Dependency inversion principle

class MySQLDatabase:
    def connect(self):
        print("Connected to MySQL")

class App:
    def __init__(self):
        self.db = MySQLDatabase()


# ✅ FIXED DIP: Depend on abstractions
class Database:
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL")

class App:
    def __init__(self, db: Database):
        self.db = db
        self.db.connect()
