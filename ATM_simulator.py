class ATM_simulator:
    def __init__(self):
        self.users = [["user1", 2020, 5000], ["user2", 2024, 10000]]
        self.user_index = -1
        self.logged_in = False

    def sign_in(self):
        username = input("Enter your username: ")
        for i, user in enumerate(self.users):
            if username == user[0]:
                pin = int(input("Enter your PIN: "))
                if pin == user[1]:
                    print("Login successful.")
                    self.user_index = i
                    self.logged_in = True
                    return
                else:
                    print("Incorrect PIN.")
                    return
        print("Username not found in our system.")

    def check_balance(self):
        if self.logged_in:
            print(f"Your current balance is: ${self.users[self.user_index][2]}")
        else:
            print("Please sign in first.")

    def withdraw_money(self):
        if self.logged_in:
            amount = int(input("How much money do you want to withdraw? "))
            if amount <= self.users[self.user_index][2]:
                print("Your money is being withdrawn.")
                self.users[self.user_index][2] -= amount
                print(f"New balance: ${self.users[self.user_index][2]}")
            else:
                print("Insufficient funds.")
        else:
            print("Please sign in first.")

    def deposit_amount(self):
        if self.logged_in:
            amount = int(input("Enter how much money you want to deposit: "))
            self.users[self.user_index][2] += amount
            print("Successfully added money.")
            print(f"New balance: ${self.users[self.user_index][2]}")
        else:
            print("Please sign in first.")

    def change_pin(self):
        if self.logged_in:
            new_pin = int(input("Enter new PIN: "))
            self.users[self.user_index][1] = new_pin
            print("Your PIN has been changed successfully.")
        else:
            print("Please sign in first.")

s = ATM_simulator()
s.sign_in()

while True:
    print("\n1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Amount")
    print("4. Change PIN")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        s.check_balance()
    elif choice == 2:
        s.withdraw_money()
    elif choice == 3:
        s.deposit_amount()
    elif choice == 4:
        s.change_pin()
    elif choice == 5:
        print("Exiting. Thank you for using the ATM!")
        break
    else:
        print("Invalid choice. Please try again.")
