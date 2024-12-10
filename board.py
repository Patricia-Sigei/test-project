class ScrabbleBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.special_tiles = {
            (7, 7): "★",  # Start tile
            (0, 0): "DW", (0, 7): "TW", (0, 14): "DW",  
            (7, 0): "TW", (7, 14): "TW",  
            (14, 0): "DW", (14, 7): "TW", (14, 14): "DW",  
            (1, 1): "DL", (1, 5): "DL", (1, 9): "DL", (1, 13): "DL",  
            (3, 3): "TW", (3, 11): "TW", (5, 1): "DL", (5, 5): "TL",  
            (9, 1): "DL", (9, 5): "TL", (11, 3): "TW", (11, 11): "TW",  
            (13, 1): "DL", (13, 5): "DL", (13, 9): "DL", (13, 13): "DL",  
            (5, 9): "TL", (9, 9): "TL"  
        }
        self.populate_special_tiles()

    def populate_special_tiles(self):
        # Populate the special tiles on the board
        for coord, tile in self.special_tiles.items():
            x, y = coord
            self.board[x][y] = tile

    def display_board(self):
        from tabulate import tabulate
        headers = [f"{i}" for i in range(15)]
        print(tabulate(self.board, headers=headers, tablefmt="fancy_grid"))

    def place_word(self, word, x, y, direction):
        """
        Place a word on the board starting at (x, y). 
        Direction: 'H' for horizontal, 'V' for vertical.
        """
        if direction == 'H':
            for i, char in enumerate(word):
                self.board[x][y + i] = char
        elif direction == 'V':
            for i, char in enumerate(word):
                self.board[x + i][y] = char
        self.display_board()

# Test board setup
if __name__ == "__main__":
    board = ScrabbleBoard()
    board.display_board()
    board.place_word("HELLO", 7, 7, 'H')  # Example placement
