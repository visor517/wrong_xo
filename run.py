import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from wrong_gui import Ui_MainWindow
from logic import Game

def main():

    # создаем графическое окружение
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    cur_game = Game('X', 'Y')

    def gameOver(message):
        msg = QMessageBox()
        msg.setText(message)
        msg.setWindowTitle("THE END")
        msg.exec_()

    # ход игрока
    def makeMove():
        field = app.sender()
        field.setText(cur_game.player_char)
        field.setEnabled(False)
        move = tuple([int(i) for i in field.objectName().split('_')[1:]])
        cur_game.makeMove(move, cur_game.player_char)
        if not cur_game.checkLose(move, cur_game.player_char):
            gameOver("Game over!")


    for item in list(ui.buttonGroup.buttons()):
        item.clicked.connect(makeMove)
        

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
