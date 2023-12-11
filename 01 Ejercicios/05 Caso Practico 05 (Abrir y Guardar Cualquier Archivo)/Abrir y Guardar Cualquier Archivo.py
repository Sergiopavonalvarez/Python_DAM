import sys
import platform
import os
from PySide6.QtCore import QCoreApplication, QFile, QIODevice
from PySide6.QtGui import QAction, QIcon, QTextCursor
from PySide6.QtWidgets import QApplication, QFileDialog, QTextEdit, QMainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de texto plano")
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        ruta_a_icono1 = os.path.join(os.path.dirname(__file__), "C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/01 Ejercicios/04 Ponte A Prueba 04 (Abrir y Guardar El Mismo Archivo)/abrir.png")
        ruta_a_icono3 = os.path.join(os.path.dirname(__file__), "C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/01 Ejercicios/04 Ponte A Prueba 04 (Abrir y Guardar El Mismo Archivo)/descarga.png")
        ruta_a_icono2 = os.path.join(os.path.dirname(__file__), "C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/01 Ejercicios/04 Ponte A Prueba 04 (Abrir y Guardar El Mismo Archivo)/salir.png")

        # Barra Menu
        barra_menu=self.menuBar()
        # Añadimos la opcion menu
        menu=barra_menu.addMenu("&Menu")
        # Creamos la accion
        accion_abrir=QAction(QIcon(ruta_a_icono1), "Abrir", self)
        accion_guardar=QAction(QIcon(ruta_a_icono3), "Guardar", self)
        accion_salir=QAction(QIcon(ruta_a_icono2), "Salir", self)
        # Conectamos la accion a la ranura
        accion_abrir.triggered.connect(self.openFile)
        accion_guardar.triggered.connect(self.saveFile)
        accion_salir.triggered.connect(self.cerrar)
        # Añadimos accion al menu
        menu.addAction(accion_abrir)
        menu.addAction(accion_guardar)
        menu.addAction(accion_salir)

        # WhatThis
        accion_abrir.setStatusTip("Abre el archivo")
        accion_guardar.setStatusTip("Guarda el archivo")
        accion_salir.setStatusTip("Sale del archivo")

        #Barra Herramientas
        barra_herramientas=QToolBar("Barra de herramientas")
        # Añadimos la accion a la barra de herramientas
        barra_herramientas.addAction(accion_abrir)
        barra_herramientas.addAction(accion_guardar)
        barra_herramientas.addAction(accion_salir)
        # Añadimos la barra de herramientas
        self.addToolBar(barra_herramientas)

        #Barra de estado
        barra_estado=self.statusBar()
        # Añadimos la barra de estado
        barra_estado.addPermanentWidget(QLabel(platform.system()))
        # Mostramos el mensaje
        barra_estado.showMessage("Cargando...",3000)
        self.archivo_abierto = None  # Inicializamos como None

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Text files (*.txt)")
        if filename:
            self.archivo_abierto = filename  # Actualizamos la variable global
            file = QFile(self.archivo_abierto)
            if file.open(QIODevice.ReadOnly):
                text = file.readAll().data().decode('utf-8')
                self.textEdit.setPlainText(text)
                file.close()

    def saveFile(self):
        if self.archivo_abierto:
            file = QFile(self.archivo_abierto)
            if file.open(QIODevice.WriteOnly):
                text = self.textEdit.toPlainText()
                file.write(text.encode())
                file.close()
        else:
            filename, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Text files (*.txt)")
            if filename:
                self.archivo_abierto = filename  # Actualizamos la variable global
                file = QFile(self.archivo_abierto)
                if file.open(QIODevice.WriteOnly):
                    text = self.textEdit.toPlainText()
                    file.write(text.encode())
                    file.close()



    def cerrar(self):
        global archivo_abierto
        archivo_abierto = None
        self.textEdit.setPlainText("")
        QCoreApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = App()
    ventana1.show()
    app.exec()