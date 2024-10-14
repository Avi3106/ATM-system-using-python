#creating a python program to deposit, withdraw and check the balance of a user..
#defining a class named BankHolder
class BankHolder:
    def __init__(self,acountholder,balance) :
        self.acountholder = acountholder
        self.balance = float(balance) #converting the value to the float
#creating different functions into the same class
#three different functions for each purpose
    def withdraw(self,amount):
        amount= float(amount) #converting the value to the float
        if amount>= self.balance:
            print("not enough credit to withdraw")
        elif amount<=0:
            print("invalid amount")
        else:
            self.balance -= amount
            print(f"the withdrawal of {amount} is successful!!")
            
    def deposit(self,amount):
        amount= float(amount)
        if amount<=0:
            print("cannot deposit less than 1 rs")
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

#creating the options for the user to choose from
while True: #this loop will run until the user choose to exit
    print("please choose an option to move forward")
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")

    #taking the choice of the user..
    user_choice= int(input('enter your choice: '))# in Int format
    
    match user_choice:#using match case function for ease
        
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
            
            
            
            
