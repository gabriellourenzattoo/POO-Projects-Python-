from account import Account

class Nubank(Account):
    def __init__(self, name, age, email, password, money = 0):
        super().__init__(name, age, email, password,"Nubank", money)
class Mercado_pago(Account):
    def __init__(self, name, age, email, password,money = 0):
            super().__init__(name, age, email, password, "Mercado Pago", money)
class Itau(Account):
    def __init__(self, name, age, email, password, money = 0):
            super().__init__(name, age, email, password, "Itaú", money)
class Inter(Account):
    def __init__(self, name, age, email, password,money = 0):
            super().__init__(name, age, email, password, "Inter", money)
class Santander(Account):
    def __init__(self, name, age, email, password,money = 0):
            super().__init__(name, age, email, password,"Santander", money)