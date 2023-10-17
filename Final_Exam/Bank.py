class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = User.generate_account_number()
        self.transaction_history = []

    @staticmethod
    def generate_account_number():
        User.account_counter = getattr(User, 'account_counter', 0) + 1
        return User.account_counter

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            print(f"Deposited ${amount} into Account {self.account_number}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            print(f"Withdrew ${amount} from Account {self.account_number}")
        else:
            print("Withdrawal amount exceeded. Insufficient funds.")

    def check_balance(self):
        return self.balance

    def view_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if User.loan_feature and amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Took a loan of ${amount}")
            User.loan_limit -= 1
            print(f"Loan of ${amount} taken from Account {self.account_number}")

    def transfer(self, recipient, amount):
        if recipient in User.users:
            if self.balance >= amount:
                self.balance -= amount
                recipient_account = User.users[recipient]
                recipient_account.deposit(amount)
                self.transaction_history.append(f"Transferred ${amount} to Account {recipient_account.account_number}")
                print(f"Transferred ${amount} to Account {recipient_account.account_number}")
            else:
                print("Insufficient funds for the transfer.")
        else:
            print("Account does not exist.")

class Admin:
    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        User.users[name] = user
        print(f"Account created for {name}")

    def delete_account(self, name):
        if name in User.users:
            del User.users[name]
            print(f"Account for {name} deleted.")
        else:
            print("Account not found.")

    def list_accounts(self):
        for user in User.users:
            print(f"Name: {user}, Account Number: {User.users[user].account_number}")

    def total_bank_balance(self):
        return sum(user.balance for user in User.users.values())

    def total_loan_amount(self):
        return (User.loan_limit * 1000)

    def toggle_loan_feature(self, enable):
        User.loan_feature = enable
        if enable:
            print("Loan feature enabled.")
        else:
            print("Loan feature disabled.")


User.users = {}
User.loan_limit = 2
User.loan_feature = False

admin = Admin()
while True:
    print("\nBanking System Options:")
    print("1. User Menu")
    print("2. Admin Menu")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        user_name = input("Enter your name: ")
        if user_name in User.users:
            user = User.users[user_name]
            while True:
                print(f"\nWelcome, {user_name} (Account Number: {user.account_number})")
                print("User Menu:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. View Transaction History")
                print("5. Take Loan")
                print("6. Transfer Money")
                print("7. Back to Main Menu")
                option = input("Enter your choice: ")
                    
                if option == "1":
                    amount = float(input("Enter the amount to deposit: "))
                    user.deposit(amount)
                elif option == "2":
                    amount = float(input("Enter the amount to withdraw: "))
                    user.withdraw(amount)
                elif option == "3":
                    balance = user.check_balance()
                    print(f"Account Balance: ${balance}")
                elif option == "4":
                    history = user.view_transaction_history()
                    print("Transaction History:")
                    for transaction in history:
                        print(transaction)
                elif option == "5":
                    amount = float(input("Enter the loan amount: "))
                    user.take_loan(amount)
                elif option == "6":
                    recipient = input("Enter recipient's name: ")
                    amount = float(input("Enter the amount to transfer: "))
                    user.transfer(recipient, amount)
                elif option == "7":
                    break
                else:
                    print("Invalid option. Please try again.")

    elif choice == "2":
        print("Admin Menu:")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. List Accounts")
        print("4. Total Bank Balance")
        print("5. Total Loan Amount")
        print("6. Toggle Loan Feature")
        print("7. Back to Main Menu")
        admin_option = input("Enter your choice: ")

        if admin_option == "1":
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            address = input("Enter user's address: ")
            account_type = input("Enter account type (Savings/Current): ")
            admin.create_account(name, email, address, account_type)
        elif admin_option == "2":
            name = input("Enter user's name to delete: ")
            admin.delete_account(name)
        elif admin_option == "3":
            admin.list_accounts()
        elif admin_option == "4":
            total_balance = admin.total_bank_balance()
            print(f"Total Bank Balance: ${total_balance}")
        elif admin_option == "5":
            total_loans = admin.total_loan_amount()
            print(f"Total Loan Amount: ${total_loans}")
        elif admin_option == "6":
            enable_loan = input("Enable loan feature? (yes/no): ")
            admin.toggle_loan_feature(enable_loan.lower() == "yes")
        elif admin_option == "7":
             pass
        else:
            print("Invalid option. Please try again.")

    elif choice == "3":
        break
    else:
         print("Invalid option. Please try again.")

