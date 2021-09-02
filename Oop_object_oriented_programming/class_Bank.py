class Bank:
    bank_name="sbi"
    def account_creation(self,ac_no,name):
        self.ac_no = ac_no
        self.name=name
        self.minimumbalance=5000
        self.balance=self.minimumbalance
    def deposit(self,amt):
        self.amt=amt
        self.balance += self.amt
        print("your",Bank.bank_name,"account has been credited with amount",self.amt)
        print("your current balance=",self.balance)
    def withdrawal(self,amount):
        self.amount=amount
        if self.amt > self.balance:
            print("insufficient balance")
        else:
            print("account debited with",self.amount)
            self.balance -= self.amount
            print("available balance=",self.balance)
ref=Bank()
num=int(input("enter ac no:"))
ref.account_creation(num,"anu")
ref.deposit(2500)
ref.withdrawal(1500)