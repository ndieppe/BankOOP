import random; import datetime
class bank:
    def __init__(self, balance, transactions):
        self.balance = balance
        self.transactions = transactions

    def __str__(self):
        return f"Your remaining balance is £{self.balance}"
    
    def intrestcalc(self):
        intrest = random.uniform(1,3.25)
        newbal = self.balance * (1 + (intrest/100)) ** 12
        return f"Your balance in a year will aproximately be £{newbal:.2f}"
    
    def withdraw(self):
        WithdrawVal = 0
        while WithdrawVal <= 0 or WithdrawVal > self.balance:
            try:
                WithdrawVal = float(input("Please enter an amount of money you would like to withdraw: "))
            except:
                print("Your failed to enter a valid amount, please try again: ")
        self.balance = self.balance - WithdrawVal
        time = datetime.datetime.now()
        timedisplay = time.strftime("%x") + " " + time.strftime("%X")
        self.transactions.update({f"-£{WithdrawVal:.2f}": timedisplay})
        return f"You successfully withdrew £{WithdrawVal}, your new balance is £{self.balance:.2f}"

    
    def deposit(self):
        deposit = 0
        while deposit <= 0:
            try:
                deposit = float(input("Please enter an amount of money you would like to deposit: "))
            except:
                print("Your failed to enter a valid amount, please try again: ")
        self.balance += deposit

        time = datetime.datetime.now()
        timedisplay = time.strftime("%x") + " " + time.strftime("%X")
        self.transactions.update({f"+£{deposit:.2f}": timedisplay})

        return f"You successfully deposited £{deposit}, your new balance is £{self.balance:.2f}"
    
    
    def viewbalance(self):
        return f"Your current balance is £{self.balance:.2f}"

    def Viewtransactions(self):
        print("************************************************")
        print("Your list of transactions:")
        for key, value in self.transactions.items():
            print(f"{key}  -  {value}")
        print("************************************************")   



def options():
    print(''''
************************************************
    1. Dispaly balance
    2. Withdraw money
    3. Deposit money
    4. Balance prediction (1 year)
    5. View transactions
    5. Exit
************************************************
    ''')
    option = 0
    while option < 1 or option > 6:
        try:
            option = int(input("Enter an option (1-6): "))
        except:
            print("Failed to enter a valid input")
    return option



customer1 = bank(500, {})
def main():
    option = 0
    while option != 5:
        option = options()
        match option:
            case 1:
                print(customer1.viewbalance())
            case 2:
                print(customer1.withdraw())
            case 3:
                print(customer1.deposit())
            case 4:
                print(customer1.intrestcalc())
            case 5:
                print(customer1.Viewtransactions())
            case 6:
                print("Goodbye")
                quit()
    

if __name__ == "__main__":
    main()

