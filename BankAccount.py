
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
        
