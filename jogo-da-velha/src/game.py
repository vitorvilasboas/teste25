class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Representa o tabuleiro
        self.current_player = 'X'

    def start_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        print("Jogo da Velha iniciado!")

    def make_move(self, position):
        if self.is_valid_move(position):
            self.board[position] = self.current_player
            if not self.check_winner():
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
            (0, 4, 8), (2, 4, 6)               # Diagonais
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                print(f"Jogador {self.board[combo[0]]} venceu!")
                return True
        if ' ' not in self.board:
            print("Empate!")
            return True
        return False

    def reset_game(self):
        self.start_game()

    def is_valid_move(self, position):
        return self.board[position] == ' ' and 0 <= position < 9