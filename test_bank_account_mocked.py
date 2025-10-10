# test_bank_account_mocked.py
# Demonstrates pytest-mock for spying and verifying method calls.

from bank_account import BankAccount

def test_transfer_calls_withdraw_and_deposit(mocker):
    """
    Test that transfer() calls withdraw() and deposit() with correct arguments.
    1 Create two BankAccount instances
    2 We want to test that transfer():
    3 Calls withdraw() on the sender account.
    4 Calls deposit() on the target account.
    5 Passes the correct arguments to both.
    6 We check that the correct methods were called and the balances are correct
    @param mocker: a pytest-mock fixture for creating spies and mocks
    @return: none
    @exceptions: none
    """

    sender = BankAccount("Alice", 100)
    receiver = BankAccount("Bob", 50)

    # Spy on the methods we expect to be called
    spy_withdraw = mocker.spy(sender, "withdraw")
    spy_deposit = mocker.spy(receiver, "deposit")

    # Execute the transfer
    sender.transfer(receiver, 30)

    # Verify that withdraw and deposit were called once each
    spy_withdraw.assert_called_once_with(30)
    spy_deposit.assert_called_once_with(30)

    # Verify final balances (normal assertion)
    assert sender.balance == 70
    assert receiver.balance == 80
