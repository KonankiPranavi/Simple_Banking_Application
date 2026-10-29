import sys
import pytest
from main import main

def test_check_balance(capsys):
    sys.argv = ["main.py", "1"]
   import sys
import pytest
from app import main

def test_check_balance(capsys):
    sys.argv = ["app.py", "1"]
    main()
    captured = capsys.readouterr()
    assert "Current Balance: $1000.00" in captured.out

def test_deposit_money(capsys):
    sys.argv = ["app.py", "2", "500"]
    main()
    captured = capsys.readouterr()
    assert "New Balance: $1500.00" in captured.out
