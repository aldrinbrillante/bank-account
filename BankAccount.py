
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
        #add interest to current balance
        self.balance += interest

##########################################################################################################################################################
# The print_receipt method prints a receipt with the account name, account number, and balance like this:
#Joi Anderson
#Account No.: ****5678
#Routing No.: 98765432
#Balance: $100.00 
##########################################################################################################################################################

    def print_receipt(self):
        account_str = str(self.account_number)


        print(f"Account Name: {self.full_name}")
        print(f"Account Number: ****{account_str[-4:]}")
        print(f"Routing Number:{self.routing_number}")
        print(f"Balance: {self.balance}")

##########################################################################################################################################################
# Outside of the BankAccount class,
# define 3 different bank account examples using the BankAccount() object.
##########################################################################################################################################################

# Account 1
# name = BankAccount("name", account number, routing number, balance)
Aldrin = BankAccount("Aldrin", 1234567, 1111111, 0)
Aldrin.get_balance()
Aldrin.add_interest()
Aldrin.print_receipt()

#insert break for terminal
print("\n")

# Account 2
Vreea = BankAccount("Vreea", 7654321, 1111111, 0)
Vreea.balance = 100
Vreea.withdraw(50)
Vreea.deposit(25)
Vreea.print_receipt()

#insert break for terminal
print("\n")

# Account 3 
Karen = BankAccount("Karen", 1936295, 1111111, 0)
Karen.balance = 500
Karen.withdraw(50)
Karen.deposit(10)
Karen.print_receipt()

#insert break for terminal
print("\n")








