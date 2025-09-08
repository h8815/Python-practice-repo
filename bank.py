class Account:
    def __init__(self,bal,acc_no):
        self.acc_no = acc_no 
        self.bal = bal

    def debit(self):
        amt = int(input("Enter amount you want to debit : "))
        if (amt>self.bal):
            print("You cannot withdrawn money more than your balance")
            print("Try again...")
            exit()
        else:
            self.bal = self.bal - amt
            print(f"From account {self.acc_no}\nAmount {amt} debited \nAvailable balance :- {self.bal}")

    def credit(self):
        amt = int(input("Enter amount you want to credit : "))
        self.bal += amt
        print(f"From account {self.acc_no}\nAmount {amt} credited \nBalance :- {self.bal}")

    def balance(self):
        print(f"Account - {self.acc_no}\nBalance :- {self.bal}") 


acc_no = (input("Enter 15 digit account number : "))
if len(acc_no) == 15 :
    balance = 10000
    a1 = Account(balance,acc_no)
    print("What do you want to do ?")
    print("1.Debit money\n2.Credit money\n3.Balance")
    choice = int(input())
    match (choice):
        case 1: a1.debit()
        case 2: a1.credit()
        case 3: a1.balance()
        case _:print("Invalid input");exit() 
else:
    print(f"Please enter 10 digit account number\nYou only enter {len(acc_no)} digit")