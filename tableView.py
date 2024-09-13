from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem
import sqlite3
import sys

# TODO: mejorar las tablas para que se puedan usar con otra info.

con = sqlite3.connect("db_horario.db")
cur = con.cursor()

app = QApplication(sys.argv)

resId = cur.execute("SELECT id_maestro from maestro")
idMaestro = resId.fetchall()
resName = cur.execute("SELECT nombre from maestro")
nombre = resName.fetchall()
resTipo = cur.execute("SELECT tipo_maestro from maestro")
tipoMaestro = resTipo.fetchall()
# Retorna tuplas, entonces, es necesario convertir a listas para acceder a valores
teachers_data = [list(idMaestro), list(nombre), list(tipoMaestro)]

table = QTableWidget()

# print(teachers_data)

table.setRowCount(len(idMaestro))
table.setColumnCount(len(teachers_data))
table.setHorizontalHeaderLabels(["idMaestro", "nombre", "tipoMaestro"])

for i in range(len(teachers_data)):
    item_idMaestro = QTableWidgetItem(idMaestro[i][0])
    item_nombre = QTableWidgetItem(nombre[i][0])
    item_tipoMaestro = QTableWidgetItem(tipoMaestro[i][0])
    # Add items to the table.
    table.setItem(i, 0, item_idMaestro)
    table.setItem(i, 1, item_nombre)
    table.setItem(i, 2, item_tipoMaestro)

table.show()
sys.exit(app.exec())
