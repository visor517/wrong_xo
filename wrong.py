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
    def printBoard(self):
        pprint(self.board)

    # сделать ход
    def makeMove(self, move, char):
        x, y = move
        self.board[x][y] = char
        self.available_moves.remove(move)
        self.ai_moves.remove(move)

    # генератор хода ai
    def generateMove(self):
        
        # выбор безопасного хода
        while len(self.ai_moves) > 0:
            move = choice(list(self.ai_moves))
            if self.checkLose(move, self.ai_char):
                return move
            else:
                self.ai_moves.remove(move)
        
        return choice(self.available_moves)

    # проверка на поражение после хода
    def checkLose(self, move, char):
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


cur_game = Game('X', 'O')

# основной цикл
while len(cur_game.available_moves) > 0:
    command = input('Введите координаты хода через пробел или q для выхода: ')

    # проверяем на выход
    if command.lower() == 'q':
        break

    # обрабатываем ход игрока
    try:
        x, y = command.split(' ')
        move = int(x), int(y)
    except:
        print(f'Команда {command} не определена')
        
    if move[0] in range(10) and move[1] in range(10) and move in cur_game.available_moves:

        cur_game.makeMove(move, cur_game.player_char)
        if not cur_game.checkLose(move, cur_game.player_char):
            cur_game.printBoard()
            print('Вы проиграли!')
            break
        ai_move = cur_game.generateMove()
        cur_game.makeMove(ai_move, cur_game.ai_char)
        if not cur_game.checkLose(ai_move, cur_game.ai_char):
            cur_game.printBoard()
            print('ИИ проиграл!')
            break
        cur_game.printBoard()
    else:
        print('Координаты могут иметь значения от 0 до 9 или ход не допустим')

print('Игра закончена')
