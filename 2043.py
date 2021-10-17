class Bank:

    def __init__(self, balance: List[int]):
        # All account balances
        self.accs = [0] + balance        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Make sure both account ids are valid
        if not self.valid(account1) or not self.valid(account2):
            return False
        # Make sure there is enough money in acc1
        if money > self.accs[account1]:
            return False
        self.accs[account1] -= money
        self.accs[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        # Make sure account is avlid
        if not self.valid(account):
            return False
        self.accs[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # Make sure account is valid and has enough funds to withdraw
        if not self.valid(account) or self.accs[account] < money:
            return False
        self.accs[account] -= money
        return True

    def valid(self, acc):
        return acc >= 1 and acc < len(self.accs)
