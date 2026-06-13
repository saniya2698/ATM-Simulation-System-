balance = 1000
transaction_history = []

def deposit():
    global balance

    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        balance += amount
        transaction_history.append(f"Deposited ₹{amount}")

        print(f"₹{amount} deposited successfully.")
        print(f"Current Balance: ₹{balance}")

    except ValueError:
        print("Invalid amount entered.")


def withdraw():
    global balance

    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if amount > balance:
            print("Insufficient Balance.")
            return

        balance -= amount
        transaction_history.append(f"Withdrawn ₹{amount}")

        print(f"₹{amount} withdrawn successfully.")
        print(f"Current Balance: ₹{balance}")

    except ValueError:
        print("Invalid amount entered.")


def check_balance():
    print(f"\nCurrent Balance: ₹{balance}\n")


def show_history():
    print("\nTransaction History")

    if len(transaction_history) == 0:
        print("No transactions found.")

    else:
        for transaction in transaction_history:
            print(transaction)

    print()


while True:

    print("========================= ATM Simulation =========================")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Inquiry")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        deposit()

    elif choice == "2":
        withdraw()

    elif choice == "3":
        check_balance()

    elif choice == "4":
        show_history()

    elif choice == "5":
        print("Thank You for Using ATM.")
        break

    else:
        print("Invalid Choice.")