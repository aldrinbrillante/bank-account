from random import randint


#define a BankAccount class
class BankAccount:

    routing_number = 123456789 

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

    #define print_receipt function
    def print_receipt(self):
        account_str = str(self.account_number)

        print(f"Account Name: {self.full_name}")
        print(f"Account Number: ****{account_str[-4:]}") #i do bracket '-4' to subtract the 4 asterisk i placed prior to account string
        print(f"Routing Number:{self.routing_number}")
        print(f"Balance: {self.balance}")


#randint for random deigit generator for account number 
def random_AccNum():
    """random 8 digit account number generator"""
    acc_Num = ""
    for i in range(8):
        acc_Num += str(randint(0, 9))
    return int(acc_Num)

##########################################################################################################################################################
# Outside of the BankAccount class,
# define 3 different bank account examples using the BankAccount() object.
##########################################################################################################################################################

# Account 1
# name = BankAccount("name", account number, routing number, 0)
Aldrin = BankAccount("Aldrin", random_AccNum(), 1111111, 0)
Aldrin.balance = 1000
Aldrin.withdraw(500)
Aldrin.deposit(25)
Aldrin.print_receipt()

#insert break for terminal
print("\n")

# Account 2
Vreea = BankAccount("Vreea", random_AccNum(), 1111111, 0)
Vreea.balance = 100
Vreea.withdraw(50)
Vreea.deposit(25)
Vreea.print_receipt()

#insert break for terminal
print("\n")

# Account 3 
Karen = BankAccount("Karen", random_AccNum(), 1111111, 0)
Karen.balance = 500
Karen.withdraw(50)
Karen.deposit(10)
Karen.print_receipt()

#insert break for terminal
print("\n")


# Bank ATM ~ Stretch Challenge 
# Create a terminal ATM. Be sure to add a method to charge an ATM fee for withdrawing money.

while True:

    print("Welcome to Bank ATM")
    # print()
    action = input("Select Action: (1) Get Balance. (2) Deposit. (3) Withdraw. ")
    
    if action == str(1):
        print (Vreea.print_receipt())

    elif action == str(2):
    
        deposit = input("Please enter your amount to deposit: ")
        print (Vreea.deposit (int(deposit)))

    elif action == str(3):

        withdraw = input("Please enter your amount to withdraw (Fee is ): ")
        print (Vreea.withdraw (int(withdraw)))

    elif action == "Exit":
        pass

    else:
            print("Please select one of the following options")







