#Bank Account Simulator

class BankAccount:
    def __init__(self, account_holder, initial_balance = 0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance  += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Witdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid withdrawal amoun or insufficient funds.")

    def show_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Balance: ${self.balance}")

accounts = {}

def create_account():
    name = input("Enter account holder's name: ").strip()
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(name, initial_balance)
    accounts[name] = account

    print("Account created successfully!")

def access_account():
    name = input("Enter your name: ").strip()
    if name in accounts:
        account = accounts[name]
        while True:
            print("\n--- Account Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Details")
            print("4. Exit")
            choice = input("Enter your choice(1-4):")

            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == '3':
                account.show_details()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Account not found. Please create an account first.ww") 

while True:
    print("\n--- Main Menu ---")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")
    main_choice = input("Enter your choice(1-3): ")

    if main_choice == '1':
        create_account()
    elif main_choice == '2':
        access_account()
    elif main_choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")