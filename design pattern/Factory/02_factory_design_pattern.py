# from enum import Enum
from enum import Enum, auto
from inspect import getmembers, isclass, isabstract
# import payment_methods
class CreditCardPayment:
    def __init__(self):
        print("Credit Card Payment Initialized")

class PayPalPayment:
    def __init__(self):
        print("PayPal Payment Initialized")

class GooglePayPayment:
    def __init__(self):
        print("Google Pay Payment Initialized")

class PaymentFactory:
    @staticmethod
    def create(payment_method: PaymentMethod):
        if payment_method == PaymentMethod.CREDIT_CARD:
            return CreditCardPayment()
        elif payment_method == PaymentMethod.PAYPAL:
            return PayPalPayment()
        elif payment_method == PaymentMethod.GOOGLE_PAY:
            return GooglePayPayment()
        else:
            raise ValueError(f"{payment_method} is not currently supported as a payment method.")



class PaymentMethod(Enum):
    CREDIT_CARD = 1
    PAYPAL = 2
    GOOGLE_PAY = 3


# Creator
class DynamicPaymentFactory(object):
    # A dictionary to store the available payment implementations
    payment_dictionary = {}

    def __init__(self):
        self.load_payment_methods()

    def load_payment_methods(self):
        members = getmembers(
            payment_methods, lambda m: isclass(m) and not isabstract(m)
        )
        for name, _type in members:
            if isclass(_type) and issubclass(_type, payment_methods.Payment):
                self.payment_dictionary[name] = _type

    def create(self, payment_type: str):
        if payment_type in self.payment_dictionary:
            return self.payment_dictionary[payment_type]()
        else:
            raise ValueError(
                f"{payment_type} is not currently supported as a payment method."
            )
            
            



# from dynamic_payment_factory import DynamicPaymentFactory
# from payment_factory import PaymentFactory
# from payment_method import PaymentMethod


# Client
def main():
    # factory = DynamicPaymentFactory()
    # payment = PaymentFactory.create(PaymentMethod.CREDIT_CARD)
    factory = DynamicPaymentFactory()
    factory.load_payment_methods()
    payment = factory.create("CreditCardPayment")
    # payment.pay(1000.00)


if __name__ == "__main__":
    main()