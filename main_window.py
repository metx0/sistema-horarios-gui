from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout
from PyQt5.uic import loadUi
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("ui/menu_bar.ui", self)

        with open("styles.qss", "r") as f:
            self.setStyleSheet(f.read())

        self.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()
