# bank_account.py
# Simple class to demonstrate pytest with classes.

class BankAccount:
    """A simple bank account class."""

    def __init__(self, owner, balance=0):
        """
        Initialize the bank account.
        @param owner: string the name of the account owner
        @param balance: float the starting balance (default 0)
        @:return: none
        @:exceptions: none
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit a positive amount into the account.
        @param amount: float the amount to deposit
        @:return: float the new balance
        @:exceptions: ValueError if amount is not positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraw an amount if funds are sufficient.
        @param amount: float the amount to withdraw
        @:return: float the new balance
        @:exceptions: ValueError if amount is not positive or insufficient funds
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def transfer(self, target_account, amount):
        """
        Transfer amount to another BankAccount.
        @param target_account: BankAccount the account to transfer to
        @param amount: float the amount to transfer
        @:return: none
        @:exceptions: ValueError if withdrawal fails
        """
        self.withdraw(amount)
        target_account.deposit(amount)
