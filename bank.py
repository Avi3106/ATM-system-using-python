class BankHolder:
    def __init__(self,acountholder,balance) :
        self.acountholder = acountholder
        self.balance = float(balance)
        
    def withdraw(self,amount):
        amount= float(amount)
        if amount>= self.balance:
            print("besharm jitna chadar hai utna hi per pasaro")
        elif amount<=0:
            print("invalid amount")
        else:
            self.balance -= amount
            print(f"the withdrawal of {amount} is successful!!")
            
    def deposit(self,amount):
        amount= float(amount)
        if amount<=0:
            print("1 rs to deposit kr...")
        else:
            self.balance += amount
            print(f"successfuly deposited {amount} rs")
    
    def checkbalance(self):
        print(f"hii {self.acountholder} your balance is: {self.balance}")

print("namaskar!!! welcome to lena dena bank")

print("enter your name to create the account")
name= input('enter your name : ')
balance = input('enter the amount you want to deposit first time: ')
account=BankHolder(name,balance)

while True:
    print("please choose an option to move forward")
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")
    
    user_choice= int(input('enter your choice: '))
    
    match user_choice:
        
        case 1:
            account.checkbalance()
        case 2:
            amount = input('enter the amount you want to deposit: ')
            account.deposit(amount)
        case 3:
            amount = input('enter the amount you want to withdraw: ')
            account.withdraw(amount)
        case 4:
            print("thank you for using lena dena bank")
            exit()
        case _:
            print('enter correct option!')
            
            
            
            
