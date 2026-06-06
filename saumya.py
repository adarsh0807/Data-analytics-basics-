from datetime import datetime

# Transaction class to store transaction details
class Transaction:
    def __init__(self, date, trans_type, amount):
        self.date = date
        self.trans_type = trans_type
        self.amount = amount
    
    def __str__(self):
        return f"{self.date}: {self.trans_type.capitalize()} of ${self.amount:.2f}"

# Base Account class
class Account:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance
        self.transaction_history = []  # List to store transactions
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction("deposit", amount)
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.add_transaction("withdraw", amount)
            return True
        return False
    
    def add_transaction(self, trans_type, amount):
        transaction = Transaction(datetime.now(), trans_type, amount)
        self.transaction_history.append(transaction)
    
    def get_balance(self):
        return self.balance
    
    def get_account_number(self):
        return self.account_number
    
    def get_owner(self):
        return self.owner
    
    def get_transaction_history(self):
        return self.transaction_history

# SavingsAccount class with interest rate
class SavingsAccount(Account):
    def __init__(self, account_number, owner, initial_balance=0, interest_rate=0.01):
        super().__init__(account_number, owner, initial_balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        return interest

# CheckingAccount class with overdraft limit
class CheckingAccount(Account):
    def __init__(self, account_number, owner, initial_balance=0, overdraft_limit=100):
        super().__init__(account_number, owner, initial_balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > 0 and (self.balance + self.overdraft_limit) >= amount:
            self.balance -= amount
            self.add_transaction("withdraw", amount)
            return True
        return False

# Bank class to manage accounts
class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to store accounts
    
    def add_account(self, account):
        if account.get_account_number() not in self.accounts:
            self.accounts[account.get_account_number()] = account
            return True
        print("Account number already exists.")
        return False
    
    def get_account(self, account_number):
        return self.accounts.get(account_number)
    
    def list_all_accounts(self):
        if not self.accounts:
            print("No accounts exist.")
            return
        for account in self.accounts.values():
            print(f"Account Number: {account.get_account_number()}, Owner: {account.get_owner()}, Balance: ${account.get_balance():.2f}")
    
    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        if from_account and to_account:
            if from_account.withdraw(amount):
                to_account.deposit(amount)
                print("Transfer successful.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("One or both accounts do not exist.")
    
    def find_accounts_above_balance(self, amount):
        return [acc for acc in self.accounts.values() if acc.get_balance() > amount]

# Main function with command-line interface
def main():
    bank = Bank()
    while True:
        print("\n=== Bank System Menu ===")
        print("1. Create account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Transfer money")
        print("5. View account details")
        print("6. View transaction history")
        print("7. List all accounts")
        print("8. Find accounts above balance")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")
        
        try:
            if choice == "1":
                acc_type = input("Account type (savings/checking): ").lower()
                acc_num = input("Account number: ")
                owner = input("Owner name: ")
                balance = float(input("Initial balance: "))
                
                if acc_type == "savings":
                    rate = float(input("Interest rate (e.g., 0.02 for 2%): "))
                    account = SavingsAccount(acc_num, owner, balance, rate)
                elif acc_type == "checking":
                    limit = float(input("Overdraft limit: "))
                    account = CheckingAccount(acc_num, owner, balance, limit)
                else:
                    print("Invalid account type.")
                    continue
                
                if bank.add_account(account):
                    print("Account created successfully.")
            
            elif choice == "2":
                acc_num = input("Account number: ")
                amount = float(input("Amount to deposit: "))
                account = bank.get_account(acc_num)
                if account and account.deposit(amount):
                    print("Deposit successful.")
                elif not account:
                    print("Account not found.")
                else:
                    print("Invalid amount.")
            
            elif choice == "3":
                acc_num = input("Account number: ")
                amount = float(input("Amount to withdraw: "))
                account = bank.get_account(acc_num)
                if account and account.withdraw(amount):
                    print("Withdrawal successful.")
                elif not account:
                    print("Account not found.")
                else:
                    print("Insufficient funds or invalid amount.")
            
            elif choice == "4":
                from_acc = input("From account number: ")
                to_acc = input("To account number: ")
                amount = float(input("Amount to transfer: "))
                bank.transfer(from_acc, to_acc, amount)
            
            elif choice == "5":
                acc_num = input("Account number: ")
                account = bank.get_account(acc_num)
                if account:
                    print(f"Account Number: {account.get_account_number()}")
                    print(f"Owner: {account.get_owner()}")
                    print(f"Balance: ${account.get_balance():.2f}")
                    if isinstance(account, SavingsAccount):
                        print(f"Interest Rate: {account.interest_rate*100}%")
                    elif isinstance(account, CheckingAccount):
                        print(f"Overdraft Limit: ${account.overdraft_limit:.2f}")
                else:
                    print("Account not found.")
            
            elif choice == "6":
                acc_num = input("Account number: ")
                account = bank.get_account(acc_num)
                if account:
                    history = account.get_transaction_history()
                    if history:
                        print("Transaction History:")
                        for trans in history:
                            print(trans)
                    else:
                        print("No transactions yet.")
                else:
                    print("Account not found.")
            
            elif choice == "7":
                bank.list_all_accounts()
            
            elif choice == "8":
                amount = float(input("Enter balance threshold: "))
                accounts = bank.find_accounts_above_balance(amount)
                if accounts:
                    print(f"Accounts with balance above ${amount:.2f}:")
                    for acc in accounts:
                        print(f"Account Number: {acc.get_account_number()}, Owner: {acc.get_owner()}, Balance: ${acc.get_balance():.2f}")
                else:
                    print("No accounts found above this balance.")
            
            elif choice == "9":
                print("Exiting Bank System. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please select 1-9.")
        
        except ValueError:
            print("Invalid input. Please enter numeric values where required.")

if __name__ == "__main__":
    main()