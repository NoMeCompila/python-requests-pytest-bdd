import json

pokemon_data = '{"id": 1,"name": "Pikachu","type": "Electric","abilities": ["Static", "Lightning Rod"]}'

# combia el tipo de dato json representado por string a un objeto json (diccionario)
pokemon_json = json.loads(pokemon_data)
# print(type(pokemon_json))

# print(pokemon_json['abilities'][0])

# read from file

with open('./pokemons.json') as json_file:
    poke_data = json.load(json_file)
    #print(poke_data[0]['base_stats']['hp'])

    for poke in poke_data:
        assert type(poke_data[0]['base_stats']['hp']) == int