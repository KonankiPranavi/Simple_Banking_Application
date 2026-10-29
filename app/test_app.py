from app import BankingSystem

def test_check_balance():
    account = BankingSystem(500.0)
    assert account.check_balance() == 500.0

def test_deposit():
    account = BankingSystem(500.0)
    assert account.deposit(200.0) is True
    assert account.check_balance() == 700.0

def test_invalid_deposit():
    account = BankingSystem(500.0)
    assert account.deposit(-50.0) is False
