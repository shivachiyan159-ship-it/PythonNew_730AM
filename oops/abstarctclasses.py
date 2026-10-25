# abstarction means it is a concept to hid ethe implementation
# abstarct class is a machanism to enforce a contract between parent and child class
# abstarct class may contain abstarct methods and non abstarct methods
# abstarct method contains only declatration


from abc import ABC, abstractmethod


# class UPI:
#     def UPIpay(self):
#         print("payment processing using UPI")


# class CreditCard:
#     def Creditcardpayment(self):
#         print("payment processing using creditcard")


# class NetBanking:
#     def Netbankingpay(self):
#         print("payment processing using netbanking")


# upiobj = UPI()
# upiobj.UPIpay()

# credobj = CreditCard()
# credobj.Creditcardpayment()


class Payment(ABC):

    @abstractmethod
    def payment(self):
        pass

    def display(self):
        print("display info")


class UPI(Payment):
    def payment(self):
        print("upi paymnet processing")


class CreditCard(Payment):
    def payment(self):
        print("creditcard paymnet processing")


class Netbanking(Payment):
    def payment(self):
        print("Netbanking paymnet processing")


upiobj = UPI()
upiobj.payment()
upiobj.display()


upiobj = CreditCard()
upiobj.payment()
upiobj.display()


upiobj = Netbanking()
upiobj.payment()
upiobj.display()


# university (JNTU)
# rules
# coursefee - 50000
# courses - ece , eee , cse , it , mech


# stanns college(JNTU)
# course fee - 50000
# ece ,it


# quiss college(JNTU)
# course fee - 65000 # wrong
# ece ,it
