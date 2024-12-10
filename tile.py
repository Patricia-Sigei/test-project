import random

class TileBag:
    def __init__(self):
        self.tiles = [
        ['A'] * 9 + ['B'] * 2 + ['C'] * 2 + ['D'] * 4 + ['E'] * 12 +
        ['F'] * 2 + ['G'] * 3 + ['H'] * 2 + ['I'] * 9 + ['J'] * 1 +
        ['K'] * 1 + ['L'] * 4 + ['M'] * 2 + ['N'] * 6 + ['O'] * 8 +
        ['P'] * 2 + ['Q'] * 1 + ['R'] * 6 + ['S'] * 4 + ['T'] * 6 +
        ['U'] * 4 + ['V'] * 2 + ['W'] * 2 + ['X'] * 1 + ['Y'] * 2 +
        ['Z'] * 1 + [' '] * 2  # 
        ]
        random.shuffle(self.tiles)

    def draw_tiles(self, num_tiles):
        drawn_tiles = self.tiles[:num_tiles]
        self.tiles = self.tiles[num_tiles:]
        return drawn_tiles
