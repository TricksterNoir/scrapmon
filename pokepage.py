from beautifulsoup import BS4_Retorno
from functionspokepage import list_of_pokemon
import re
from globalfunctions import Calculo 

pokemon_name_list = list_of_pokemon()
pokemon_gender_ratio = ""
name = ""

for pokemon_name in pokemon_name_list:
    retorno = BS4_Retorno.abre_site(f'https://bulbapedia.bulbagarden.net/wiki/{pokemon_name}_(Pokémon)')

    def pokemon_basic_infos():
        container_category = retorno.find('a',{'title': re.compile('Pokémon category')})
        seed_type = container_category.find_previous('big')
        id_and_name = retorno.find('span', text=lambda text: text.startswith('#'))
        return f'Pokémon: {id_and_name.text} - Pokémon Seed Type: {seed_type.text}'

    def pokemon_type():
        container_types = retorno.find_all('a', {'title': re.compile('\(type\)$')})
        for item in container_types:# TERMINAR DE ARRUMAR ESSE CÓDIGO.
            ...
            #if span_tag:
            #    b_tag = span_tag.find('b')
            #    if b_tag and b_tag.text != 'Unknown':
            #        print(b_tag)
        #for pokemon_type in container_types:
        #    teste = pokemon_type.text
        #    if teste != 'Unknown':
        #        print(teste)

    def gender_ratio():
        container_gender = retorno.find_all('a',{'title': re.compile('\with a gender ratio of')})
        if container_gender:
            for item in container_gender:
                porcentage = item.find_all('span')
                if porcentage:
                    for porcent in porcentage:
                        if name == "":
                            name += porcent.text
                        else:
                            name += f', {porcent.text}'
        return name

    def catch_rate():
        container_catch = retorno.find('span',{'title':re.compile('^When an ordinary Poké Ball is thrown at full health')})
        catch_rate = container_catch.find_previous('td')
        
        return f'Catch rate: {catch_rate.text}'

    def egg_groups():
        container_eggs = retorno.find('a', {'title': re.compile('Egg Group')})
        backtracking_eggs = container_eggs.find_previous('td')
        table_type_eggs = backtracking_eggs.find('table')
        a_tag = table_type_eggs.find_all('a')
        names = []

        for tag in a_tag:
            names.append(tag.text)
        
        return names

    def egg_cycles():
        container_egg_cycle = retorno.find_all('a', {'title':re.compile('Egg cycle')})
        
        for a_tag in container_egg_cycle:
            backtracking_cycles = a_tag.find_previous('td')
            table_cycle = backtracking_cycles.find('table')
            cycles = table_cycle.find('td')

        return cycles.text
    
    def pokemon_height():
        container_height = retorno.find_all('a', {'title':re.compile('List of Pokémon by height')})
        for a_tag in container_height:
            backtracking_height = a_tag.find_previous('td')
            table_height = backtracking_height.find('table')
            list_height = table_height.find('td')
            for height in list_height:
                height_class = Calculo(str(height))
                meters = height_class.converte_polegada()
                print(meters)

    if __name__ == '__main__':
        pokemon_height()
        break