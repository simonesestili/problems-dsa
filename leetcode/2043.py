class Bank:
    def __init__(self, balance):
        self.bal = [-1] + balance

    def transfer(self, a, b, money):
        if a < len(self.bal) and b < len(self.bal) and self.bal[a] >= money:
            self.bal[a] -= money
            self.bal[b] += money
            return True
        return False

    def deposit(self, a, money):
        if a < len(self.bal):
            self.bal[a] += money
            return True
        return False

    def withdraw(self, a, money):
        if a < len(self.bal) and self.bal[a] >= money:
            self.bal[a] -= money
            return True
        return False
