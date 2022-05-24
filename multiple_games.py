import random
import requests

game_results = []
player_result = 0
opp_result = 0
draw_result = 0


def get_multiple_pokemon():
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


def get_random_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokie_id)
    res = requests.get(url)
    pokemon = res.json()

    return {
        'name': pokemon["name"],
        'id': pokemon["id"],
        'height': pokemon["height"],
        'weight': pokemon["weight"],
    }


def calc_game_results():
    global player_result
    global opp_result
    global draw_result

    if my_selection > opp_selection:
        player_result += 1
        game_results.append('Player Wins')
        print('YOU WON round {}!!!! '.format(game + 1))
    elif opp_selection > my_selection:
        opp_result += 1
        game_results.append('Opponent Wins')
        print('YOU LOSE 👎🏻  Opponent wins round {}'.format(game + 1))
    elif my_selection == opp_selection:
        draw_result += 1
        game_results.append("Draw")
        print('It was a Draw')


def calc_overall_game_stats():
    global player_result
    global opp_result
    global draw_result

    if player_result > opp_result:
        print('YOU WIN THE GAME 🏆 Results were {p}-{o}'.format(p=player_result, o=opp_result))
    elif opp_result > player_result:
        print('YOU LOST THE GAME. Better Luck next time. Results were {o}-{p}'.format(o=opp_result, p=player_result))
    elif player_result == opp_result:
        print('Draw')


for game in range(4):
    multiple_choice = []
    for multi in range(3):
        pokie_id = random.randint(1, 151)
        multiple_choice.append(pokie_id)

    my_choice = get_multiple_pokemon()
    print('You were given {}'.format(my_choice))

    stat_choice = input('Which stat would you like to use? (Choose from id, height or weight) ')

    opponent_choice = get_random_pokemon()
    print('Opponents choice was {}'.format(opponent_choice))

    my_selection = my_choice[stat_choice]
    opp_selection = opponent_choice[stat_choice]

    calc_game_results()

    with open("resultsFile.txt", "w") as f:
        for result in enumerate(game_results, 1):
            f.write(str(result) + "\n")

calc_overall_game_stats()
