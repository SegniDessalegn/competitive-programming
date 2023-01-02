class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1 -= 1
        account2 -= 1
        if account1 < len(self.balance) and account2 < len(self.balance) and self.balance[account1] >= money:
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        account -= 1
        if account < len(self.balance):
            self.balance[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        account -= 1
        if account < len(self.balance) and self.balance[account] >= money:
            self.balance[account] -= money
            return True
        return False
