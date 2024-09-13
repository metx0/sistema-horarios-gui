import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
# Used for text alignment
from PyQt5.QtCore import Qt
from tableView import TeacherTable

app = QApplication(sys.argv)

# Load the QSS (Qt Style Sheet) file
with open("styles.qss", "r") as f:
    app.setStyleSheet(f.read())

# Create the main window
window = QWidget()
window.setWindowTitle("Sistema escolar de horarios")

# Create the title
title = QLabel("Sistema escolar para generar horarios", window)

# Give it an "id"
title.setObjectName("title")

# Center it horizontally
title.setAlignment(Qt.AlignHCenter)

# Create a VBox layout to place the title
vbox = QVBoxLayout()
vbox.addWidget(title)
vbox.addWidget(TeacherTable())
window.setLayout(vbox)

window.showMaximized()

sys.exit(app.exec_())
