from random import randint
from pykatchu import pokemon

class Charmander(pokemon.Pokemon):
    def __init__(self):
        super().__init__()
        
    def get_attack_noise(self):
        return 'Charmanderrrrr!!!!'

    def get_name(self):
        return 'Charmander'
