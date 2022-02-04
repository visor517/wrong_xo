from pprint import pprint
from random import randint


class Game:

    def __init__(self):
        self.board = [['_' for j in range(10)] for i in range(10)]
        self.player_char = 'X'  # пока без выбора
        self.ai_char = 'O'

    # вывод доски
    def printBoard(self):
        pprint(self.board)

    # сделать ход
    def makeMove(self, x, y, char=None):
        if not char:
            char = self.player_char
        self.board[x][y] = char
        return self.checkLose(x, y, char)

    # ход ИИ
    def generateMove(self):
        x = randint(0, 9)
        y = randint(0, 9)
        return self.makeMove(x, y, self.ai_char)

    # проверка на поражение после хода
    def checkLose(self, x, y, char):
        line = ''.join(self.board[x])
        col = ''.join([self.board[i][y] for i in range(10)])
        #diag = ''.join()
        return line.find(char*5) < 0 and col.find(char*5) < 0


cur_game = Game()

# основной цикл
while True:
    command = input('Введите координаты хода через пробел или q для выхода: ')

    # проверяем выход
    if command.lower() == 'q':
        break

    # обрабатываем ход игрока
    try:
        x, y = command.split(' ')
        if not cur_game.makeMove(int(x), int(y)):
            cur_game.printBoard()
            print('Вы проиграли!')
            break
        if not cur_game.generateMove():
            cur_game.printBoard()
            print('ИИ проиграл!')
            break
        cur_game.printBoard()
    
    except ValueError:
        print(f'Ход {command} нераспознан. Вводите координты через пробел. Пример: 4 6') 
    except IndexError:
        print(f'Ход {command} нераспознан. Допустимые значения координат от 0 до 9')
