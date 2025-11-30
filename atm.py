import os

PIN_FILE = "pin.txt"
BALANCE_FILE = "balance.txt"


def setup_files():
    if not os.path.exists(PIN_FILE):
        with open(PIN_FILE, "w") as f:
            f.write("1234")

    if not os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "w") as f:
            f.write("1000")


def get_pin():
    with open(PIN_FILE, "r") as f:
        return f.read().strip()


def set_pin(new_pin):
    with open(PIN_FILE, "w") as f:
        f.write(new_pin)


def get_balance():
    with open(BALANCE_FILE, "r") as f:
        return float(f.read().strip())


def set_balance(amount):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(amount))

# ---------------------------
# PIN VERIFICATION (3 tries)
# ---------------------------
def verify_pin():
    stored_pin = get_pin()
    attempts = 3

    while attempts > 0:
        user_pin = input("Enter your PIN: ")

        if user_pin == stored_pin:
            print("PIN accepted. Welcome!")
            return True
        else:
            attempts -= 1
            print(f"Wrong PIN! Attempts left: {attempts}")

    print("Too many wrong attempts. Card blocked.")
    return False

# ---------------------------
# ATM Menu Functions
# ---------------------------
def check_balance():
    print(f"Your balance is: ₹{get_balance()}")

def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        new_bal = get_balance() + amount
        set_balance(new_bal)
        print(f"Deposited ₹{amount}. New balance: ₹{new_bal}")
    else:
        print("Invalid amount.")

def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    bal = get_balance()

    if amount <= 0:
        print("Invalid amount.")
    elif amount > bal:
        print("Not enough balance.")
    else:
        new_bal = bal - amount
        set_balance(new_bal)
        print(f"Withdrew ₹{amount}. New balance: ₹{new_bal}")

def change_pin():
    current = input("Enter your current PIN: ")

    if current != get_pin():
        print("Wrong current PIN.")
        return

    new_pin = input("Enter new PIN: ")
    confirm = input("Confirm new PIN: ")

    if new_pin == confirm:
        set_pin(new_pin)
        print("PIN changed successfully!")
    else:
        print("PINs do not match.")

# ---------------------------
# MAIN PROGRAM
# ---------------------------
def main():
    setup_files()

    print("===== Welcome to Python ATM =====")

    if not verify_pin():
        return  

    while True:
        print("\nChoose an option:")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            print("Thank you for using Python ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()