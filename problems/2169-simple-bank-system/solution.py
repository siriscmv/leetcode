class Bank:
    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.bal = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 > self.n: return False
        if account2 < 1 or account2 > self.n: return False 
        if self.bal[account1-1] < money: return False
        self.bal[account1-1] -= money
        self.bal[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n: return False
        self.bal[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n: return False
        if self.bal[account-1] < money: return False
        self.bal[account-1] -= money
        return True
