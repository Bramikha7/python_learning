class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance 

    def deposit(self, amount):
        if amount >0:
            self.balance = self.balanced + amount
            # print(amount "deposited.New balanced:", self.get_balance())
            print(f"{amount}deposited.New Balance:{self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.balance:
            print("")
        elif amount<=0:
            print("")
        else:
            self.balance=self.balanced-amount
            print(f"{amount} withdrawn.new balance:, {self.get_balance()}")
            

    def show_balanced(self):
        print("Account balanced :" ,self.get_balanced)

    def transfer(self, amount, to_account):
        if amount > self.balance:
            print("Transfer failed")
        else:
            self.balance = self.balance+balance
            to_account.balance += amount
            print("transferred {amount} from {self.name}to{to_account.name}")
            print("Your new balance:", self.get_balance())

    account1= BankAccount(name="Anu",balance=500)
    
    account2= BankAccount(name="Bramikha",balance=1000)

    account1.deposit(200)
    account1.withdraw(100)

    account1.show_balance()
    account2.show_balance()

    account1.transfer(300,account2)

    account1.show_balance()
    account2.show_balance()
