import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QPushButton,
)

# Used for text alignment
from PyQt5.QtCore import Qt
from tableWidget import DataTable


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Sistema escolar de horarios")

        # Main layout (vertical, for the menu bar and the content)
        self.main_layout = QVBoxLayout()

        # Create the buttons (elements of the header)
        self.show_tables_button = QPushButton("Ver tablas")
        self.show_schedule_button = QPushButton("Generar horario")

        # Create the title
        self.title = QLabel("Sistema escolar para generar horarios")

        # Give it an "id"
        self.title.setObjectName("title")
        # Center it horizontally
        self.title.setAlignment(Qt.AlignHCenter)

        self.main_layout.addWidget(self.title)
        self.setLayout(self.main_layout)

        self.showMaximized()


def main():
    app = QApplication(sys.argv)

    # Load the QSS (Qt Style Sheet) file
    with open("styles.qss", "r") as f:
        app.setStyleSheet(f.read())

    # Create an instance of the main window
    main_window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    