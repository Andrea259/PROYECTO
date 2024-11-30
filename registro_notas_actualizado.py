import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLabel, QMessageBox

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Información del Docente")
        self.setGeometry(100, 100, 400, 300)

        # Crear el layout principal
        layout = QVBoxLayout()

        # Etiquetas y campos para ingresar datos del docente
        self.docente_label = QLabel("Nombre del Docente:")
        self.docente_input = QLineEdit()

        self.materia_label = QLabel("Materia:")
        self.materia_combo = QComboBox()
        self.materia_combo.addItems(["Matemáticas", "Inglés", "Lenguaje", "Sociales", "Ciencias"]) 

        self.curso_label = QLabel("Curso:")
        self.curso_combo = QComboBox()
        self.curso_combo.addItems(["7°", "8°", "9°", "1° Bachillerato", "2° Bachillerato"]) 

        # Botón para ingresar
        self.ingresar_button = QPushButton("Ingresar")
        self.ingresar_button.clicked.connect(self.abrir_registro_notas)

        # Agregar widgets al layout
        layout.addWidget(self.docente_label)
        layout.addWidget(self.docente_input)
        layout.addWidget(self.materia_label)
        layout.addWidget(self.materia_combo)
        layout.addWidget(self.curso_label)
        layout.addWidget(self.curso_combo)
        layout.addWidget(self.ingresar_button)

        # Crear un widget central y asignarle el layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

     # Aplicar estilo CSS
        self.setStyleSheet("""
            QWidget {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
            }
            QLabel {
                font-size: 14px;
                margin-bottom: 5px;
            }
            QLineEdit, QComboBox, QPushButton {
                padding: 8px;
                font-size: 14px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QLineEdit:focus, QComboBox:focus {
                border-color: #007BFF;
            }
            QPushButton {
                background-color: #007BFF;
                color: white;
                border: none;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QComboBox {
                background-color: white;
                color: #333;
            }
            QTableWidget {
                background-color: white;
                border-radius: 5px;
                border: 1px solid #ccc;
                margin-top: 10px;
            }
            QTableWidgetItem {
                padding: 5px;
            }
        """)

    def abrir_registro_notas(self):
        # Validar que todos los campos estén llenos
        if self.docente_input.text() and self.materia_combo.currentText() and self.curso_combo.currentText():
            # Cerrar esta ventana y abrir la de RegistroNotas
            self.registro_notas = RegistroNotas()
            self.registro_notas.show()
            self.close()
        else:
            # Mostrar un mensaje de error si hay campos vacíos
            QMessageBox.warning(self, "Error", "Por favor complete todos los campos.")


class RegistroNotas(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Registro de Notas")
        self.setGeometry(100, 100, 600, 400)

        # Crear el layout principal
        layout = QVBoxLayout()

        # Selección de estudiante
        self.estudiante_label = QLabel("Estudiante:")
        self.estudiante_combo = QLineEdit()

        # Selección de periodo
        self.periodo_label = QLabel("Periodo:")
        self.periodo_combo = QComboBox()
        self.periodo_combo.addItems(["Trimestre 1", "Trimestre 2", "Trimestre 3"])  # Ejemplo de periodos

        # Selección de tipo de evaluación
        self.tipo_eval_label = QLabel("Tipo de Evaluación:")
        self.tipo_eval_combo = QComboBox()
        self.tipo_eval_combo.addItems(["Examen", "Tareas", "Proyecto"])  # Ejemplo de tipos de evaluación

        # Entrada de la nota
        self.nota_label = QLabel("Nota:")
        self.nota_input = QLineEdit()

        # Botón para guardar y eliminar
        self.save_button = QPushButton("Guardar Nota")
        self.save_button.clicked.connect(self.guardar_nota)

        self.delete_button = QPushButton("Eliminar Nota")
        self.delete_button.clicked.connect(self.eliminar_nota)


        # Tabla para mostrar notas
        self.table = QTableWidget(0, 4)  # 4 columnas para estudiante, periodo, tipo de evaluación, nota
        self.table.setHorizontalHeaderLabels(["Estudiante", "Periodo", "Evaluación", "Nota"])

        # Organizar widgets en el layout
        layout.addWidget(self.estudiante_label)
        layout.addWidget(self.estudiante_combo)
        layout.addWidget(self.periodo_label)
        layout.addWidget(self.periodo_combo)
        layout.addWidget(self.tipo_eval_label)
        layout.addWidget(self.tipo_eval_combo)
        layout.addWidget(self.nota_label)
        layout.addWidget(self.nota_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.table)

        # Crear un widget central y asignarle el layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Aplicar estilo CSS
        self.setStyleSheet("""
            QWidget {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
            }
            QLabel {
                font-size: 14px;
                margin-bottom: 5px;
            }
            QLineEdit, QComboBox, QPushButton {
                padding: 8px;
                font-size: 14px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QLineEdit:focus, QComboBox:focus {
                border-color: #007BFF;
            }
            QPushButton {
                background-color: #28a745;
                color: white;
                border: none;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #218838;
            }
            QComboBox {
                background-color: white;
                color: #333;
            }
            QTableWidget {
                background-color: white;
                border-radius: 5px;
                border: 1px solid #ccc;
                margin-top: 10px;
            }
            QTableWidgetItem {
                padding: 5px;
            }
            QHeaderView::section {
                background-color: #007BFF;
                color: white;
                padding: 5px;
            }
        """)

    def guardar_nota(self):
        # Obtener los datos ingresados
        estudiante = self.estudiante_combo.text()
        periodo = self.periodo_combo.currentText()
        tipo_eval = self.tipo_eval_combo.currentText()
        nota = self.nota_input.text()

        # Verificar que la nota sea válida
        if nota.isdigit() and 0 <= int(nota) <= 10:
            # Agregar los datos a la tabla
            fila = self.table.rowCount()
            self.table.insertRow(fila)
            self.table.setItem(fila, 0, QTableWidgetItem(estudiante))
            self.table.setItem(fila, 1, QTableWidgetItem(periodo))
            self.table.setItem(fila, 2, QTableWidgetItem(tipo_eval))
            self.table.setItem(fila, 3, QTableWidgetItem(nota))

            # Limpiar los campos de entrada
            self.estudiante_combo.clear()
            self.nota_input.clear()
        else:
            # Mostrar un mensaje de error
            QMessageBox.warning(self, "Error", "Ingrese una nota válida entre 0 y 10.")

    def eliminar_nota(self):
        # Obtener la fila seleccionada
        fila_seleccionada = self.table.currentRow()
        if fila_seleccionada >= 0:
            self.table.removeRow(fila_seleccionada)
        else:
            QMessageBox.warning(self, "Error", "Seleccione una fila para eliminar.")

# Código para ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication([])  # Se debe pasar un argumento, por ejemplo sys.argv, pero para simplificar dejamos [].
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    app.exec_()
