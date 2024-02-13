from beautifulsoup import BS4_Retorno
import re
import json

soup = BS4_Retorno.abre_site('https://bulbapedia.bulbagarden.net/wiki/List_of_Pokémon_by_National_Pokédex_number')

############# Pegando as infos dos pokemons ###############

tables = soup.find_all('table', {'class': 'roundy'})

pokemon_list = []

for table in tables:
    rows_name = table.find_all('tr', {'style': re.compile('background:#FFF')}) #Pegando todas as linhas das tabelas

    for row in rows_name: 

        rows_id = row.find('td',text=re.compile('^#')) # O ^ antes do # é para buscar tudo o que começar com # para encontrar o ID do pokemon
        if rows_id:
            pokemon_id = rows_id.text

        name = row.find('a', {'title': re.compile('\(Pokémon\)')}) #Aqui eu busco o nome do pokemon em todo lugar que contenha (Pokémon)
        pokemon_name = name.text

        type = ''
        pokemon_type = row.find_all('a',{'title': re.compile('\(type\)')})
        if pokemon_type:
            row_type = len(pokemon_type)
            for i in range(row_type):
                
                if type == '':
                    type += pokemon_type[i].text
                else:
                    type += f' - {pokemon_type[i].text}'
        
        img_tag = row.find('img')
        if img_tag:
            pokemon_img = img_tag.get('src')
        
        #Transformo em um Json para facilitar a manipulação dos dados em outras partes do programa.
        pokemon = {
            'Id': pokemon_id,
            'Img': pokemon_img,
            'Name': pokemon_name,
            'Types': type
        }

        pokemon_list.append(pokemon)

        with open('Pokemon_list.json','w') as archive:
            json.dump(pokemon_list, archive, indent=2)
