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

    def startGame():
        global cur_game

        # обновляем поле
        for item in ui.buttonGroup.buttons():
            item.setText('')
            item.setEnabled(True)

        if ui.radioButtonX.isChecked():
            cur_game = Game('X', 'O')
        else:
            cur_game = Game('O', 'X')
            aiMove()

    # конец игры, блокировка поля
    def gameOver(message):
        for item in ui.buttonGroup.buttons():
            item.setEnabled(False)
        # сообщение
        msg = QMessageBox()
        msg.setText(message)
        msg.setWindowTitle("THE END")
        msg.exec_()

    # ход игрока
    def makeMove():
        field = MainWindow.sender()
        field.setText(cur_game.player_char)
        field.setEnabled(False)
        move = tuple([int(i) for i in field.objectName().split('_')[1:]])
        cur_game.makeMove(move, cur_game.player_char)
        if not cur_game.checkLose(move, cur_game.player_char):
            gameOver("Game over!")
            return

        if len(cur_game.available_moves) == 0:
            gameOver("Dead heat!")
        else:
            aiMove()
    
    # ход ии
    def aiMove():
        move = cur_game.generateMove()
        cur_game.makeMove(move, cur_game.ai_char)
        field = MainWindow.findChild(QPushButton, f'field_{move[0]}_{move[1]}')
        field.setText(cur_game.ai_char)
        field.setEnabled(False)
        if not cur_game.checkLose(move, cur_game.ai_char):
            gameOver("Victory!")

        if len(cur_game.available_moves) == 0:
            gameOver("Dead heat!")


    # навешиваем метод на поля
    for item in ui.buttonGroup.buttons():
        item.clicked.connect(makeMove)

    ui.startButton.clicked.connect(startGame)
        

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
