import psycopg2
from board import ScrabbleBoard


# Letter points in Scrabble
LETTER_VALUES = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10
}

class Scorer:
    def __init__(self):
        
        self.conn = psycopg2.connect(
            dbname="scrabble_game",
            user="your_username",
            password="your_password",
            host="localhost"
        )
        self.cursor = self.conn.cursor()

    def validate_word(self, word):
        """Check if a word is valid using the dictionary."""
        query = "SELECT word FROM dictionary WHERE word = %s;"
        self.cursor.execute(query, (word,))
        result = self.cursor.fetchone()
        return result is not None

    def calculate_score(self, word, positions, board):
        """
        Calculate the score for a word based on:
        - Letter values
        - Special tiles (e.g., TW, DL)
        """
        score = 0
        word_multiplier = 1

        for i, (letter, (x, y)) in enumerate(zip(word, positions)):
            letter_value = LETTER_VALUES[letter.upper()]
            tile = board[x][y]

            # Apply special tile logic
            if tile == "DL":  
                letter_value *= 2
            elif tile == "TL":  
                letter_value *= 3
            elif tile == "DW":  
                word_multiplier *= 2
            elif tile == "TW":  
                word_multiplier *= 3

            score += letter_value

        return score * word_multiplier

    def close_connection(self):
        """Close PostgreSQL connection."""
        self.cursor.close()
        self.conn.close()


# Example usage
if __name__ == "__main__":
    scorer = Scorer()
    word = "HELLO"
    positions = [(7, 7), (7, 8), (7, 9), (7, 10), (7, 11)]  
    board = ScrabbleBoard().board  

    if scorer.validate_word(word):
        score = scorer.calculate_score(word, positions, board)
        print(f"The score for '{word}' is {score}")
    else:
        print(f"'{word}' is not a valid word!")
