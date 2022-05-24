import requests
import random


def multiple_pokemon():
    print('Your pokemon choices are {}'.format(multiple_choice))
    multi_choice = input('Which pokemon would you like to use? ')
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(multi_choice)
    res = requests.get(url)
    pokemon_multiple = res.json()

    return {
        'name': pokemon_multiple["name"],
        'id': pokemon_multiple["id"],
        'height': pokemon_multiple["height"],
        'weight': pokemon_multiple["weight"],
        }


def random_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokie_id)
    res = requests.get(url)
    pokemon = res.json()

    return {
        'name': pokemon["name"],
        'id': pokemon["id"],
        'height': pokemon["height"],
        'weight': pokemon["weight"],
        }


multiple_choice = []

for p in range(4):
    pokie_id = random.randint(1, 151)
    multiple_choice.append(pokie_id)


my_choice = multiple_pokemon()
print('You were given {}'.format(my_choice))
stat_choice = input('Which stat would you like to use? (Choose from id, height or weight) ')

opponent_choice = random_pokemon()
print('Opponents choice was {}'.format(opponent_choice))

my_selection = my_choice[stat_choice]
opp_selection = opponent_choice[stat_choice]


if my_selection > opp_selection:
    print('YOU WIN!!!!!! 🏆')
elif my_selection < opp_selection:
    print('YOU LOSE 👎🏻')
else:
    print('It was a Draw')
