#Creates a unique number to use when creating a new account.
import random

#Used to store each account's Number to verify that we don't have any duplicates.
numbers = []
#Maximum available number.
maxNum = 1000
def newAccountNumber():
    newNumber = random.randint(0,maxNum)
    if len(numbers) == 0:
        numbers.append(newNumber)
        return newNumber
    else:
        for i in range(0, len(numbers) , 1):
            if numbers[i] == newNumber:
                newNumber = random.randint(0,1000)
            else:
                numbers.append(newNumber)
                return newNumber
