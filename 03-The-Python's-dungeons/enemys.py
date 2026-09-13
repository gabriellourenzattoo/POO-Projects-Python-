
class Enemy:
    def __init__(self, name, max_life:int=100, resistance:int=5, atack_power:int=10, speed:int=5, ):
        self.name = name.title().strip()
        self.max_life = max_life
        self.life = self.max_life
        self.resistance = resistance
        self.speed = speed
        self.atack_power = atack_power
        
    def atack(self, human):
        from character import Character
        human.take_damage(self.atack_power)
        print(f"{self.name} Attacked: {human.name}. {human.name} took a hit with {self.atack_power} power.")
        return self
    
    def take_damage(self, damage):
        self.life -= max(1, damage - (1 - self.resistance / 100))
        return self
    
