from account import Account
from bank import Nubank, Mercado_pago, Inter, Itau, Santander

accounts = []

def find_account(name: str):
    for account in accounts:
        if account.name.strip().lower() == name.strip().lower():
            return account
    else:
        return None
def login(account: Account):
    print(f"\nAccount Menu...\n")
    password = input("    Entrer Your password: ")
    
    if account.password != password:
        return
    
    while True:
        print(f"\nAccount Menu...\n")
        print(f"    1. Deposit")
        print(f"    2. Withdraw")
        print(f"    3. Pix")
        print(f"    4. Check Balance")
        print(f"    5. Account Info")
        print(f"    6. Change Accont Info")
        print(f"    7 Logout\n")
        choice = int(input("    Entrer a Your choice: "))
        match choice:
            case 1:
                account.deposit()
            case 2:
                account.withdraw()
            case 3:
                account_pix = input("\n    Entrer a Account for Pix: ")
                account_for_pix = find_account(account_pix)
                if account_for_pix:
                    account.pix(account_for_pix)
                else:
                    print(" Account Not Found.")
            case 4:
                account.check_balance()
            case 5:
                account.view()
            case 6:
                account.change()
            case 7:
                break
            case _:
                print("\n Invalid Option.")
              
def register():
    print("\nRegister Menu...\n")
    account_name = input("    Name: ")
    account_with_this_name = find_account(account_name)
    if account_with_this_name:
        print("An account with this name already exists.")
        return
    account_age = int(input("     Age: "))
    account_email = input("    Email: ")
    account_password =input("    Password: ")
    print("    Bank:")
    print("        1. Nubank")
    print("        2. Mercado Pago")
    print("        3. Itaú")
    print("        4. Inter")
    print("        5. Santander")
    print("        6. None")
    choice_bank = int(input("        Entrer a choice for Bank: "))
    match choice_bank:
        case 1:
            account = Nubank(account_name, account_age, account_email, account_password)
            accounts.append(account)
        case 2: 
            account = Mercado_pago(account_name, account_age, account_email, account_password)
            accounts.append(account)
        case 3:
            account = Itau(account_name, account_age, account_email, account_password)
            accounts.append(account)
        case 4:
            account = Inter(account_name, account_age, account_email, account_password)
            accounts.append(account)
        case 5:
            account = Santander(account_name, account_age, account_email, account_password)
            accounts.append(account)
        case _:
            account = Account(account_name, account_age, account_email, account_password)
            accounts.append(account)
while True:
    
    print(f"\nMenu...\n")
    print(f"    1. Login")
    print(f"    2. Registre")
    print(f"    3. Exit\n")
    choice = int(input("    Enter Your choice: "))
    
    match choice:
        case 1:
            print(f"\nLogin's Menu\n")
            account_name = input("    Enter a Account name: ")
            account = find_account(account_name)
            if account:
                login(account)
            else: print("    This account don't exist. ")
        case 2:
            register()
        case 3:
            print("\nExit...\n")
            break