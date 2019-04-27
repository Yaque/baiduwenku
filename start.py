from PyQt5 import QtWidgets
import sys
from main_ui import Ui_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# pyinstaller -F -w --icon=icon.ico start.py -p main_ui.py --hidden-import Ui_MainWindow -p main_thread.py --hidden-import MyWorkThread -p WenKu.py --hidden-import BaikuSpider
