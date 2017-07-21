### Bank Transaction System v2.2.3 ###
**Made by @Georgegreece**
This System was made as a fun little side project and it's still just that.
It has many features already and more will come.
The account information is saved locally, as the idea is for this program
to be used in ATMs or something similar.
##### Accounts #####
Each account is stored in the `Accounts` dictionary.
The accounts' dictionary names are stored using  `p` and their unique `ID`
For example the first user would be `p1`, second user would be `p2` etc.

Each account has a unique *Transaction Number* used for money transfers.
The *Transaction Number* is created by the `newAccountNumber()` function.
We create the accounts using our `Person()` class.
Example:
```python
Accounts["p1"] = Person("John D.", newAccountNumber(), 0)
```
Also, each account has a `log` dictionary where it stores it's logs.
The logs are stored with the `YEAR-MONTH-DAY-HOUR:MINUTE` format.
Example:
```python
print(Accounts["p1"].log["2017-07-21-15:32"])
```
This should return the exact transaction that happened on that date and time.
The program uses the `saveLog()` function.
It is not recommended to save manually unless implementing a new feature.
But here it is:
Function `saveLog(money,action,accTo)`
Example:
```python
Accounts["p1"].saveLog(444,"t",221)
```
Saves a transaction log depending on the specified `action`
```
"d" = Deposit
"t" = Transfer
"w" = Withdraw
```
*Note: Only transfers need the accTo, for everything else just send an empty string*
# Functions #
##### Return Codes #####
Return codes are an important way of knowing what happened in the program.
Here's a list of the codes and what they mean.
You can also find the codes on the top of the `Bank.py` file.
```
0 = Success
1 = Not A Number
2 = Number Bellow Zero
3 = Not Enough Money
4 = Account Not Found
5 = Account Equals Current Account
6 = Account Number Not A Number
7 = Pin Length Not 4
8 = Incorrect Pin
9 = Unexpected Error (AKA this shouldn't be happening)
```
### Account Operations ###

##### Creating a New Account #####
Function:
`newAccount(Name, Money, Pin)`

Example:
```python
newAccount("John D.", 55, 1234)
```
Adds an account to the dictionary with the name `John D.` , current money `$55` and a PIN of `1234` (Hashed)

##### Finding an Account #####
Function:
`findAccount(Number)` 

Example:
```python
findAccount(554)
```
Returns the account's dictionary name.

##### Getting an Account #####
Function:
`getAccount(Number)` 

Example:
```python
getAccount(554)
```
Returns the account for simple function usage.

##### Getting an Account's Information #####
*Note: You can use either the Dictionary Name or the Account's Number*
Function:
`info(Account)`

Example:
```python
info(554)
info("p1")
```
Returns the account's `Number`, `Holder` and `Money`

##### Clearing the logs #####
Function:
`clearLog(Account)` 

Example:
```python
clearLog(554)
```
Clears the account's Logs.
### Money Operations ###

##### Depositing Money #####
Function:
`deposit(Account, Money)`

Example:
```python
deposit("p1", 555)
```
Deposits `$555` to the account with a dictionary name of `p1`
##### Withdrawing Money #####
Function:
`withdraw(Account, Money)`

Example:
```python
withdraw("p1", 555)
```
Withdraws `$555` from the account with a dictionary name of `p1`

##### Transfering Money #####
Function:
`transfer(Transferer, Transferee, Amount)`

Example:
```python
transfer(554,315,50)
```
Transfers `$50` from the Account `554` to the account `315`

### Maintenance Operations ###

##### Saving and Loading the Accounts #####
Function:
`save()`
Saves the Accounts dictionary to a `.pkl` file. Change the `AccFile` variable to change the filename.

Function:
`load()`
Loads the Accounts dictionary from the above file.

##### Deleting all Accounts #####
Function:
`clear()`
Empties the Accounts dictionary and deletes the save file.

##### Maintenance Console #####
Function:
`maintenanceLogin()`
Logs into the Maintenance Console (Not implemented yet.)

### PIN Operations ###

##### Logging in #####
Function:
`login(Acc, Pin)`

Example:
```python
login(554, 1234)
```
Checks if the inputted PIN equals the Account's Pin.

##### Changing PIN #####
Function:
`newPin(Pin, Account)`

Example:
```python
transfer(1234, 443)
```
Sets Account's `443` PIN to `1234` (Hashed)

##### Hashing PINs #####
Function:
`hashPin(Pin)`

Example:
```python
hashPin(1234)
```
Hashes the PIN `1234` and returns the hash.
