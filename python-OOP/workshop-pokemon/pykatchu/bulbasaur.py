from random import randint
from pykatchu import pokemon


class Bulbasaur(pokemon.Pokemon):
    def __init__(self):
        super().__init__()
        self.strength += 1

    def get_attack_noise(self):
        return 'Bulbasauuuurr!!'

    def get_name(self):
        return 'bulbasaur'
