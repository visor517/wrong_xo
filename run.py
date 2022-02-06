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

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
