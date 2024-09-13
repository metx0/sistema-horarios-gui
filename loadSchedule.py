from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QSizePolicy, QSpacerItem
from PyQt5.QtCore import Qt
from algo import genetic
import threading

class LoadSchedule(QWidget):
    def __init__(self):
        super().__init__()
        
        title_label = QLabel("Genera un horario en base a los datos cargados")
        title_label.setObjectName("title-schedule")
        title_label.setAlignment(Qt.AlignHCenter)

        generate_btn = QPushButton("Generar horario")
        generate_btn.setObjectName("generate-btn")
        generate_btn.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        # Add event
        generate_btn.clicked.connect(self.generate_schedule)

        layout = QVBoxLayout()
        
        # Añadir espaciador arriba del título
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        # Añadir el título
        layout.addWidget(title_label)

        # Añadir espaciador arriba del botón
        layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Fixed))
        
        # Añadir el botón centrado
        layout.addWidget(generate_btn, alignment=Qt.AlignCenter)

        # Añadir espaciador debajo del botón
        layout.addSpacerItem(QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(layout)

    def generate_schedule(self):
        # run the algorithm in a separate thread
        new_thread = threading.Thread(target=genetic.main)
        new_thread.start()
