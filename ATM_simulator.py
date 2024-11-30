class ATM_simulator:
    def __init__(self):
        self.users=[["user1",2020,5000],["user2",2024,10000]]
        self.user_varaible=0
        self.l=0
    def sign_in(self):
        a=input("enter your username")
        for i in range(len(self.users)):
            self.user_varaible+=1
            if a in self.users[i]:
                print("you enter corect usename")
                self.l+=1
                b=int(input("now enter pin to proceed"))
                if b==self.users[i][1]:
                    print("you enterd correct pin")
                    self.l+=1
                    break
                else:
                    print("wrong pin")
                    break
        else:
            print("usename is not present in our system")
    def withdraw_money(self):
        if self.l==2:
            c=int(input("how much money you want to withdraw"))
            if c<=self.users[self.user_varaible-1][2]:
                print("your money is withdrawing")
                self.users[self.user_varaible-1][2]-=c
            else:
                print("you dont have this much of balance")
        else:
            print("do sign in first")
    def deposit_amount(self):
        if self.l==2:
            d=int(input("enter how much money you want to add to your balance"))
            self.users[self.user_varaible-1][2]+=d
            print("successfully added money")
        else:
            print("do sign in first")
    def change_pin(self):
        if self.l==2:
            e=int(input("enter new pin "))
            self.users[self.user_varaible-1][1]=e
            print("your pin change successfult")
        else:
            print("do sign in first")

s=ATM_simulator()
s.sign_in()
while True:
    print("\n1. Withdraw Money") 
    print("\n2. Deposit Amount") 
    print("\n3. Change PIN") 
    print("\n4. Exit") 
    choice = int(input("Enter your choice: "))
    if choice == 1:
        s.withdraw_money() 
    elif choice == 2:
        s.deposit_amount()
    elif choice == 3:
        s.change_pin() 
    elif choice == 4:
         print("Exiting. Thank you for using the ATM!") 
         break 
    else: 
         print("Invalid choice. Please try again.")
