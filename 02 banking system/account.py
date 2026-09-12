
class Account():
    def __init__(self, name, age:int, email:str, password:str, bank:str=None, money:int=0):
        self.name = name.strip().title()
        self.age = age
        self.email = email.strip().title()
        self.bank = bank
        self.money = money
        self.password = password
        
    def change(self):
        print(f"\nChange...\n")
        print(f"    1. Name")
        print(f"    2. Age")
        print(f"    3. Email")
        print(f"    4. Password\n")
        
        choice = int(input("Your choice: "))
        
        match choice:
            case 1:
                print(f"\nChange Name...\n")
                new_name = input("    Enter a Your new Name: ").strip().title()
                
                if new_name != self.name:
                    self.name = new_name
                    print(f"\n    Name successfully changed. Changed the Name to: '{self.name}'")
                else:
                    print(f"\n    You cannot exchange it for the same thing.")
                return self
            
            case 2:    
                print(f"\nChange age...\n")
                new_age = int(input("    Enter a Your new Age: "))
                
                if new_age != self.age:
                    self.age = new_age
                    print(f"\n    Age successfully changed. Changed the Age to: '{self.age}'")
                else:
                    print(f"\n    You cannot exchange it for the same thing.")
                return self                
            
            case 3:
                print(f"\nChange email...\n")
                new_email = int(input("    Enter a Your new email: ")).strip().title()
                
                if new_email != self.email:
                    self.email = new_email
                    print(f"\n    Email successfully changed. Changed the Email to: '{self.email}'")
                else:
                    print(f"\n    You cannot exchange it for the same thing.")
                return self
                
            case 4:
                print(f"\nChange Password...\n")
                password = input("    Enter a Your Password: ").strip()
                
                if password == self.password:
                    new_password = str(input("    Enter a new Password: ")).strip()
                    if new_password != self.password:
                        self.password = new_password
                        print(f"\n    Password successfully changed. Changed the password to: {'*' * len(self.password)}")
                    else:
                        print(f"\n    You cannot exchange it for the same thing.")
                else:
                    print(f"    Incorrect Password\n"
                          f"    1. Unknow Password")
                    choice = input("    ")
                    if choice == '1':
                        new_password = input("    Enter a new Password: ").strip()
                        if new_password != self.password:
                            self.password = new_password
                            print(f"\n    Password successfully changed. Changed the password to: {'*' * len(self.password)}")
                        else:
                            print(f"\n    You cannot exchange it for the same thing.")
            case _:
                print("    Invalid Option.")
        return self
                
                
    def deposit(self):
        print(f"\nDeposit...\n")
        print(f"   1. 10 U$")
        print(f"   2. 50 U$")
        print(f"   3. Other values\n")
        choice = int(input("   Enter a Your Choice: "))
        match choice:
            case 1:
                print("\n   You are deposited 10U$.")
                self.money += 10
            case 2:
                print("\n   You are deposited 50U$.")
                self.money += 50
            case 3:
                value_deposit = int(input("\n   Enter a value of deposit: "))
                print(f"   You are deposited {value_deposit}U$")
                self.money += value_deposit
            case _:
                print("    Invalid Option.")
        return self
    
    def pix(self, other_account: "Account"):
        print(f"\nPix...\n")
        value = int(input("   Enter a value: "))
        if self.money >= value:
            other_account.money += value
            self.money -= value
            print("    Pix payment successfully completed.")
        else:
            print("    You don't have money for Pix")
        return self
            
    def withdraw(self):
        print(f"\nWithdraw...\n")
        print(f"   1. 10 U$")
        print(f"   2. 50 U$")
        print(f"   3. Other values\n")
        choice = int(input("   Enter a Your Choice: "))
        match choice:
            case 1:
                if self.money >= 10:
                    print("\n   You are withdraw 10U$.")
                    self.money -= 10
                else:
                    print("    You don't have this money.")
            case 2:
                if self.money >= 50:
                    print("\n   You are deposited 50U$.")
                    self.money -= 50
                else:
                    print("    You don't have this money.")
            case 3:
                if self.money >= value_deposit:
                    value_deposit = int(input("\n   Enter a value of deposit: "))
                    print(f"   You are Withdraw {value_deposit}U$")
                    self.money -= value_deposit
                else:
                    print("    You don't have this money.")
            case _:
                print("    Invalid Option.")
        return self
    
    def check_balance(self):
        print(f"\nCheck Balance...\n")
        print(f"Money: {self.money}")
    def view(self):
        print(f"\nView...\n")
        
        print(f"   Name: {self.name}")
        print(f"   Age: {self.age}")
        print(f"   Email: {self.email}")
        print(f"   Bank: {self.bank}")
        print(f"   Money: {self.money}U$")
        
   