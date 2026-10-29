class BankingSystem:
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

def main():
    account = BankingSystem(1000.0)
    print("--- Simple Banking Application ---")
    while True:
        print("\n1. Check Balance\n2. Deposit Money\n3. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            print(f"Current Balance: ${account.check_balance():.2f}")
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if account.deposit(amount):
                print(f"Successfully deposited ${amount:.2f}. New balance: ${account.check_balance():.2f}")
            else:
                print("Invalid deposit amount.")
        elif choice == "3":
            print("Thank you for using the banking application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
