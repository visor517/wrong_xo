import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

from wrong_gui import Ui_MainWindow
from logic import Game

def main():

    # создаем графическое окружение
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    def start_game():
        global cur_game

        # обновляем поле
        for item in ui.buttonGroup.buttons():
            item.setText('')
            item.setEnabled(True)

        if ui.radioButtonX.isChecked():
            cur_game = Game('X', 'O')
        else:
            cur_game = Game('O', 'X')
            ai_move()

    # конец игры, блокировка поля
    def over_game(message):
        for item in ui.buttonGroup.buttons():
            item.setEnabled(False)
        # сообщение
        msg = QMessageBox()
        msg.setText(message)
        msg.setWindowTitle("THE END")
        msg.exec_()

    # ход игрока
    def make_move():
        field = MainWindow.sender()
        field.setText(cur_game.player_char)
        field.setEnabled(False)
        move = tuple([int(i) for i in field.objectName().split('_')[1:]])
        cur_game.make_move(move, cur_game.player_char)
        if not cur_game.check_lose(move, cur_game.player_char):
            over_game("Game over!")
            return

        if len(cur_game.available_moves) == 0:
            over_game("Dead heat!")
        else:
            ai_move()
    
    # ход ии
    def ai_move():
        move = cur_game.generate_move()
        cur_game.make_move(move, cur_game.ai_char)
        field = MainWindow.findChild(QPushButton, f'field_{move[0]}_{move[1]}')
        field.setText(cur_game.ai_char)
        field.setEnabled(False)
        if not cur_game.check_lose(move, cur_game.ai_char):
            over_game("Victory!")

        if len(cur_game.available_moves) == 0:
            over_game("Dead heat!")


    # навешиваем метод на поля
    for item in ui.buttonGroup.buttons():
        item.clicked.connect(make_move)

    ui.startButton.clicked.connect(start_game)
        

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
