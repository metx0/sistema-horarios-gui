from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
import sqlite3

class TeacherTable(QTableWidget):
    def __init__(self):
        super().__init__()

        self.con = sqlite3.connect("db_horario.db")
        self.cur = self.con.cursor()

        self.make_queries()
        self.make_table()

    def make_queries(self):
        self.resId = self.cur.execute("SELECT id_maestro from maestro")
        self.idMaestro = self.resId.fetchall()
        self.resName = self.cur.execute("SELECT nombre from maestro")
        self.nombre = self.resName.fetchall()
        self.resTipo = self.cur.execute("SELECT tipo_maestro from maestro")
        self.tipoMaestro = self.resTipo.fetchall()
        # Retorna tuplas, entonces, es necesario convertir a listas para acceder a valores
        self.teachers_data = [list(self.idMaestro), list(self.nombre), list(self.tipoMaestro)]

    def make_table(self):
        self.setRowCount(len(self.idMaestro))
        self.setColumnCount(len(self.teachers_data))
        self.setHorizontalHeaderLabels(["idMaestro", "nombre", "tipoMaestro"])
        self.fill_table()

    def fill_table(self):
        for i in range(len(self.idMaestro)):
            item_idMaestro = QTableWidgetItem(str(self.idMaestro[i][0]))
            item_nombre = QTableWidgetItem(self.nombre[i][0])
            item_tipoMaestro = QTableWidgetItem(str(self.tipoMaestro[i][0]))
            self.setItem(i, 0, item_idMaestro)
            self.setItem(i, 1, item_nombre)
            self.setItem(i, 2, item_tipoMaestro)

        self.resizeColumnsToContents()

class SubjectTable(QTableWidget):
    def __init__(self):
        super().__init__()

        self.con = sqlite3.connect("db_horario.db")
        self.cur = self.con.cursor()

        self.make_queries()
        self.make_table()

    def make_queries(self):
        self.resId = self.cur.execute("SELECT id_materia FROM materia")
        self.idMateria = self.resId.fetchall()
        self.resName = self.cur.execute("SELECT nombre FROM materia")
        self.nombre = self.resName.fetchall()
        self.subjects_data = [list(self.idMateria), list(self.nombre)]

    def make_table(self):
        self.setRowCount(len(self.idMateria))
        self.setColumnCount(len(self.subjects_data))
        self.setHorizontalHeaderLabels(["idMateria", "nombre"])
        self.fill_table()

    def fill_table(self):
        for i in range(len(self.idMateria)):
            item_idMateria = QTableWidgetItem(str(self.idMateria[i][0]))
            item_nombre = QTableWidgetItem(self.nombre[i][0])
            self.setItem(i, 0, item_idMateria)
            self.setItem(i, 1, item_nombre)
        
        self.resizeColumnsToContents()
