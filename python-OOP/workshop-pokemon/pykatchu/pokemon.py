from random import randint


class Pokemon:
    def __init__(self):
        self.health = randint(1, 6)
        self.strength = randint(1, 6)
        self.armor = randint(1, 6)
        self.__is_dead = False

    def attack(self, other_pokemon):
        attack_result = self.strength + \
            randint(1, 4) - other_pokemon.armor - randint(1, 4)
        if(attack_result > 0):
            other_pokemon.health -= attack_result
            if other_pokemon.health <= 0:
                other_pokemon.set_is_dead(True)
            return True
        elif self.get_name() == 'Charmander':
            other_pokemon.health -= 1
            if other_pokemon.health <= 0:
                other_pokemon.set_is_dead(True)
            return True
        else:
            return False

    def is_dead(self):
        return self.__is_dead

    def set_is_dead(self, is_dead):
        self.__is_dead = is_dead
