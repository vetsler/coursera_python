class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
        self.has = self.name+' has '
    #Happy coding

    def withdraw(self,m2w):
        try:
            if self.balance - m2w < 0:
                raise ValueError
            else:
                self.balance = self.balance - m2w
                return self.has+str(self.balance)+'.'
        except ValueError:
            print('sorry he has only {0}'.format(self.balance))


    def check(self, user, money):
        try:
            if (user.balance - money < 0) or (not user.checking_account):
                raise ValueError
            else: 
                user.balance = user.balance - money
                self.balance = self.balance + money
                return self.has+str(self.balance)+' and ' +user.has+str(user.balance)+ '.'
        except ValueError:
            print('sorry {0} has less, only {1}, and account {2}'.format(user.name, user.balance, user.checking_account))
        
    
    def add_cash(self, money):
        self.balance = self.balance + money
        return self.has+str(self.balance)+'.'
