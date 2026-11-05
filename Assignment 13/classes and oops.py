# Q1 - Student Result Manager (Encapsulation)

class Student:
    def __init__(self, name, marks):
        self.name = name          # public
        self._marks = 0           # protected (by convention)
        self.__grade = "F"        # private
        self.set_marks(marks)

    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            print("Invalid marks:", marks, "- must be between 0 and 100. Not updated.")
            return
        self._marks = marks
        self.__calculate_grade()
        print("Marks updated to", marks)

    def __calculate_grade(self):
        if self._marks >= 80:
            self.__grade = "A"
        elif self._marks >= 60:
            self.__grade = "B"
        elif self._marks >= 40:
            self.__grade = "C"
        else:
            self.__grade = "F"

    def get_marks(self):
        return self._marks

    def get_grade(self):
        return self.__grade


s1 = Student("Ayesha", 85)
print(s1.name, "->", s1.get_marks(), s1.get_grade())

s2 = Student("Bilal", 55)
print(s2.name, "->", s2.get_marks(), s2.get_grade())

print("\n--- valid update ---")
s2.set_marks(72)
print(s2.name, "->", s2.get_marks(), s2.get_grade())

print("\n--- invalid update ---")
s2.set_marks(150)
print(s2.name, "->", s2.get_marks(), s2.get_grade())

# Extension: trying to reach the private attribute directly
print("\n--- direct access to __grade ---")
try:
    print(s2.__grade)
except AttributeError as e:
    print("AttributeError:", e)

# Explanation:
# Python renames __grade to _Student__grade inside the class (name mangling).
# So s2.__grade doesn't exist from outside and raises AttributeError.
# It's not real security though, s2._Student__grade would still work.
print("Via mangled name:", s2._Student__grade)




# Q2 - Secure Bank Account (Encapsulation)

class BankAccount:
    def __init__(self, holder_name, balance, pin):
        self.holder_name = holder_name
        self.__balance = balance
        self.__pin = pin

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit rejected: amount must be greater than zero.")
            return
        self.__balance += amount
        print(f"Deposited Rs. {amount}. ")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Withdrawal rejected: incorrect PIN.")
            return
        if amount <= 0:
            print("Withdrawal rejected: amount must be greater than zero.")
            return
        if amount > self.__balance:
            print("Withdrawal rejected: insufficient balance.")
            return
        self.__balance -= amount
        print(f"Withdrew Rs. {amount}.")

    def get_balance(self, pin):
        if pin != self.__pin:
            print("Incorrect PIN, can't show balance.")
            return None
        return self.__balance


acc = BankAccount("Hamza", 5000, 1234)
print("Account holder:", acc.holder_name)
print("Starting balance:", acc.get_balance(1234))

print("\n1) Successful deposit")
acc.deposit(2000)
print("Balance:", acc.get_balance(1234))

print("\n2) Successful withdrawal")
acc.withdraw(1500, 1234)
print("Balance:", acc.get_balance(1234))

print("\n3) Rejected: wrong PIN")
acc.withdraw(500, 9999)

print("\n4) Rejected: more than balance")
acc.withdraw(100000, 1234)

print("\nRejected: negative deposit")
acc.deposit(-300)

# Extension:
# Double underscores only trigger name mangling, they don't encrypt anything.
# Anyone can still read the value with acc._BankAccount__balance or
# acc._BankAccount__pin. Python has no real private members, it relies on
# programmers following conventions. Real security needs things like
# hashing the PIN, a database and proper access control.
print("\nBypassing the 'private' balance:", acc._BankAccount__balance)
print("Bypassing the 'private' pin:", acc._BankAccount__pin)



# Q3 - Employee Roles (Inheritance)

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)


class Developer(Employee):
    def __init__(self, name, emp_id, language):
        super().__init__(name, emp_id)
        self.language = language

    def display_details(self):
        super().display_details()
        print("Role: Developer")
        print("Programming Language:", self.language)


class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print("Role: Manager")
        print("Team Size:", self.team_size)


dev = Developer("Sara Khan", "E101", "Python")
mgr = Manager("Omar Sheikh", "E202", 8)

dev.display_details()
print("-" * 25)
mgr.display_details()




# Q4 - Vehicle Rental System (Inheritance)

class Vehicle:
    def __init__(self, brand, model, daily_rate):
        self.brand = brand
        self.model = model
        self.daily_rate = daily_rate

    def calculate_rent(self, days):
        if days <= 0:
            raise ValueError("Rental days must be more than zero")
        return self.daily_rate * days


class Car(Vehicle):
    insurance_fee = 1000

    def calculate_rent(self, days):
        base = super().calculate_rent(days)
        return base + Car.insurance_fee


class Bike(Vehicle):
    def calculate_rent(self, days):
        base = super().calculate_rent(days)
        return base - base * 0.10


car = Car("Toyota", "Corolla", 4000)
bike = Bike("Honda", "CD70", 800)

days = 3
print(f"{car.brand} {car.model} for {days} days: Rs. {car.calculate_rent(days):,.2f}")
print(f"{bike.brand} {bike.model} for {days} days: Rs. {bike.calculate_rent(days):,.2f}")

print("\nTrying invalid durations:")
for v in (car, bike):
    try:
        v.calculate_rent(0)
    except ValueError as e:
        print(f"{v.model}: {e}")


        # Q5 - Notification Dispatcher (Polymorphism)

class EmailNotification:
    def send(self, message):
        print("[Email] Sending email:", message)


class SMSNotification:
    def send(self, message):
        print("[SMS] Sending text message:", message)


class PushNotification:
    def send(self, message):
        print("[Push] Showing push alert:", message)


def notify_all(notifications, message):
    for n in notifications:
        n.send(message)


channels = [EmailNotification(), SMSNotification(), PushNotification()]
notify_all(channels, "Your order has been shipped!")

# New class added later, notify_all() stays exactly the same
class WhatsAppNotification:
    def send(self, message):
        print("[WhatsApp] Sending WhatsApp message:", message)


print()
channels.append(WhatsAppNotification())
notify_all(channels, "Your order has been delivered!")

# Where is the polymorphism?
# In notify_all(), the line n.send(message). The function doesn't know or care
# which class n belongs to, it just calls send() and each object responds in
# its own way. That's why WhatsAppNotification worked without touching the
# dispatcher.



# Q6 - Checkout Discount Calculator (Polymorphism)

def check_amount(amount):
    if amount < 0:
        raise ValueError("Bill amount can't be negative")


class RegularCustomer:
    def final_price(self, amount):
        check_amount(amount)
        return amount - amount * 0.05


class PremiumCustomer:
    def final_price(self, amount):
        check_amount(amount)
        return amount - amount * 0.10


class VIPCustomer:
    def final_price(self, amount):
        check_amount(amount)
        return amount - amount * 0.20


def print_receipt(customer, amount):
    final = customer.final_price(amount)
    print(f"{type(customer).__name__:<17} Bill: Rs. {amount:,.2f}  Pay: Rs. {final:,.2f}")


bill = 10000
for c in (RegularCustomer(), PremiumCustomer(), VIPCustomer()):
    print_receipt(c, bill)

# Extension: new customer type, print_receipt() is untouched
class GoldCustomer:
    def final_price(self, amount):
        check_amount(amount)
        return amount - amount * 0.15


print()
print_receipt(GoldCustomer(), bill)

print("\nNegative bill test:")
try:
    print_receipt(VIPCustomer(), -500)
except ValueError as e:
    print("Error:", e)



    # Q7 - Shape Calculator (Abstraction)
from abc import ABC, abstractmethod

PI = 3.14159


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2

    def perimeter(self):
        return 2 * PI * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


circle = Circle(5)
rect = Rectangle(4, 6)

print("Circle (radius 5)")
print("  Area:", round(circle.area(), 2))
print("  Perimeter:", round(circle.perimeter(), 2))

print("Rectangle (4 x 6)")
print("  Area:", rect.area())
print("  Perimeter:", rect.perimeter())

print("\nTrying to create a Shape directly:")
try:
    s = Shape()
except TypeError as e:
    print("TypeError:", e)

# Outcome: Python refuses to instantiate Shape because it has abstract
# methods (area and perimeter) that aren't implemented. An abstract class is
# only a blueprint, so only subclasses that implement every abstract method
# can be turned into objects.





# Q8 - Payment Gateway (Abstraction)
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def check_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")


class CardPayment(PaymentMethod):
    def pay(self, amount):
        self.check_amount(amount)
        print(f"Method: Card | Type: Payment | Amount: Rs. {amount:,}")

    def refund(self, amount):
        self.check_amount(amount)
        print(f"Method: Card | Type: Refund | Amount: Rs. {amount:,}")


class WalletPayment(PaymentMethod):
    def pay(self, amount):
        self.check_amount(amount)
        print(f"Method: Wallet | Type: Payment | Amount: Rs. {amount:,}")

    def refund(self, amount):
        self.check_amount(amount)
        print(f"Method: Wallet | Type: Refund | Amount: Rs. {amount:,}")


class BankTransferPayment(PaymentMethod):
    def pay(self, amount):
        self.check_amount(amount)
        print(f"Method: Bank Transfer | Type: Payment | Amount: Rs. {amount:,}")

    def refund(self, amount):
        self.check_amount(amount)
        print(f"Method: Bank Transfer | Type: Refund | Amount: Rs. {amount:,}")


def process_transaction(method, amount):
    try:
        method.pay(amount)
    except ValueError as e:
        print("Transaction failed:", e)


methods = [CardPayment(), WalletPayment(), BankTransferPayment()]
for m in methods:
    process_transaction(m, 2500)

print("\nRefund example:")
methods[0].refund(500)

print("\nInvalid amount:")
process_transaction(methods[1], -100)

# Extension: new payment method, process_transaction() not changed
class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        self.check_amount(amount)
        print(f"Method: Crypto | Type: Payment | Amount: Rs. {amount:,}")

    def refund(self, amount):
        self.check_amount(amount)
        print(f"Method: Crypto | Type: Refund | Amount: Rs. {amount:,}")


print("\nNew method:")
process_transaction(CryptoPayment(), 7500)