from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

# un boton para despues proceder a aparecer una animacion de carga.
class LoadSchedule(QWidget):
    def __init__(self):
        super().__init__()
        
        title_label = QLabel("Generacion de horario")
        generate_btn = QPushButton("Generar horario")

        generate_btn.clicked.connect(self.loading_anim)

        layout = QVBoxLayout()
        
        layout.addWidget(title_label)
        layout.addWidget(generate_btn)
        
        title_label.setAlignment(Qt.AlignHCenter)

        self.setLayout(layout)

    def loading_anim(self):
        # el lugar de esta funcion iria la que genera horarios.
        print("cargando...")
