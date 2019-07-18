from pykatchu.pikatchu import Pikatchu
from pykatchu.aipom import Aipom
from pykatchu.charmander import Charmander
from pykatchu.bulbasaur import Bulbasaur
import random
pokemons = [Pikatchu, Aipom, Charmander, Bulbasaur]
p1 = random.choice(pokemons)()
p2 = random.choice(pokemons)()
print(f'On the arena we have our pokemon: {p1.get_name()}, and on the other side we have : {p2.get_name()}\n Prepare yourselves!!')
game_on = True
round_conter = 0
while game_on:
    print(p1.get_attack_noise())
    print(p1.get_name() + (" hit!" if p1.attack(p2) else " miss!"))
    if not p2.is_dead():
        print(p2.get_attack_noise())
        print(p2.get_name() + (" hit!" if p2.attack(p1) else " miss!"))
    if p1.is_dead() or p2.is_dead():
        game_on = False
    if round_conter >= 10:
        game_on = False
    round_conter += 1    
print("game is over... ")
if p1.is_dead():
    print(p2.get_name() + " won")
elif p2.is_dead():
    print(p1.get_name() + " won")
else:
    print('No winners!')
