class Account:
    def __init__(self, acc_num, owner, balance=0):
        self.acc_num = acc_num
        self.owner = owner
        self.balance = balance
        self.transactions = []  # List for transaction history
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit ${amount}")
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdraw ${amount}")

class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to store accounts
    
    def add_account(self, acc_num, owner, balance):
        if acc_num not in self.accounts:
            self.accounts[acc_num] = Account(acc_num, owner, balance)
    
    def get_account(self, acc_num):
        return self.accounts.get(acc_num)
    
    def list_accounts(self):
        for acc in self.accounts.values():
            print(f"Account: {acc.acc_num}, Owner: {acc.owner}, Balance: ${acc.balance}")

def main():
    bank = Bank()
    while True:
        print("\n1. Create Account  2. Deposit  3. Withdraw  4. View Details  5. List Accounts  6. Exit")
        choice = input("Choice: ")
        
        if choice == "1":
            acc_num = input("Account number: ")
            owner = input("Owner name: ")
            balance = float(input("Initial balance: "))
            bank.add_account(acc_num, owner, balance)
            print("Account created.")
        
        elif choice == "2":
            acc_num = input("Account number: ")
            amount = float(input("Amount: "))
            acc = bank.get_account(acc_num)
            if acc:
                acc.deposit(amount)
                print("Deposit done.")
            else:
                print("Account not found.")
        
        elif choice == "3":
            acc_num = input("Account number: ")
            amount = float(input("Amount: "))
            acc = bank.get_account(acc_num)
            if acc:
                acc.withdraw(amount)
                print("Withdrawal done.")
            else:
                print("Account not found.")
        
        elif choice == "4":
            acc_num = input("Account number: ")
            acc = bank.get_account(acc_num)
            if acc:
                print(f"Account: {acc.acc_num}, Owner: {acc.owner}, Balance: ${acc.balance}")
                for trans in acc.transactions:
                    print(trans)
            else:
                print("Account not found.")
        
        elif choice == "5":
            bank.list_accounts()
        
        elif choice == "6":
            print("Goodbye!")
            break
        
        else:
              print("Invalid choice.")

main()