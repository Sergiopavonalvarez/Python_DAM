import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLineEdit, QAction, QLabel, QApplication

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo slot predefinido")
        self.setFixedSize(300, 300)  # Tamaño corregido

        self.mostrar_icon = QIcon("/04 Componentes de Usuario/QLineEdit/593374.png")
        self.line_edit1 = QLineEdit(self)

        # Fijamos el tamaño del line edit
        self.line_edit1.setFixedSize(150, 30)
        self.line_edit1.setMaxLength(25)

        # Crear la acción y conectarla al slot cambiar visibilidad
        self.accion_cambiar_visibilidad = QAction(self.mostrar_icon, "!Ejemplo¡", self)
        self.accion_cambiar_visibilidad.triggered.connect(self.cambiar_visibilidad)

        # Agregar la acción al QLineEdit
        self.line_edit1.addAction(self.accion_cambiar_visibilidad, QLineEdit.TrailingPosition)
        self.etiqueta1 = QLabel("self")
        self.etiqueta1.setFixedSize(150, 30)  # Establecemos el mismo tamaño que el QLineEdit
        self.etiqueta1.move(150, 0)

        # Conectamos el evento textChanged del LineEdit al slot setText del Label
        self.line_edit1.textChanged.connect(self.etiqueta1.setText)  # Corregido

    def cambiar_visibilidad(self):
        print("Hola mundo")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
