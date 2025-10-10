# test_bank_account.py
# Unit tests for the BankAccount class using pytest.

import pytest
from bank_account import BankAccount


# ---------- Fixtures ----------
# A fixture is any code that sets up or prepares the environment for
# a test and optionally cleans up afterward. Think of a fixture as a
# preparation step that ensures every test starts from a known, controlled state.
# Fixtures are defined using the @pytest.fixture decorator.
# @pytest.fixture marks a function as a fixture provider.
# That function can then be used by any test simply by naming it as a parameter.
@pytest.fixture
def sample_account():
    """
    Fixture that provides a fresh bank account for each test.
    @param: none
    @:return: BankAccount instance with initial balance of 100
    @:exceptions: none
    """
    return BankAccount("Alice", 100)

@pytest.fixture
def target_account():
    """
    Another account to test transfers.
    @param: none
    @:return: BankAccount instance with initial balance of 50
    @:exceptions: none
    """
    return BankAccount("Bob", 50)


# ---------- Tests ----------
def test_initial_balance(sample_account):
    """
    Test that the initial balance is set correctly.
    @param sample_account: an account object provided by the fixture
    @return: none
    @exceptions: none
    """
    assert sample_account.owner == "Alice"
    assert sample_account.balance == 100


def test_deposit_increases_balance(sample_account):
    """
    Test that depositing money increases the balance.
    @param sample_account: an account object provided by the fixture
    @return: none
    @exceptions: ValueError from deposit for negative deposit
    """
    sample_account.deposit(50)
    assert sample_account.balance == 150


def test_deposit_negative_amount_raises_error(sample_account):
    """
    Test that depositing a negative amount raises a ValueError.
    @param sample_account: an account object provided by the fixture
    @return: none
    @exceptions: ValueError for negative deposit
    """
    with pytest.raises(ValueError):
        sample_account.deposit(-10)


def test_withdraw_decreases_balance(sample_account):
    """
    Test that withdrawing money decreases the balance.
    @param sample_account: an account object provided by the fixture
    @return: none
    @exceptions: ValueError from withdraw for insufficient funds
    """
    sample_account.withdraw(30)
    assert sample_account.balance == 70


def test_withdraw_too_much_raises_error(sample_account):
    """
    Test that withdrawing more than the balance raises a ValueError.
    @param sample_account: an account object provided by the fixture
    @return: none
    @exceptions: ValueError for insufficient funds
    """
    with pytest.raises(ValueError):
        sample_account.withdraw(999)


def test_transfer_between_accounts(sample_account, target_account):
    """
    Test transferring money between two accounts.
    @param sample_account, target_account: objects provided by fixtures
    @return: none
    @exceptions: ValueError from withdraw for insufficient funds
    """
    sample_account.transfer(target_account, 40)
    assert sample_account.balance == 60
    assert target_account.balance == 90


def test_withdraw_zero_raises_error(sample_account):
    """
    Test that withdrawing zero raises a ValueError.
    @param sample_account: an account object provided by the fixture
    @return: none
    @exceptions: ValueError for zero withdrawal
    """
    with pytest.raises(ValueError):
        sample_account.withdraw(0)
