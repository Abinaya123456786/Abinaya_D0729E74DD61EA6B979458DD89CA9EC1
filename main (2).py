

 
class BankAccount:
    def __init__(self,no,name,bal=0.0):
        self.__acc_no=no
        self.__acc_hold_name=name
        self.__acc_bal=bal

    def deposit(self,amount):
        if amount>0:
            self.__acc_bal+=amount
            print("Deposited Rs.{}. New Balance: Rs.{}".format(amount,self.__acc_bal))
        else:
            print("Invalid deposit amount. Please deposit a positive amount")

    def withdraw(self,amount):
        if amount>0 and amount<=self.__acc_bal:
            self.__acc_bal-=amount
            print("Withdrew Rs.{}. New Balance: Rs.{}".format(amount,self.__acc_bal))
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def disp_bal(self):
        print("Account balance for {} (Account #{}): Rs.{}".format(self.__acc_hold_name,self.__acc_no,self.__acc_bal))

#Creating bank account object
no=input("Enter account number....")
name=input("Enter the account holder name....")
bal=int(input("Enter the initial balance...."))
ba=BankAccount(no,name,bal=5000)
ba.disp_bal()
ba.deposit(int(input("Enter the amount to be deposited....")))
ba.withdraw(int(input("Enter the amount to be withdrawn....")))
ba.disp_bal()