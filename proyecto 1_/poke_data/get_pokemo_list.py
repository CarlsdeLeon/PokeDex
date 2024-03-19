from poke_data.pokemon import searchPokemon, Pokemon
from poke_data.pokedex import DoublyLinkedList


def get_pokemon_list(cant):
    pokedex = DoublyLinkedList()
    for i in range(cant + 1, cant + 11):
        name, type, stats, abilities = searchPokemon(str(i))
        pokemon_ = Pokemon(name, type, stats, abilities)
        pokedex.add_to_tail(pokemon_)
    return pokedex


#pokedex.seach_by_position(x)
