class AIPlayer:
    def __init__(self, tiles):
        self.tiles = tiles  # Tile rack for the AI

    def generate_possible_words(self, dictionary, rack):
        """Generate possible words from the AI's tiles."""
        words = []
        for word in dictionary:
            if all(word.count(char) <= rack.count(char) for char in word):
                words.append(word)
        return words

    def best_move(self, board, scorer, dictionary):
        """Find the best word and placement for the AI."""
        possible_words = self.generate_possible_words(dictionary, self.tiles)
        best_word = None
        best_score = 0
        best_positions = []

        for word in possible_words:
            for x in range(15):
                for y in range(15):
                    for direction in ['H', 'V']:
                        positions = self.calculate_positions(x, y, word, direction)
                        if self.is_valid_placement(positions, board):
                            score = scorer.calculate_score(word, positions, board)
                            if score > best_score:
                                best_word = word
                                best_score = score
                                best_positions = positions

        return best_word, best_score, best_positions

    def calculate_positions(self, x, y, word, direction):
        """Calculate positions for placing a word."""
        positions = []
        if direction == 'H':
            for i in range(len(word)):
                positions.append((x, y + i))
        elif direction == 'V':
            for i in range(len(word)):
                positions.append((x + i, y))
        return positions

    def is_valid_placement(self, positions, board):
        """Check if the positions are valid on the board."""
        for x, y in positions:
            if x < 0 or x >= 15 or y < 0 or y >= 15 or board[x][y] != ' ':
                return False
        return True
