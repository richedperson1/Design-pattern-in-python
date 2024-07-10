from payment_method import PaymentMethod
from payment_methods import CreditCardPayment, PayPalPayment, GooglePayPayment

# class PaymentMethod(Enum):
#     CREDIT_CARD = 1
#     PAYPAL = 2
#     GOOGLE_PAY = 3
# Creator
# class PaymentFactory:
#     @staticmethod
#     def create(payment_method: PaymentMethod):
#         # match payment_method:
#             if  payment_method==1:
#                 return CreditCardPayment()
#             elif  payment_method==2:
#                 return PayPalPayment()
#             elif  payment_method==3:
#                 return GooglePayPayment()
#             else:
#                 raise ValueError(
#                     f"{payment_method} is not currently supported as a payment method."
#                 )
