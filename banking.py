from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):

    @abstractmethod
    def createAccount():
        return 0

    @abstractmethod
    def authenticate():
        return 0

    @abstractmethod
    def withdraw():
        return 0

    @abstractmethod
    def deposit():
        return 0

    @abstractmethod
    def displayBalance():
        return 0


class SavingsAccount(Account):

    def __init__(self):
        # [key][0] = Name [key][1] = balance
        self.savingsAccount = {}

    def createAccount(self,name,initialDeposit):
        self.accountNumber = randint(10000,99999)
        self.savingsAccount[self.accountNumber] = [name,initialDeposit]
        print("Account number :",self.accountNumber)

    def authenticate(self,name, accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0] == name:
                print("Authentication Successful!")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication Failed!")
                return False
        else:
            print("Authentication Failed!")
            return False

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccount[accountNumber][1]:
            print("Insufficient balance!")
        else:
            self.savingsAccount[self.accountNumber][1] -= withdrawalAmount
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingsAccount[self.accountNumber][1] += depositAmount
        self.displayBalance()

    def displayBalance(self):
        print("Available balance: ", self.savingsAccount[self.accountNumber][1])

savingsAccount = SavingsAccount()
while True:
    print("Enter 1 to create an Account ")
    print("Enter 2 to access an exiting Account ")
    print("Enter 3 to exit ")
    usersChoice = int(input())

    if usersChoice is 1:
        print("Enter the Name ")
        name = input()
        print("Enter the initial deposit amount")
        deposit = int(input())
        savingsAccount.createAccount(name, deposit)
    elif  usersChoice is 2:
        print("Enter the Name ")
        name = input()
        print("Enter the Account number")
        accountNumber = int(input())
        authernticationStatus =  savingsAccount.authenticate(name, accountNumber)
        if authernticationStatus is True:
            while True:
                print("Enter 1 for withdraw")
                print("Enter 2 for deposit")
                print("Enter 3 to diplay the balance")
                print("Enter 4 to go back to the previous menu")
                usersChoice = int(input())
                if  usersChoice is 1:
                    print("Enter the withdrawal Amount")
                    amount = int(input())
                    savingsAccount.withdraw(amount)
                elif usersChoice is 2:
                    print("Enter the deposit Amount")
                    amount = int(input())
                    savingsAccount.deposit(amount)
                elif usersChoice is 3:
                    savingsAccount.displayBalance()
                elif usersChoice is 4:
                    break

    elif usersChoice is 3:
        quit()
    else:
        print("Invalid input..")
