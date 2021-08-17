 class User:       
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):    
        self.account_balance += amount 
        return self
        
    def make_withdrowal(self, amount):
        self.account_balance -= amount
        return self
        
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
        
    def transfer_money(self, amount, other_user):
        self.account_balance = self.account_balance - amount
        other_user.account_balance = other_user.account_balance + amount 

michael = User("Michael", "michael@michael.com")
peter = User("Peter", "peter@peter.com")
mary = User("Mary", "mary@mary.com")

michael.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrowal(100).display_user_balance()
print(michael.account_balance)

peter.make_deposit(200).make_deposit(50).make_withdrowal(100).make_withdrowal(10).display_user_balance()
print(peter.account_balance)

mary.make_deposit(500).make_withdrowal(100).make_withdrowal(10).make_withdrowal(20).display_user_balance()
print(mary.account_balance)


michael.transfer_money(100, mary)
        
print(michael.account_balance)    
print(mary.account_balance)