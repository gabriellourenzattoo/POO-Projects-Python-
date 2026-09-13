
class Character:
    def __init__(self, name, classe:str=None, max_life:int=100, resistance:int=5, speed:int=5, atack_power:int=10):
        #Visual
        self.name = name.strip().title()
        self.classe = classe
        
        #Life
        self.max_life = max_life
        self.life = self.max_life
        self.resistance = resistance
        self.speed = speed
        
        #Damage
        self.atack_power = atack_power
    
    def view(self):
        print(f"\nView...\n")
        print(f"Name: {self.name}")
        print(f"Class: {self.classe}")
        print(f"Max life: {self.max_life}")
        print(f"Resistance: {self.resistance}")
        print(f"Speed: {self.speed}")
        print(f"Atack Damage: {self.atack_power}")
        
    def atack(self, enemy):
        from enemys import Enemy
        enemy.take_damage(self.atack_power)
        print(f"{self.name} Attacked: {enemy.name}. {enemy.name} took a hit with {self.atack_power} power.")
        return self
    
    def take_damage(self, damage):
        self.life -= max(1,damage - (1 - self.resistance / 100))
        return self
    
