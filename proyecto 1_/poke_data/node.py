from poke_data.pokemon import Pokemon
class Node:
    def __init__(self, data:Pokemon) -> None:
        self.data = data
        self.next = None
        self.previous = None