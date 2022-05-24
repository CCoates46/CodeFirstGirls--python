import random
import requests


def random_pokemon():
    pokie_id = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokie_id)
    res = requests.get(url)
    pokemon = res.json()

    return {
        'name': pokemon["name"],
        'id': pokemon["id"],
        'height': pokemon["height"],
        'weight': pokemon["weight"],
        }


my_choice = random_pokemon()
print('You were given {}'.format(my_choice))
stat_choice = input('Which stat would you like to use? (Choose from id, height or weight) ')

opponent_choice = random_pokemon()
print('Opponents choice was {}'.format(opponent_choice))

my_selection = my_choice[stat_choice]
opp_selection = opponent_choice[stat_choice]

if my_selection > opp_selection:
    print('YOU WIN!!!!!! 🥳')
elif my_selection < opp_selection:
    print('YOU LOSE 😩')
else:
    print('Draw')

