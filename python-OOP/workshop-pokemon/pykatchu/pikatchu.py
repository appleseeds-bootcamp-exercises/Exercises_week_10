from random import randint
from pykatchu import pokemon

class Pikatchu(pokemon.Pokemon):
    def __init__(self):
        super().__init__()
        self.health = max(self.health + 1, 6)

    def get_attack_noise(self):
        return 'pika!pika!'

    def get_name(self):
        return 'Pikatchu'
