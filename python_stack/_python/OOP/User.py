class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
    	self.account.deposit(self,amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(self,amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info(self)
        return self
    
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount) 
        return self


todd = User("Todd", "todd@todd.com")
jane = User("Jane", "jane@jane.com")
john = User("John", "john@john.com")

todd.make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance()

jane.make_deposit(50).make_deposit(1000).make_withdrawal(500).make_withdrawal(100).display_user_balance()

john.make_deposit(100).make_withdrawal(25).make_withdrawal(25).make_withdrawal(25).display_user_balance()

todd.transfer_money(jane,250).display_user_balance()
jane.display_user_balance()