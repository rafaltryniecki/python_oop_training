# Software should be open for extension, but closed for modification.

# Broken Open-Closed pricniple
# ❌ BROKEN OCP: Must modify method to add new customer types or notification types
class DiscountCalculator:
    def calculate(self, customer_type, price):
        if customer_type == "regular":
            return price
        elif customer_type == "premium":
            return price * 0.9


# ✅ FIXED OCP: Open for extension, closed for modification
class DiscountStrategy:
    def apply(self, price):
        return price

class PremiumDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.9

def calculate_discount(strategy, price):
    return strategy.apply(price)



# Modify the code below so that it admits to the Open - Closed principle
# ❌ BROKEN OCP: Must modify method to add new notification types or notification types
class Notification:
    def send(self, type, message):
        if type == "email":
            print("Sending email:", message)
        elif type == "sms":
            print("Sending SMS:", message)

