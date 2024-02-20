import json


def list_of_pokemon():
    data_json = 'Pokemon_list.json'
    pokemon_list_names = set()

    with open(data_json) as pokemon_data:
        pokemon_infos = json.load(pokemon_data)

    for pokemon in pokemon_infos:
        pokemon_list_names.add(pokemon['Name'])

    pokemon_list_names = list(pokemon_list_names)

    return pokemon_list_names

if __name__ == '__main__':
    teste = list_of_pokemon()
    print(teste[148])