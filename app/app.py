import sys

def show_menu():
    print("\n=== Simple Banking Application ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Exit")

def main():
    balance = 1000.0  # Initial starting balance
    
    # If arguments are passed (used for automated validation/testing)
    if len(sys.argv) > 1:
        choice = sys.argv[1]
        if choice == "1":
            print(f"Current Balance: ${balance:.2f}")
            return
        elif choice == "2":
            try:
                amount = float(sys.argv[2])
                if amount <= 0:
                    print("Invalid amount.")
                    return
                balance += amount
                print(f"Successfully deposited ${amount:.2f}. New Balance: ${balance:.2f}")
                return
            except (ValueError, IndexError):
                print("Invalid deposit amount execution.")
                return

    # Standard interactive console loop
    while True:
        show_menu()
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "1":
            print(f"\nCurrent Balance: ${balance:.2f}")
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))
                if amount > 0:
                    balance += amount
                    print(f"Deposited: ${amount:.2f}. New Balance: ${balance:.2f}")
                else:
                    print("Amount must be greater than zero.")
            except ValueError:
                print("Invalid input numerical value.")
        elif choice == "3":
            print("Thank you for using Simple Banking Application!")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()
