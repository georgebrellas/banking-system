#  Bank of Kekisan Transaction System v2.2.3
#         Made by @Georgegreece        
#This bank is fictional if it wasn't obvious. 

#Return Codes:
#0 = Success
#1 = Not a Number
#2 = Number Bellow Zero
#3 = Not Enough Money
#4 = Account Not Found
#5 = Account Equals Current Account
#6 = Account number not a number
#7 = Pin length not 4
#8 = Incorrect Pin
#9 = Unexpected Error (AKA this shouldn't be happening)

from NumberCheck import *
from AccountNumberGenerator import *
from time import localtime, strftime
import random
import math
import os
import pickle
import hashlib

#The filename used to store the accounts.
AccFile = "Accounts"

#A dictionary for the accounts.
Accounts = {}

#Data management/maintenance functions
def save():
    f = open(AccFile + ".pkl", "wb")
    pickle.dump(Accounts, f, pickle.HIGHEST_PROTOCOL)

def load():
    global Accounts
    f = open(AccFile + ".pkl", "rb")
    Accounts = pickle.load(f)

def clear():
    global Accounts
    Accounts = {}
    try:
        os.remove(AccFile + ".pkl")
    except FileNotFoundError:
        return

#Assigns a new hashed pin to an account.
def newPin(Pin,Account):
    Account = findAccount(Account)
    Accounts[Account].pin = hashPin(Pin)
    return 0

#Hashes the pin with sha256 and returns the hash
def hashPin(Pin):
    Pin = str.encode(str(Pin))
    P = hashlib.sha256()
    P.update(Pin)
    return P.digest()

def login(Acc, Pin):
    Pin = hashPin(Pin)
    Acc = findAccount(Acc)
    if Accounts[Acc].pin == Pin:
        return 0
    else:
        return 8


def maintenanceLogin():
    return

#Easier to use info function.
def info(Account):
    if not is_number(Account):
        return Accounts[Account].info()
    else:
        return Accounts[findAccount(Account)].info()
#Clears the user's log
    
def clearLog(Account):
    if not is_number(Account):
        Accounts[Account].clearLog()
        return 0
    else:
        Accounts[findAccount(Account)].clearLog()
        return 0

#Simple way to access an account
def getAccount(Number):
    return Accounts[findAccount(Number)]

#Find an account's dictionary name from his number.
def findAccount(Number):
    Found = 0
    if not is_number(Number):
        return 6
    for i in range(1, len(Accounts)+1,1):
        if int(Number) == Accounts["p" + str(i)].number:
            Found = 1
            AccountNum = i
        if i == len(Accounts) and Found == 0:
            return 4
    return "p" + str(AccountNum)

#Easier to use deposit and withdraw functions.
def deposit(Account, Money):
    try:
        Response = Accounts[Account].deposit(Money)
    except KeyError:
        print("ERROR: Account does not exist?!")
        return
    if Response == 0:
        print("Success!")
    elif Response == 1:
        print("Error: Value not a number.")
    elif Response == 2:
        print ("Error: Value bellow zero.")
        
def withdraw(Account, Money):
    try:
        Response = Accounts[Account].withdraw(Money)
    except KeyError:
        print("ERROR: Account does not exist?!")
        return
    if Response == 0:
        print("Success!")
    elif Response == 1:
        print("Error: Value not a number.")
    elif Response == 2:
        print ("Error: Value bellow zero.")
    elif Response == 3:
        print ("Error: Not enough money.")
    else:
        print("Error: WTF?")
        
#Way easier to use transfer function.
def transfer(Transferer, Transferee , Amount):
    Transferer = findAccount(Transferer)
    Transferee = findAccount(Transferee)
    return Accounts[Transferer].transfer(Transferee, Amount)

#Account Creator
def newAccount(name,money,pin):
    if len(str(pin)) != 4:
        return 7
    varName = "p" + str(len(Accounts) + 1)
    name = str(name)
    pin = hashPin(pin)
    Accounts[varName] = Person(name, newAccountNumber(), money, pin)
    
    
#Our Account manager.
class Person:
    def __init__(self,name,number,money,pin):
        global  numOfUsers
        self.id = len(Accounts) + 1
        self.name = name
        self.number = number
        self.money = money
        self.pin = pin
        self.log = {}
    def info(self):
        number = self.number
        holder = self.name
        money = self.money
        return number,holder,money
    def withdraw(self, WithdrawalAmount):
        if not is_number(WithdrawalAmount):
            return 1
        elif int(WithdrawalAmount) <= 0:
            return 2
        elif int(WithdrawalAmount) > self.money:
            return 3
        self.money = self.money - int(WithdrawalAmount)
        return 0
        #IDK what to do with this yet, so it's staying.
        #print("Successfully withdrew $" + str(WithdrawalAmmount) + " from account number: " + str(self.number))
        
    def deposit(self, DepositAmount):
        if not is_number(DepositAmount):
            return 1
        if int(DepositAmount) <= 0:
            return 2
        self.money = self.money + int(DepositAmount)
        self.saveLog(DepositAmount,"d","")
        #See above.
        #print("Successfully deposited $" + str(DepositAmmount) + " to account number: " + str(self.number))

    def transfer(self,TransferTo,TransferAmount):
        if not is_number(TransferAmount):
            return 1
        elif int(TransferAmount) <= 0:
            return 2
        elif int(TransferAmount) > self.money:
            return 3
        else:
            Accounts[TransferTo].money += int(TransferAmount)
            self.money -= int(TransferAmount)
            self.saveLog(TransferAmount,"t", TransferTo)
            return 0
        
    def saveLog(self,money,action,accTo):
        sysTime = strftime("%Y-%m-%d %H:%M:%S", localtime())
        logTime = strftime("%Y-%m-%d-%H:%M", localtime())
        if action == "d":
            log = str(sysTime) + ": Deposited $" + str(money)
            self.log[logTime] = log
            return 0
        
        elif action == "w":
            log = str(sysTime) + ": Withdrew $" + str(money)
            self.log[logTime] = log
            return 0
        
        elif action == "t":
            log = str(sysTime) + ": Transfered $" + str(money) + " to " + str(Accounts[accTo].name) + "(" + str(Accounts[accTo].number) + ")"
            self.log[logTime] = log
            return 0
        else:
            print("Unknown action!? Please don't mess with me <3")
            return 9
        
    def clearLog(self):
        self.log = {}
        return 0
        
#Test accounts. Can be safely deleted.
#Accounts["p1"] = Person("Bank",0,50,1111)
#Accounts["p2"] = Person("Stud",1,10,1111)
