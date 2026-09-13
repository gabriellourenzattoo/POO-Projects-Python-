from character import Character
import random

class Mage(Character):
    def __init__(self, name, classe = "Mage", max_life = 80, resistance = 2, speed = 4, atack_power = 3):
        super().__init__(name, classe, max_life, resistance, speed, atack_power)
        self.magic_damage = 15
        self.max_mana = 50
        self.mana = self.max_mana
      
    def view(self):
        super().view()    
        print(f"Magic Damage: {self.magic_damage}")
        print(f"Mana: {self.mana}")
    def atack(self, enemy):
        from enemys import Enemy
        if self.mana > 0:
            power = self.magic_damage
            self.mana -= 5
            withal = "Magic"
        else:
            power = self.atack_power
            withal = "Melee"
        enemy.take_damage(power)
        print(f"{self.name} Attacked: {enemy.name} with {withal}. {enemy.name} took a hit with {power} power.")
        return self
    
class Warrior(Character):
    def __init__(self, name, classe = "Warrior", max_life = 80, resistance = 7, speed = 5, atack_power = 20):
        super().__init__(name, classe, max_life, resistance, speed, atack_power)
        
class Assassin(Character):
    def __init__(self, name, classe = "Assasin", max_life = 90, resistance = 6, speed = 10, atack_power = 13):
        super().__init__(name, classe, max_life, resistance, speed, atack_power)
        
    def atack(self, enemy):
        from enemys import Enemy
        critcal = random.randint(1,10) < 3
        if critcal:
            power = self.atack_power * 1.25
            enemy.take_damage(power)
            print(f"{self.name} Attacked: {enemy.name} with a critcal hit. {enemy.name} took a hit with {power} power.")
        else:
            power = self.atack_power
            enemy.take_damage(power)
            print(f"{self.name} Attacked: {enemy.name}. {enemy.name} took a hit with {power} power.")
        return self
     
    def take_damage(self, damage):
        dodge = random.randint(1,10) < 3
        if dodge:
            print(f"{self.name} dodged the attack.")
        else:    
            self.life -= damage - (1 - self.resistance // 100)
        return self
        
class Tank(Character):
    def __init__(self, name, classe = None, max_life = 150, resistance = 10, speed = 1, atack_power = 4):
        super().__init__(name, classe, max_life, resistance, speed, atack_power)
        
class Archer(Character):
    def __init__(self, name, classe = None, max_life = 90, resistance = 5, speed = 8, atack_power = 5):
        super().__init__(name, classe, max_life, resistance, speed, atack_power)
        self.arch_damage = 15
        self.arrows = 15
        
    def view(self):
        super().view()
        print(f"Arch Damage: {self.arch_damage}")
        print(f"Arrows: {self.arrows}")
            
    def atack(self, enemy):
        from enemys import Enemy
        critcal = random.randint(1,10) < 4
        
        if self.arrows > 0:
            power = self.arch_damage
            self.arrows -= 1 
            withal = "Arrow"
        else:
            power = self.atack_power
            withal = "Melee"
        if critcal:
            power = power * 1.25
            enemy.take_damage(power)
            print(f"{self.name} Attacked: {enemy.name} with {withal} Crital hit. {enemy.name} took a hit with {power} power.")
        else:
            enemy.take_damage(power)
            print(f"{self.name} Attacked: {enemy.name} with {withal}. {enemy.name} took a hit with {power} power.")
        return self