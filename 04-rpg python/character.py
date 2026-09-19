class Character:
    def __init__(self, name: str, password: str, email: str, classe: str = "None", max_life: int = 100, resistance: int = 5, stamina: int = 50, speed: int = 10, max_damage: int = 12):
        import random

        self.name = name.strip().title()
        self.password = str(password).strip()
        self.email = email.strip().title()
        self.classe = classe.title()

        """ Character Informations """

        #Niveis

        self.level = 0
        self.level_max = 100
        self.experience = 0
        self.experience_necessary = 100 + (self.level * 25)

        #Attributes

        #Life & Stamina
        self.max_life = max_life
        self.life = self.max_life
        self.resistance = resistance
        self.stamina = stamina
        self.speed = speed

        #Damage
        self.max_damage = max_damage
        self.min_damage = max_damage * 0.75 
        self.damage = random.uniform(self.min_damage, self.max_damage)

        #Critical
        self.critical_chance = 0
        self.critical_damage = 0

        #Dodge
        self.dodge_chance = 0

        self.status ={
            #Damage Status
            "damage": 0,

            #Life Status
            "life": 0,
            "stamina": 0,

            #Buff status
            "speed": 0,
            "critical_chance": 0,
            "critical_damage": 0,
            "dodge_chance": 0,
        }


    def __str__(self):
        def abbreviate_name(name):
            abbreviate = name.split()
            if len(name) <= 13:
                return name
            if len(abbreviate[0] + " " + abbreviate[-1]) > 13:
                if len(abbreviate[0]) > 13:
                    return abbreviate[0][:10] + "..."
                else:
                    len_name_1 = len(abbreviate[0])
                    remaining_space = max(0, (13 - 1 - 3 - len_name_1))
                    return abbreviate[0] + " " + abbreviate[-1][:remaining_space] + "..."
            else:
                return abbreviate[0] + " " +  abbreviate[-1]

        #Colors        
        RESET   = "\033[0m"

        # Standard Colors
        SD_BLACK     = "\033[30m"
        SD_RED       = "\033[31m"  #Damage
        SD_GREEN     = "\033[32m"  # Life
        SD_YELLOW    = "\033[33m"  # XP / GOLD
        SD_BLUE      = "\033[34m"  # Magic
        SD_ROXO      = "\033[35m"  # Epic itens
        SD_CYAN      = "\033[36m"  # ICE
        SD_WHITE     = "\033[37m"
        #Bold
        BL_BLACK     = "\033[1;30m"
        BL_RED       = "\033[1;31m"  # Red
        BL_GREEN     = "\033[1;32m"  # Green life
        BL_YELLOW    = "\033[1;33m"  # Brilliant Yellow gold 
        BL_BLUE      = "\033[1;34m"  # Brilliant Blue
        BL_PURPLE    = "\033[1;35m"  # Purple legendary
        BL_CYAN      = "\033[1;36m"  # Brilliant cyan
        BL_WHITE     = "\033[1;37m"


        return(
            f"\n┌────────────────────────────────────────────────┐\n"
            f"│{"View...":^48}│\n"
            f"├────────────────────────────────────────────────┤\n"
            f"│ Name: {BL_CYAN}{abbreviate_name(self.name):<13} {RESET}│ Class: {BL_PURPLE}{self.classe:<11} {RESET}      │\n"
            f"├────────────────────────────────────────────────┤\n"
            f"│ Level: {self.level:<12} │ XP: {self.experience:<21}│\n"
            f"│ Life: {SD_GREEN if self.life > self.max_life * 0.5 else(SD_YELLOW if self.life < self.max_life * 0.5 and self.life > self.max_life * 0.25 else BL_RED)} {self.life:>5} / {self.max_life:<4} {RESET}│ DMG: {self.min_damage:>5} / {self.max_damage:<5}       │\n"
        )

eu = Character("GABRIELREBOLADOR LENTINHO PARA OS CRIAS", "1231231adas", "GABRIELJOBGOSTOZA@GMAIL.COM")
print(eu)

