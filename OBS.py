import datetime

class Card():
    def __init__(self, balance, credit_limit):
        self.balance = balance
        self.credit_limit = credit_limit

class Debitcard(Card):
    def __init__(self, balance, credit_limit):
        super().__init__(balance, credit_limit)

    def Withdraw(self):
        x1 = datetime.datetime.now()
        rs1 = int(input("Enter the amount to be withdrawn : ₹"))
        if rs1 > self.balance:
            print("Insufficient balance.")
            return
        print("Successfully withdrawn ₹", rs1, "on", x1)
        self.balance = self.balance - rs1

    def Deposit(self):
        x2 = datetime.datetime.now()
        rs2 = int(input("Enter the amount to be deposited : ₹"))
        print("Successfully deposited ₹", rs2, "on", x2)
        self.balance = self.balance + rs2

    def CheckBal(self):
        x3 = datetime.datetime.now()
        print("The balance available in our account on", x3, "is ₹", self.balance)

class Creditcard(Card):
    def __init__(self, credit_limit):
        super().__init__(0, credit_limit)  # Initialize balance to 0 for credit card
        self.time = datetime.datetime.now()
        self.credit_balance = 0
        self.payback = 0

    def Withdraw(self):
        x4 = datetime.datetime.now()
        rs3 = int(input("Enter the amount you want to use : ₹"))
        if rs3 > self.credit_limit:
            print("Credit limit exceeded.")
            return

        print("Successfully withdrawn ₹", rs3, "on", x4)
        self.credit_limit = self.credit_limit - rs3
        self.credit_balance = self.credit_balance + rs3
        self.time = x4

    def CreditDetails(self):
        x5 = datetime.datetime.now()
        print("Amount available to use on", x5, "is ₹", self.credit_limit)
        print("Last transaction on this credit card was on", self.time)
        if self.time.year == x5.year and self.time.month == x5.month:
            self.payback = self.credit_balance
            print("The amount to be paid back as on", x5, "is ₹", self.payback)
        else:
            diff = (x5.year - self.time.year) * 12 + (x5.month - self.time.month)
            rate = 1 + diff * 0.1  # 10% interest per month
            self.payback = self.credit_balance * rate
            print("The amount to be paid back as of", x5, "is ₹", self.payback)

    def pay_back(self):
        x6 = datetime.datetime.now()
        amt = int(input("Enter the amount to be paid back : "))
        self.credit_balance -= amt
        if self.credit_balance < 0 :
            self.credit_balance = 0
        print("Amount paid back successfully on", x6)

obj1 = Debitcard(100000, 50000)
obj2 = Creditcard(50000)

obj1.Withdraw()
obj1.Withdraw()
obj1.CheckBal()