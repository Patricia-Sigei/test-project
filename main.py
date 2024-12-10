from board import ScrabbleBoard
from score import Scorer
from random import choice
from tile import TileBag
from ai import AIPlayer

class ScrabbleGame:
    def __init__(self):
        self.board = ScrabbleBoard()
        self.scorer = Scorer()
        self.tile_bag = TileBag()
        self.players = {}
        self.current_round = 0

    def setup_game(self):
        print("Welcome to CLI Scrabble!")
        mode = input("Choose mode: 1 (AI vs Player) or 2 (AI vs 2 Players): ")
        self.players = {
            "AI": {"tiles": self.tile_bag.draw_tiles(7), "score": 0},
            "Player 1": {"tiles": self.tile_bag.draw_tiles(7), "score": 0},
        }
        if mode == "2":
            self.players["Player 2"] = {"tiles": self.tile_bag.draw_tiles(7), "score": 0}

    def play_turn(self, player):
        if player == "AI":
            ai = AIPlayer(self.players["AI"]["tiles"])
            dictionary = self.get_dictionary()
            best_word, score, positions = ai.best_move(self.board.board, self.scorer, dictionary)
            if best_word:
                self.board.place_word(best_word, positions[0][0], positions[0][1], 'H')
                self.players["AI"]["score"] += score
                print(f"AI played '{best_word}' for {score} points!")
        else:
            print(f"{player}'s turn! Your tiles: {self.players[player]['tiles']}")
            word = input("Enter a word: ").upper()
            x, y, direction = map(int, input("Enter start position (row, col) and direction (0 for H, 1 for V): ").split())
            positions = self.board.calculate_positions(x, y, word, 'H' if direction == 0 else 'V')
            if self.board.is_valid_placement(positions):
                score = self.scorer.calculate_score(word, positions, self.board.board)
                self.players[player]["score"] += score
                print(f"{player} played '{word}' for {score} points!")
            else:
                print("Invalid move! Try again.")

    def get_dictionary(self):
        """Retrieve all valid words from the database."""
        query = "SELECT word FROM dictionary;"
        self.scorer.cursor.execute(query)
        return [row[0] for row in self.scorer.cursor.fetchall()]

    def start_game(self):
        self.setup_game()
        print("\nStarting game...\n")
        self.board.display_board()

        turns = ["AI", "Player 1", "Player 2"] if "Player 2" in self.players else ["AI", "Player 1"]

        while self.current_round < 2:
            for turn in turns:
                self.play_turn(turn)
                self.board.display_board()

            self.current_round += 1

        self.declare_winner()

    def declare_winner(self):
        print("\nGame Over! Final Scores:")
        for player, data in self.players.items():
            print(f"{player}: {data['score']} points")
        winner = max(self.players, key=lambda p: self.players[p]["score"])
        print(f"The winner is {winner}!")

if __name__ == "__main__":
    game = ScrabbleGame()
    game.start_game()
