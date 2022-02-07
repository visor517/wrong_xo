from pprint import pprint
from random import choice


class Game:

    def __init__(self, player_char, ai_char):
        self.board = [['_' for j in range(10)] for i in range(10)]
        self.player_char = player_char
        self.ai_char = ai_char
        # доступные ходы. упростит проверку. для 10х10 вполне норм
        self.available_moves = {(i, j) for j in range(10) for i in range(10)}
        # для оставшихся возможных ходов ai
        self.ai_moves = {(i, j) for j in range(10) for i in range(10)}

    # вывод доски
    def print_board(self):
        pprint(self.board)

    # сделать ход
    def make_move(self, move, char):
        x, y = move
        self.board[x][y] = char
        self.available_moves.remove(move)
        self.ai_moves.discard(move)

    # генератор хода ai
    def generate_move(self):
        
        # выбор безопасного хода
        while len(self.ai_moves) > 0:
            move = choice(list(self.ai_moves))
            if self.check_lose(move, self.ai_char):
                return move
            else:
                self.ai_moves.remove(move)
        
        return choice(list(self.available_moves))

    # проверка на поражение после хода
    def check_lose(self, move, char):
        x, y = move
        temp, self.board[x][y] = self.board[x][y], char # для проверки без хода
        line = ''.join(self.board[x])
        col = ''.join([self.board[i][y] for i in range(10)])
        if x > y:
            diag1 = ''.join([self.board[x - y + i][i] for i in range(10 - x + y)])
        else:
            diag1 = ''.join([self.board[i][y - x + i] for i in range(10 - y + x)])
        if x + y < 9:
            diag2 = ''.join([self.board[x + y - i][i] for i in range(1 + x + y)])
        else:
            diag2 = ''.join([self.board[i][x + y - i] for i in range(9, x + y - 10, -1)])
        self.board[x][y] = temp

        return line.find(char*5) < 0 and col.find(char*5) < 0 and diag1.find(char*5) < 0 and diag2.find(char*5) < 0
