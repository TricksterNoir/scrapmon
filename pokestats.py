from beautifulsoup import BS4_Retorno
import re
import json 

soup = BS4_Retorno.abre_site('https://bulbapedia.bulbagarden.net/wiki/List_of_Pokémon_by_base_stats_(Generation_IX)')

rows = soup.find_all('tr')

list_pokemon = []

for row in rows:
    pokemon_name = ""
    pokemon_id = ""
    pokemon_hp = 0
    pokemon_atk = 0
    pokemon_def = 0
    pokemon_spatk = 0
    pokemon_spdef = 0
    pokemon_speed = 0
    pokemon_total = 0
    pokemon_avg = 0

    # Filtrando o nome dos pokémons.
    name = row.find('a', {'title':re.compile('\(Pokémon\)')})
    if name:
        small_tag = row.find('small')# A tag small é uma tag que foi usada pra descrever caracteristicas especiais de algum pokemon.
        if small_tag:
            pokemon_name = f'Name: {name.text} - {small_tag.text}'
        else:
            pokemon_name = f'Name: {name.text}' 

    tags = row.find_all('td')
    
    # Filtrando todas as tags td que não tenha o colspan = 2 e pego apenas as tags td que não possuam outras tags dentro.
    stats_tag = [td for td in tags if not td.find() and not (td.get('colspan') == '2')]
    if stats_tag:
        pokemon_hp = stats_tag[1].text
        pokemon_atk = stats_tag[2].text
        pokemon_def = stats_tag[3].text
        pokemon_spatk = stats_tag[4].text
        pokemon_spdef = stats_tag[5].text
        pokemon_speed = stats_tag[6].text
        pokemon_total = stats_tag[7].text
        pokemon_avg = stats_tag[8].text

    if pokemon_hp != 0:
        pokemon_name = pokemon_name.replace('\n', '')
        pokemon_hp = pokemon_hp.replace('\n', '')
        pokemon_atk = pokemon_atk.replace('\n', '')
        pokemon_def = pokemon_def.replace('\n', '')
        pokemon_spatk = pokemon_spatk.replace('\n', '')
        pokemon_spdef = pokemon_spdef.replace('\n', '')
        pokemon_speed = pokemon_speed.replace('\n', '')
        pokemon_total = pokemon_total.replace('\n', '')
        pokemon_avg = pokemon_avg.replace('\n', '')

        pokemon = {
            'Name':pokemon_name,
            'HP':pokemon_hp,
            'ATK': pokemon_atk,
            'DEF': pokemon_def,
            'SP Atk': pokemon_spatk,
            'SP Def': pokemon_spdef,
            'SPEED': pokemon_speed,
            'TOTAL': pokemon_total,
            'AVG': pokemon_avg
        }

        list_pokemon.append(pokemon)
    
    with open('Pokemon_stats_list.json','w',encoding='utf8') as archive:
        json.dump(list_pokemon, archive, indent=2, ensure_ascii=False)
