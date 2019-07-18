from random import randint
from pykatchu import pokemon


class Aipom(pokemon.Pokemon):
    def __init__(self):
        super().__init__()
        self.armor = max(self.armor, 4)

    def get_attack_noise(self):
        return 'Aiiiiipom!!!!!'

    def get_name(self):
        return 'Aipom'
