
#define a BankAccount class
class BankAccount:
    #required attributes
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = 0

##########################################################################################################################################################
# Define the following methods for the BankAccount class:
##########################################################################################################################################################


##########################################################################################################################################################
# The 'deposit' method will take one parameter amount and will add amount to the balance. Will print the message: "Amount Deposited: $X.XX"
##########################################################################################################################################################

    def deposit(self, amount):
        #add amount to balance
        self.balance += amount
        print(f"Amount Deposited: ${amount}")

##########################################################################################################################################################
# The withdraw method will take one parameter amount and will subtract amount from the balance.
# Also, it will print a message, like “Amount Withdrawn: $X.XX”.
# If the user tries to withdraw an amount that is greater than the current balance, print ”Insufficient funds.”
# and charge them with an overdraft fee of $10
##########################################################################################################################################################

    #withdraw function
    def withdraw(self, amount):
        #subtract amount from the balance
        self.balance -= amount
        #print message "amount withdrawn: "$x.xx"
        print(f"Amount Withdrawn: ${amount}")
        #If the user tries to withdraw an amount that is greater than the current balance, print ”Insufficient funds.”
        #and charge them with an overdraft fee of $10
        if amount > self.balance:
            print("Insufficient funds")
            self.balance -= 10

##########################################################################################################################################################
# The get_balance method will print a user-friendly message with the account balance and then also return the current balance of the account.
##########################################################################################################################################################

    #get_balance function
    def get_balance(self):
        #print user-friendly message + return account balance
        print(f"Your current balance is: ${self.balance}")
        return self.balance

##########################################################################################################################################################
# The add_interest method adds interest to the users balance.
# The annual interest rate is 1% (i.e. 0.083% per month).
# Thus, the monthly interest is calculated by the following equation: interest = balance *  0.00083 
##########################################################################################################################################################

    #add_interest function
    def add_interest(self):
        balance = self.balance
        #monthly interest calculation: interest = balance *  0.00083 
        interest = balance *  0.00083 



