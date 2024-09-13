import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QStackedWidget
# Used for text alignment
from PyQt5.QtCore import Qt
from tableView import TeacherTable, SubjectTable
from navBar import NavBar
from loadSchedule import LoadSchedule

app = QApplication(sys.argv)

# Load the QSS (Qt Style Sheet) file
with open("qss/styles.qss", "r") as f:
    app.setStyleSheet(f.read())

# Create the main window
window = QWidget()
window.setWindowTitle("Sistema escolar de horarios")

# Create the title
title = QLabel("Sistema escolar de generación de horarios", window)

# Give it an "id"
title.setObjectName("title-window")

# Center it horizontally
title.setAlignment(Qt.AlignHCenter)

# Stack for page changing.
stackedPages = QStackedWidget()

layout = QVBoxLayout()
layout.addWidget(title)
nav = NavBar(stackedPages)
layout.addWidget(nav)

# View tables page.
table_page = QWidget()
table_layout = QVBoxLayout()
table_layout.addWidget(TeacherTable())
table_layout.addWidget(SubjectTable())
table_page.setLayout(table_layout)

# Schedule generator page.
gen_page = QWidget()
gen_layout = QVBoxLayout()
gen_layout.addWidget(LoadSchedule())
gen_page.setLayout(gen_layout)

# Add widgets to stack.
stackedPages.addWidget(table_page)
stackedPages.addWidget(gen_page)

layout.addWidget(stackedPages)

window.setLayout(layout)

window.showMaximized()

sys.exit(app.exec_())
