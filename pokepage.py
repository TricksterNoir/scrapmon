from beautifulsoup import BS4_Retorno
from functionspokepage import list_of_pokemon
import re

pokemon_name_list = list_of_pokemon()
pokemon_gender_ratio = ""
name = ""

for pokemon_name in pokemon_name_list:
    retorno = BS4_Retorno.abre_site(f'https://bulbapedia.bulbagarden.net/wiki/{pokemon_name}_(Pokémon)')
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
