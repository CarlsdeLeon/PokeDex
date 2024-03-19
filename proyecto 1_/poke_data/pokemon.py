import requests
import json


class Pokemon:
    def __init__(self, name, type, stats, abilities) -> None:
        self.name = name
        self.type = type
        self.stats = stats
        self.abilities = abilities

    def __str__(self) -> str:
        types = ''
        stat = ''
        ability = ''
        for i in range(len(self.type)):
            types += '<br>' + self.type[i]
        for i in range(len(self.stats)):
            stat += '<br>' + self.stats[i]
        for i in range(len(self.abilities)):
            ability += '<br>' + self.abilities[i]
        return str(f'Name : {self.name}{types}' + '<br/>' + stat + '<br/>' + ability + '<br/>')

def searchPokemon(idPokemon):
    name = ''
    types = []
    stats = []
    abilities = []
    url_api = 'https://pokeapi.co/api/v2/pokemon/' 
    search = requests.get(url_api + idPokemon)
    if search.status_code == 200:
        pokemon = json.loads(search.content)
        name = pokemon['name']
        for type in pokemon['types']:
            types.append('Type : ' + str(type['type']['name']))
        for i in range(6):
            stats.append(str(pokemon['stats'][i]['stat']['name']) + ' : ' +str(pokemon['stats'][i]['base_stat']))

        for ability in pokemon['abilities']:
            if ability['is_hidden']:
                abilities.append('Hidden Ability' + ' : '+ str(ability['ability']['name']))
            else:
                abilities.append(('Ability' + ' : '+ str(ability['ability']['name'])))
    else:
        print('Pokemon not found, see the data you input.')
    return name, types,stats, abilities

