import sys
import pytest
from main import main

def test_check_balance(capsys):
    sys.argv = ["main.py", "1"]
    main()
    captured = capsys.readouterr()
    assert "Current Balance: $1000.00" in captured.out

def test_deposit_money(capsys):
    sys.argv = ["main.py", "2", "500"]
    main()
    captured = capsys.readouterr()
    assert "New Balance: $1500.00" in captured.out

def test_withdraw_money_success(capsys):
    sys.argv = ["main.py", "3", "400"]
    main()
    captured = capsys.readouterr()
    assert "New Balance: $600.00" in captured.out

def test_withdraw_money_insufficient(capsys):
    sys.argv = ["main.py", "3", "1200"]
    main()
    captured = capsys.readouterr()
    assert "Insufficient balance" in captured.out
