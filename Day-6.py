# Polymorphism
# Payment System

class Payment:
    def pay(self):
        print("Processing payment...")

class GooglePay(Payment):
    def pay(self):
        print("Payment done using Google Pay")

class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe")

class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card")

payment = Payment()
gpay = GooglePay()
phonepe = PhonePe()
credit = CreditCard()
payment.pay()
gpay.pay()
phonepe.pay()
credit.pay()