class Bank:
    def __init__(self, name, age):
        self.balance = 0
        print(f'Welcome {name}')

    def deposit(self, amount):
        self.balance += amount
        print(f'You deposit {amount} EGP - Your balance now : {self.balance} EGP')

    # def withdraw(self, amount):
    #     if amount <= self.balance:
    #         self.balance -= amount
    #         print(f'You withdraw {amount} EGP - Your balance now : {self.balance} EGP')
    #     else :
    #         print(f'You dont have enough balance')

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'You dont have enough balance')
            return

        self.balance -= amount
        print(f'You withdraw {amount} EGP - Your balance now : {self.balance} EGP')
        

c1 = Bank('Mohamed', 25)
c1.deposit(500)
c1.deposit(1000)
c1.deposit(700)

c1.withdraw(700)
c1.withdraw(700)
c1.withdraw(1700)