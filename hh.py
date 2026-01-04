class BankAccount:
    # ===== class variable =====
    bank_name = "Global Bank"
    accounts_count = 0

    # ===== constructor (instance initialization) =====
    def __init__(self, owner, balance=0):
        self.owner = owner          # instance variable
        self.balance = balance      # instance variable
        BankAccount.accounts_count += 1

    # ===== instance method =====
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}, new balance: {self.balance}"
        return "Invalid amount"

    # ===== instance method =====
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn {amount}, remaining balance: {self.balance}"
        return "Insufficient funds"

    # ===== instance method =====
    def get_balance(self):
        return self.balance

    # ===== class method =====
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    # ===== class method =====
    @classmethod
    def get_accounts_count(cls):
        return cls.accounts_count

    # ===== static method =====
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    # ===== static method =====
    @staticmethod
    def bank_rules():
        return "Minimum balance is 0, no overdraft allowed."
