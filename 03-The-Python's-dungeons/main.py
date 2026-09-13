from character import Character
from enemys import Enemy
from rpgclass import Mage, Warrior, Assassin, Tank, Archer
import random
accounts = []
enemys = [
    Enemy("Goblin", 70, 3, 10, 7),
    Enemy("Skeleton", 60, 5, 8, 6),
    Enemy("Orc", 120, 8, 15, 4),
    Enemy("Wolf", 80, 4, 12, 10),
    Enemy("Troll", 180, 12, 20, 2),
    Enemy("Dark Mage", 90, 3, 18, 6),
    Enemy("Golem", 250, 20, 25, 1),
    Enemy("Vampire", 150, 10, 18, 8),
    Enemy("Dragon", 500, 25, 40, 7),
]

def find_account(name:str):
    for account in accounts:
        if account.name.lower() == name.lower():
            return account
    return None

def Battle(Account:Character, enemy: Enemy):
    while Account.life > 0 and enemy.life > 0:
        print("\nBatle...\n")
        print(f"Name: {Account.name} | {enemy.name}")
        print(f"Life: {Account.life} | {enemy.life}")
        new_turn = input("\nPressione Enter para o próximo turno...")
        
        Account.atack(enemy)
        if enemy.life > 0:
            enemy.atack(Account)

        if Account.life > 0 and enemy.life < 0:
            print(f"\n🎉 {Account.name} Ganhou A Batalha.")
        if enemy.life > 0 and Account.life < 0:
            print(f"\n💀 {enemy.name} Ganhou a Batalha.")
        

def login(Account:Character):
    while True:
        print(f"\n=======    RPG    ======")
        print(f"Hello, {Account.name}!\n")
        print(f"1. Character.")
        print(f"2. Battle.")
        print(f"3. Logout.\n")
        try:
            choice = int(input("Enter a Your Choice:"))
            match choice:
                case 1:
                    Account.view()
                case 2:
                    Battle(Account, random.choice(enemys))
                case 3:
                    break
        except (ValueError, TypeError):
                print("Enter a valid number.")

while True:
    print(f"\nRPG PYG\n")
    print("1. Login")
    print("2. Registre")
    print("3. Exit\n ")
    try:
        choice = int(input("Enter a Your Choice: "))
        
        match choice:
            case 1:
                user_name = input("\nEnter a Username of your Account: ")
                Account =find_account(user_name)
                if Account:
                    login(Account)
                else:
                    print("Account not found.")
            case 2:
                print("\nRegistre...\n")
                user_name = input("\nEnter a Username of your Account: ")
                Account =find_account(user_name)
                if not Account:
                    print("\nEntrer a Your class.\n")
                    print(f"1. Mage")
                    print(f"2. Warrior")
                    print(f"3. Assasin")
                    print(f"4. Tank")
                    print(f"5. Archer\n")
                    choice = int(input("Enter a Your choice: "))
                    match choice:
                        case 1:
                            new_account = Mage(user_name)
                            accounts.append(new_account)
                            print("Account successfully created")
                        case 2:
                            new_account = Warrior(user_name)
                            accounts.append(new_account)
                            print("Account successfully created")
                        case 3:
                            new_account = Assassin(user_name)
                            accounts.append(new_account)
                            print("Account successfully created") 
                        case 4:
                            new_account = Tank(user_name)
                            accounts.append(new_account)
                            print("Account successfully created")
                        case 5:
                            new_account = Archer(user_name)
                            accounts.append(new_account)
                            print("Account successfully created")
                        case _:
                            print("Invalid Option.")
                else:
                    print("\nYou cannot create an account that already exists.")  
            case 3:
                print("\nExit...\n")
                break                    
            case _:
                print("Invalid Option.")
    except (ValueError, TypeError):
        print("Enter a valid number.")