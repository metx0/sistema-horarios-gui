from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QSizePolicy, QSpacerItem

# Buttons that show the other windows (widgets)
class NavBar(QWidget):    
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        
        generate_view_btn = QPushButton('Generar horarios')
        tables_view_btn = QPushButton('Ver tablas')

        layout = QHBoxLayout()

        generate_view_btn.clicked.connect(self.switch_to_generate)
        tables_view_btn.clicked.connect(self.switch_to_tables)

        layout.addWidget(generate_view_btn)
        layout.addWidget(tables_view_btn)

        # Push the buttons to the left
        spacer = QSpacerItem(500, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addSpacerItem(spacer)

        self.setLayout(layout)

    def switch_to_tables(self):
        self.stack.setCurrentIndex(0)

    def switch_to_generate(self):
        self.stack.setCurrentIndex(1)

