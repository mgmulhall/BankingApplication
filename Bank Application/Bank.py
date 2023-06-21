#Maggie Mulhall
#Banking Application 
#Program Abilities:
#     1. Open an account
#     2. Get account information and balance
#     3. Change PIN
#     4. Deposit money in account
#     5. Transfer money between accounts
#     6. Withdraw money from account
#     7. ATM withdrawal
#     8. Deposit change
#     9. Close an account
#     10. Add monthly interest to all accounts


#Initializations
import random
import math
from pydoc import *

#Account class
class Account:

    #Initialize object
    def __init__(self, F_Name,L_Name,social,pin,balance,account_number):
       
       #Set attributes
        balance=int(balance)
        self.F_Name=F_Name
        self.L_Name=L_Name
        self.social=social
        self.pin=pin 
        self.balance = balance
        self.account_number = account_number
    
   #Getter and setter methods
    '''
   Getter methods:
    Input: None
    Output: Attribute
   Setter methods:
    Input: Attribute
    Output: None''' 
    def get_F_Name(self):
        return self.F_Name
    def set_F_Name(self,F_Name):
        self.F_Name=F_Name
    def get_L_Name(self):
        return self.L_Name
    def set_L_Name(self,L_Name):
        self.L_Name=L_Name
    def get_social(self):
        return self.social
    def set_social(self,social):
        self.social=social
    def get_pin(self):
        return self.pin
    def set_pin(self,pin):
        self.pin=pin
    def set_account_number(self,account_number):
        self.accountNum=account_number
    def get_account_number(self):
        return self.account_number
    def set_balance(self,balance):
        self.balance=balance
    def get_balance(self):
        return self.balance
    def get_social_protected(self):
        social=self.get_social()
        l=social[8]
        m=social[7]
        k=social[6]
        g=social[5]
        self.social_protected="XXX-XX-"+g+k+m+l
        return self.social_protected

    #Validate pin number
    def isValidPIN(self,entered_pin):
        '''This method validates an accounts pin number
        Input: pin
        Output: True or False'''
        if entered_pin==self.get_pin():
            return True
        else: 
            return False
    
    #Deposit money into account instance
    def deposit(self,deposit_amount):
        '''This method deposits money into an account
        Input: Amount to deposit
        Output: Updated account balance'''
        new_balance=int(self.get_balance()+deposit_amount)
        self.set_balance(new_balance)
        return new_balance
    
    #Withdraw money from account instance
    def withdraw(self,withdraw_amount):
        '''This method withdraws money from an account
        Input: withdrawal amount
        Output: updated account balance'''
        new_balance=int(self.get_balance()-withdraw_amount)
        self.set_balance(new_balance)
        return new_balance
    
    #Display account instance info
    def toString(self):
        self.get_social_protected()
        formatted_bal=(self.balance / 100)
        formatted_bal="{:,}".format(formatted_bal)
        return f"\nAccount Number: {self.account_number}\nOwner First Name: {self.F_Name}\nOwner Last Name: {self.L_Name}\nOwner SSN: {self.social_protected}\nPIN: {self.pin}\nBalance: ${formatted_bal}"

#Bank Manager class
class BankManager:
    
    #Initialize object
    def __init__(self):
        self.bank = Bank()

    #Main function
    def main(self):
        '''This function is the main loop that continuously asks for choice until exited out
    Input: N/A
    Output: N/A    '''
        choice=0
        while True:
            if choice=="11":
                print("Closing Bank... Thanks!")
                break
            else:
                choice=self.display_options()
                self.eval_choice(choice)
                continue
    
    def display_options(self):
        '''This function displays options and accepts option choice'''
        print('''\nWhat do you want to do?
    1. Open an account
    2. Get account information and balance
    3. Change PIN
    4. Deposit money in account
    5. Transfer money between accounts
    6. Withdraw money from account
    7. ATM withdrawal
    8. Deposit change
    9. Close an account
    10. Add monthly interest to all accounts
    11. End Program''')
        choice=input('Enter your choice number: ')
        return choice
    
    #Preform transactions based on choice
    def eval_choice(self,choice):
        '''This method evaluates transactions
        Input: Transaction choice
        Output: N/A'''
        
        #Open an account
        if choice=="1":
            accounts=self.bank.get_accounts()
            #Determine if the bank can hold another account
            if None in accounts:
                Bank.setup_Account(self.bank)
            else:
                print("\nBank is full and can't hold any more accounts :(")
        
        #Get account information
        elif choice=="2":
            #First, verify account number and pin
            foundAcct=self.promptForAccountNumberAndPIN()
            if foundAcct!="-1":
                print(foundAcct.toString())
        
        #Change pin
        elif choice=="3":
            #First, verify account number and pin
            foundAcct=self.promptForAccountNumberAndPIN()
            
            #If account is validated, prompt for new pin, confirm and change it
            if foundAcct!="-1":
                while True:
                    newPin=input("Enter your new PIN: ")
                    if (len(newPin) == 4 and newPin.isdigit() == True):
                        newPinConfirmed=input("Confirm new pin: ")
                        if newPin==newPinConfirmed:
                            foundAcct.set_pin(newPin)
                            print("\nPIN updated")
                            break
                        else:
                            print("PIN's don't match. \n Try Again.")
                            continue
                    else:
                        print("Invalid Entry, PIN not changed. Try Again.")
        
        #Deposit transaction
        elif choice=="4":
            #First, verify account number and pin
            foundAcct=self.promptForAccountNumberAndPIN()
            if foundAcct!="-1":
                while True:
                    while True:
                        try:
                            #Prompt for/validate deposit amount
                            deposit_amount_float=float(input("How much would you like to deposit (ex. 50.31)? "))
                            #new="{:.2f}".format(deposit_amount_float)
                            break
                        except ValueError:
                            print("Invalid Input. Try Again.")
                            continue
                    #if amount entered is positive
                    #Deposit amount in cents to the account
                    #Display balance to user
                    if float(deposit_amount_float)>0:
                        deposit=BankUtility.convertFromDollarsToCents(float(deposit_amount_float))
                        new_balance_display=(foundAcct.deposit(deposit)/100)
                        new_balance_display="{:,}".format(new_balance_display)
                        print("Success!\nCurrent account balance after deposit: $",new_balance_display)
                        break
                    else:
                        print("Amount cannot be negative. Try Again.")
                        continue
        
        #Transfer
        elif choice=="5":
            #Prompt for/validate first account
            print("\nAcount to transfer from:")
            from_account=self.promptForAccountNumberAndPIN()
            if from_account!="-1":
                #Prompt for/validate second account
                print("\nAccount to transfer to:")
                to_account=self.promptForAccountNumberAndPIN()
                if to_account!="-1":
                    while True:
                        try:
                            #Prompt for/validate transfer amount
                            amount=float(input("\nHow much would you like to transfer? (ex 50.00) :"))
                            internal_amount=BankUtility.convertFromDollarsToCents(amount)
                            if from_account.get_balance()<=internal_amount:
                                print("This would result in insufficient funds. Try Again.")
                                continue
                            break
                        except ValueError:
                            print("Invalid Input. Try Again.")
                            continue
                        
                    #Make deposit and display results
                    from_account.withdraw(internal_amount)
                    to_account.deposit(internal_amount)
                    amount="{:,}".format(amount)
                    from_bal=(from_account.get_balance()/100)
                    from_bal="{:,}".format(from_bal)
                    to_bal=(to_account.get_balance()/100)
                    to_bal="{:,}".format(to_bal)

                    print("\nAmount transfered: $",amount)
                    print("\nOrigin account balance: $",(from_bal))
                    print("Destination account balance: $",(to_bal))
        
        #withdrawal 
        elif choice=="6":
            #Prompt for/validate account
            foundAcct=self.promptForAccountNumberAndPIN()
            if foundAcct!="-1":
                while True:
                        try:
                            #Prompt for/validate withdraw amount
                            withdraw_amount=float(input("How much would you like to withdraw? "))
                            withdraw_amount_internal=BankUtility.convertFromDollarsToCents(withdraw_amount)
                            if withdraw_amount_internal>=foundAcct.get_balance():
                                print("This would result in insufficient funds. Try Again.")
                                continue
                            elif withdraw_amount_internal<=0:
                                print("Amount needs to be positive. Try Again.")
                                continue
                            else:
                                #Make withdraw and display results
                                new_balance_internal=foundAcct.withdraw(withdraw_amount_internal)
                                new_balance=(new_balance_internal/100)
                                new_balance="{:,}".format(new_balance)
                                print("Updated balance: $",new_balance)
                                break
                        except ValueError:
                            print("Invalid Input. Try Again.")
                            continue
             
        #ATM withdrawal
        elif choice=="7":
            #Prompt for/validate account
            foundAcct=self.promptForAccountNumberAndPIN()
            if foundAcct!="-1":
                while True:
                        try:
                            #Prompt for/validate input amount to withdraw
                            ATM_amount=int(input("\n Multiples of $5\n Max amount: $1,000\nHow much would you like to withdraw? (ex. 25) :"))
                            if ATM_amount<5 or ATM_amount>1000 or ATM_amount%5!=0:
                                print("Invalid Amount. Try Again.")
                                continue
                            
                            #Validate amount requested is in the account
                            internal_ATM_amount=BankUtility.convertFromDollarsToCents(ATM_amount)
                            if internal_ATM_amount>=(foundAcct.get_balance()):
                                print("This would result in insufficient funds. Try Again.")
                                continue

                            #Make withdrawal and display results
                            foundAcct.withdraw(internal_ATM_amount)
                            twenties=(math.trunc(ATM_amount/20))
                            remainder=ATM_amount-(twenties*20)
                            tens=(math.trunc(remainder/10))
                            remainder=remainder-(tens*10)
                            fives=(math.trunc(remainder/5))
                            ATM_amount="{:,}".format(ATM_amount)
                            balance=foundAcct.get_balance()/100
                            balance="{:,}".format(balance)
                            print("\nATM withdrawal made for $",ATM_amount)
                            print("Number of 20 dollar bills: ",twenties)
                            print("Number of 10 dollar bills: ",tens)
                            print("Number of 5 dollar bills: ",fives)
                            print("Remaining account balance: $",balance)
                            break
                        except ValueError:
                            print("Invalid Input. Try Again.")
                            continue
                        
        #Deposit change           
        elif choice=="8":

            #Initialize instance of coin collector class
            collector=CoinCollector()
            #Prompt for/validate account
            foundAcct=self.promptForAccountNumberAndPIN()
            if foundAcct!="-1":
                print('''
o ‘P’ represents a penny (1 cent)
o ‘N’ represents a nickel (5 cents)
o ‘D’ represents a dime (10 cents)
o ‘Q’ represents a quarter (25 cents)
o ‘H’ represents a half-dollar (50 cents)
o ‘W’ represents a whole dollar (100 cents)''')
                
                #Accept input and make deposit
                deposit=input("Please enter in your coins (ex PNDQHW) : ")
                amountInCents=collector.parseChange(deposit)
                amountInDollars=amountInCents/100
                foundAcct.deposit(amountInCents)
                balance=foundAcct.get_balance()/100
                balance="{:,}".format(balance)
                print("\nSuccessfully deposited $",amountInDollars)
                print("Current balance: $",balance)
        
        #Close account
        elif choice=="9":
            #Prompt for/validate account
            foundAcct=self.promptForAccountNumberAndPIN()
            if foundAcct!="-1":
                self.bank.removeAccountFromBank(foundAcct)

        #Monthly interest       
        elif choice=="10":
            while True:
                try:
                    #Prompt for/validate interest rate
                    annual_rate=(float(input("\nPlease enter an annual interest rate (enter 2.75 for 2.75%): ")))/100
                    if annual_rate>0 and annual_rate<=100:
                        #Deposit/ track interest
                        intrest_array=[]
                        for account in self.bank.accounts:
                            if account != None:
                                intrest=((float(account.get_balance())*(annual_rate/12))/100)
                                intrest_array.append(intrest)

                        accounts=self.bank.addMonthlyInterest(annual_rate)
                        break
                    else:
                        print("Interest must 0-100. Try Again.")
                except ValueError:
                    print("Invalid Input. Try Again.")
                    continue
            
            #Display updated acount balances
            i=0
            for account in accounts:
                
                if account != None:
                    intrest=intrest_array[i]
                    formatted_intrest="{:.2f}".format(intrest)
                    formatted_intrest="{:,}".format(float(formatted_intrest))
                    balance=(account.get_balance()/100)
                    balance="{:,}".format(balance)
                    i+=1
                    print("\nInterest added for one month!")
                    print("$",formatted_intrest," added to account ",account.get_account_number(),"\n Balance after deposit: $",balance)
                
    def promptForAccountNumberAndPIN(self):
        '''This method prompts for and validates accounts and their pins
        Input: none
        Output: account or -1'''
        entered_accNum=input("\nWhat is your account number? ")
        foundAcct=self.bank.findAccount(entered_accNum)
        if foundAcct=="-1":
            print("Account not found for account number: ",entered_accNum)
            return "-1"
        else:
            entered_pin=input("Found the account! What's your pin? ")
            correctPin=Account.isValidPIN(foundAcct,entered_pin)
            if correctPin==True:
                return foundAcct
            else:
                print("Invalid PIN")
                return "-1"

#Bank Class
class Bank:
    def __init__(self):
        self.accounts = [None] * 100

    #Setup new accounts 
    def setup_Account(self):
        print("\nLets open you an account!")
        while True:
            F_Name=input("What's your first name? ")
            if len(F_Name)==0:
                print("You must enter a first name.\n")
                continue
            else:
                break
        while True:
            L_Name=input("What's your last name? ")
            if len(L_Name)==0:
                print("You must enter a last name.\n")
                continue
            else:
                break
        while True:
            social=input("What's your social security number? (no dashes) ")
            if social.isdigit() and len(social)==9:
                break
            else:
                print("Social Security must be 9 digit number, no dashes. Try Again.\n")
        pin=str(BankUtility.generateRandomInteger(1000,9999))
        while True:
            try:
                balance_dollars=float(input("How much money are you opening with (ex 2225.95)?: "))
                balance=BankUtility.convertFromDollarsToCents(balance_dollars)
                break
            except ValueError:
                print("Invalid Input. Try Again.\n")
                continue
        while True:
            accountNum=str(BankUtility.generateRandomInteger(10000000,99999999))
            if accountNum in self.accounts:
                continue
            else:
                break
        new=Account(F_Name,L_Name,social,pin,balance,str(accountNum))
        self.addAccountToBank(new)
        print("Success! Congratulations on your new account! ")
        print(new.toString())
    
    #Add acount to bank account array
    def addAccountToBank(self,new):
        '''This method adds accounts to the bank account array
        Input: New account
        Output: True or False'''
        for i in range(len(self.accounts)):
            if self.accounts[i] is None:
                self.accounts[i] = new
                return True
        print("No more accounts available")
        return False

    #Remove account
    def removeAccountFromBank(self,account):
        '''This method removes accounts from the bank
        Input: Account
        Output: True or False'''
        for i in range(len(self.accounts)):
            if self.accounts[i] is not None and self.accounts[i] == account:
                self.accounts[i] = None
                print("Account Closed!")
                return True
        print("Account not found")
        return False

    #find account
    def findAccount(self, account_number):
        '''This method finds accounts by account number
        Input: Account number
        Output: Account object or -1 '''
        for account in self.accounts:
            if (account is not None) and (account.get_account_number() == account_number):
                return account
        return "-1"
    
    #Get all accounts
    def get_accounts(self):
        '''This method returns the array of account in the bank'''
        return self.accounts
    
    #Add interest
    def addMonthlyInterest(self,annual_rate):
        '''This method adds monthly interest to all accounts
        Input: Annual interest rate
        Output: Array of accounts'''
        monthly_rate=(annual_rate/12)
        accounts=self.get_accounts()
        for account in accounts:
            if account != None:
                balance=account.get_balance()
                intrest=balance*monthly_rate
                account.deposit(intrest)
        return accounts

#Bank Utility class
class BankUtility:
         
    #Check if string is numeric 
    def isNumeric(numberToCheck):
        '''This function checks if an inputted string is a digit
        Input: String
        Output: True or False'''
        
        try:
            if numberToCheck.isdigit():
                return True
            else:
                return False
        except ValueError:
            return False
        
    #Convert dollar amounts to cents
    def convertFromDollarsToCents(dollars):
        '''This function converts dollars to cents 
        Input: Amount in dollars
        Output: Amount in cents'''
        try:
            cents=dollars*100
            return cents
        except ValueError:
            return False
        
    #Random number generator
    def generateRandomInteger(min,max):
        '''This function generates random numbers
        Input: Range
        Output: Random number in the range'''
        random_num=random.randint(min,max)
        return random_num

#Coin collector class
class CoinCollector:
    def __init__(self):
        ""

    #Deposit change
    def parseChange(self,stringOfCoins):
        '''This function is used to deposit coins into an account
        Input: String of coins
        Output: Amount deposited in cents'''

        amountInCents=0
        while True:
            for i in stringOfCoins:
                if i=="P":
                    amountInCents+=1
                elif i=="N":
                    amountInCents+=5
                elif i=="D":
                    amountInCents+=10
                elif i=="Q":
                    amountInCents+=25
                elif i=="H":
                    amountInCents+=50
                elif i=="W":
                    amountInCents+=100
                else:
                    print("\nInvalid Entry: ",i)
            break
        return amountInCents

#Call main Bank Manager function
if __name__ == "__main__":
    manager=BankManager()
    print("\nWelcome to the bank! You have so many options!\n *Note: Bank will round amounts when required")
    manager.main()