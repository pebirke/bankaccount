class BankAccount(object):
    balance = 0
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "%s's account. Balance: $%.2f" % (self.name, self.balance)
    def show_balance(self):
        print "%s's balance: $%.2f" % (self.name, self.balance)
    def deposit(self, amount):
        if amount <= 0:
            print "Error! Invalid deposit"
            return
        else:
            print "%s is depositing $%.2f" % (self.name, amount)
            self.balance += amount
        self.show_balance()
    def withdraw(self, amount):
        if amount > self.balance:
            print "Error! Insufficient funds"
            return
        else:
            print "%s is withdrawing $%.2f" % (self.name, amount)
            self.balance -= amount
        self.show_balance()
