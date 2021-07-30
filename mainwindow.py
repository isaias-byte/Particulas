from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import SLOT, Slot
from PySide2.QtGui import QPen, QColor, QTransform
from ui_mainwindow import Ui_MainWindow
from adminParticulas_21A.adminparticulas import AdminParticulas
from adminParticulas_21A.particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.adminParticulas = AdminParticulas()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene()
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_tabla_pushButton.clicked.connect(self.buscar_tabla)

        self.ui.dibujar_pushButton.clicked.connect(self.dibujar)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)
        self.ui.graphicsView.setScene(self.scene)

        self.ui.ordenar_id_pushButton.clicked.connect(self.ordenar_id)
        self.ui.ordenar_distan_pushButton.clicked.connect(self.ordenar_distancia)
        self.ui.ordenar_veloci_pushButton.clicked.connect(self.ordenar_velocidad)

        self.ui.actionGrafo.triggered.connect(self.action_grafo)
        self.ui.actionRecorrido_Profundidad_Amplitud.triggered.connect(self.action_recorrido_profundidad_amplitud)
        self.ui.actionPrim.triggered.connect(self.action_prim)

        self.ui.actionKruskal.triggered.connect(self.action_kruskal)

        self.ui.actionDijkstra.triggered.connect(self.action_dijkstra)

    @Slot()
    def action_dijkstra(self):
        #print("Dijkstra")
        grafoAux = dict()
        origen = (self.ui.origen_x_spinBox.value(), self.ui.origen_y_spinBox.value())
        destino = (self.ui.destino_x_spinBox.value(), self.ui.destino_y_spinBox.value())
        destinoAux = destino
        grafoAux = self.adminParticulas.algoritmo_dijkstra(origen)
        if self.adminParticulas.algoritmo_dijkstra(origen) and destinoAux in grafoAux:
            pen = QPen()
            pen.setWidth(2)
            red = 228
            green = 0
            blue = 124
            
            color = QColor(red, green, blue)
            pen.setColor(color)
            
            self.limpiar()
            while destino != origen:
                destinoAux = destino
                destinoAux_x = destino[0]
                destinoAux_y = destino[1]
                self.scene.addEllipse(destinoAux_x, destinoAux_y, 3, 3, pen)
                destino = grafoAux[destinoAux]
                destino_x = destino[0]
                destino_y = destino[1]

                self.scene.addEllipse(destino_x, destino_y, 3, 3, pen)
                self.scene.addLine(destinoAux_x, destinoAux_y, destino_x, destino_y, pen)
        else:
            QMessageBox.critical(
                self, 
                "Error",
                "No es posible leer los valores (Origen en x e y, Destino en x e y)"
            )

    @Slot()
    def action_kruskal(self):
        #print("Kruskal")
        grafoAux = self.adminParticulas.algoritmo_kruskal()
        pen = QPen()
        pen.setWidth(2)
        red = 228
        green = 0
        blue = 124
        
        color = QColor(red, green, blue)
        pen.setColor(color)
        
        for origen, dic in grafoAux.items():
            #print(particula)
            #print(dis)
            lista = dic
            origen_x = origen[0]
            origen_y = origen[1]
            for destino, distancia in lista:
                destino_x = destino[0]
                destino_y = destino[1]

                self.scene.addEllipse(origen_x, origen_y, 3, 3, pen)
                self.scene.addEllipse(destino_x, destino_y, 3, 3, pen)
                self.scene.addLine(origen_x, origen_y, destino_x, destino_y, pen)

    @Slot()
    def action_prim(self):
        #print("Prim")
        grafoAux = dict()
        origen = (self.ui.origen_x_spinBox.value(), self.ui.origen_y_spinBox.value())
        #grafoAux = self.adminParticulas.algoritmo_prim(origen)

        if self.adminParticulas.algoritmo_prim(origen):
            
            grafoAux = self.adminParticulas.algoritmo_prim(origen)
            pen = QPen()
            pen.setWidth(2)
            red = 228
            green = 0
            blue = 124
            
            color = QColor(red, green, blue)
            pen.setColor(color)
            
            
            for origen, dic in grafoAux.items():
                #print(particula)
                #print(dis)
                lista = dic
                origen_x = origen[0]
                origen_y = origen[1]
                for destino, distancia in lista:
                    destino_x = destino[0]
                    destino_y = destino[1]

                    self.scene.addEllipse(origen_x, origen_y, 3, 3, pen)
                    self.scene.addEllipse(destino_x, destino_y, 3, 3, pen)
                    self.scene.addLine(origen_x, origen_y, destino_x, destino_y, pen)
            
        else:
            QMessageBox.critical(
                self, 
                "Error",
                "No es posible leer los valores..."
            )


    @Slot()
    def action_grafo(self):
        #print("Grafo")
        self.ui.salida_plainTextEdit.clear()
        self.ui.algoritmos_plainTextEdit.clear()
        self.ui.salida_plainTextEdit.insertPlainText(str(self.adminParticulas))
        self.ui.algoritmos_plainTextEdit.insertPlainText(self.adminParticulas.imprimir_grafo())


    @Slot()
    def action_recorrido_profundidad_amplitud(self):
        #print("Recorrido")
        origen = (self.ui.origen_x_spinBox.value(), self.ui.origen_y_spinBox.value())
        self.ui.algoritmos_plainTextEdit.clear()
        
        if self.adminParticulas.recorrido_profundidad(origen) and self.adminParticulas.recorrido_amplitud(origen):
            self.ui.algoritmos_plainTextEdit.insertPlainText("Origen: " + str(origen) + '\n')
            self.ui.algoritmos_plainTextEdit.insertPlainText("Profundidad" + '\n' +
                                                            self.adminParticulas.recorrido_profundidad(origen))
            self.ui.algoritmos_plainTextEdit.insertPlainText('\n' + "Amplitud" + '\n' +
                                                            self.adminParticulas.recorrido_amplitud(origen))

            #print("Origen: " + str(origen) + '\n' + self.adminParticulas.recorrido_profundidad(origen)
            #    + '\n' + self.adminParticulas.recorrido_amplitud(origen))

        else:
            QMessageBox.critical(
                self, 
                "Error",
                "No es posible leer los valores..."
            )
        #self.ui.algoritmos_plainTextEdit.insertPlainText(self.adminParticulas.recorrido_profundidad(origen))

    @Slot()
    def ordenar_id(self):
        #print("ordenar id")
        self.adminParticulas.ordenar_particulas_id()

    @Slot()
    def ordenar_distancia(self):
        #print("ordenar distancia")
        self.adminParticulas.ordenar_particulas_distancia()
    
    @Slot()
    def ordenar_velocidad(self):
        #print("ordenar velocidad")
        self.adminParticulas.ordenar_particulas_velocidad()

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def dibujar(self):
        #print("dibujar")
        pen = QPen()
        pen.setWidth(2)

        for particula in self.adminParticulas:
            red = particula.red
            blue = particula.blue
            green = particula.green

            color = QColor(red, green, blue)
            pen.setColor(color)

            origen_x = particula.origen_x
            origen_y = particula.origen_y
            destino_x = particula.destino_x
            destino_y = particula.destino_y

            self.scene.addEllipse(origen_x, origen_y, 3, 3, pen)
            self.scene.addEllipse(destino_x, destino_y, 3, 3, pen)
            self.scene.addLine(origen_x, origen_y, destino_x, destino_y, pen)
        

    @Slot()
    def limpiar(self):
        #print("limpiar")
        self.scene.clear()
    

    @Slot()
    def buscar_tabla(self):
        #print("buscar_tabla")
        id = self.ui.buscar_lineEdit.text()

        encontrado = False
        if id.isdigit():
            for particula in self.adminParticulas:
                if id == str(particula.id):
                    self.ui.tabla_tableWidget.clear()
                    self.ui.tabla_tableWidget.setColumnCount(10)
                    self.ui.tabla_tableWidget.setRowCount(1)
                    headers = ["Id", "Origen en x", "Origen en y", 
                        "Destino en x", "Destino en y", "Velocidad",
                        "Rojo", "Verde", "Azul", "Distancia"]
                    self.ui.tabla_tableWidget.setHorizontalHeaderLabels(headers)

                    id_widget = QTableWidgetItem(str(particula.id))
                    origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                    origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                    destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                    destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                    velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                    red_widget = QTableWidgetItem(str(particula.red))
                    green_widget = QTableWidgetItem(str(particula.green))
                    blue_widget = QTableWidgetItem(str(particula.blue))
                    distancia_widget = QTableWidgetItem(str(particula.distancia))

                    self.ui.tabla_tableWidget.setItem(0, 0, id_widget)
                    self.ui.tabla_tableWidget.setItem(0, 1, origen_x_widget)
                    self.ui.tabla_tableWidget.setItem(0, 2, origen_y_widget)
                    self.ui.tabla_tableWidget.setItem(0, 3, destino_x_widget)
                    self.ui.tabla_tableWidget.setItem(0, 4, destino_y_widget)
                    self.ui.tabla_tableWidget.setItem(0, 5, velocidad_widget)
                    self.ui.tabla_tableWidget.setItem(0, 6, red_widget)
                    self.ui.tabla_tableWidget.setItem(0, 7, green_widget)
                    self.ui.tabla_tableWidget.setItem(0, 8, blue_widget)
                    self.ui.tabla_tableWidget.setItem(0, 9, distancia_widget)
                    encontrado = True
                    return
            if not encontrado:
                QMessageBox.warning(
                    self,
                    "Atención",
                    f'La partícula con id "{id}" no fue encontrada'
                )
        else:
            QMessageBox.warning(
                self,
                "Atención",
                "El id debe contener sólo caracteres numéricos"
            )


    @Slot()
    def mostrar_tabla(self):
        #print("mostrar_tabla")
        self.ui.tabla_tableWidget.setColumnCount(10)
        headers = ["Id", "Origen en x", "Origen en y", 
                    "Destino en x", "Destino en y", "Velocidad",
                    "Rojo", "Verde", "Azul", "Distancia"]
        self.ui.tabla_tableWidget.setHorizontalHeaderLabels(headers)

        self.ui.tabla_tableWidget.setRowCount(len(self.adminParticulas))
        row = 0
        for particula in self.adminParticulas:
            #print(particula)
            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla_tableWidget.setItem(row, 0, id_widget)
            self.ui.tabla_tableWidget.setItem(row, 1, origen_x_widget)
            self.ui.tabla_tableWidget.setItem(row, 2, origen_y_widget)
            self.ui.tabla_tableWidget.setItem(row, 3, destino_x_widget)
            self.ui.tabla_tableWidget.setItem(row, 4, destino_y_widget)
            self.ui.tabla_tableWidget.setItem(row, 5, velocidad_widget)
            self.ui.tabla_tableWidget.setItem(row, 6, red_widget)
            self.ui.tabla_tableWidget.setItem(row, 7, green_widget)
            self.ui.tabla_tableWidget.setItem(row, 8, blue_widget)
            self.ui.tabla_tableWidget.setItem(row, 9, distancia_widget)
            row += 1

    @Slot()
    def action_abrir_archivo(self):
        #print("Abrir Archivo")
        ubicacion = QFileDialog.getOpenFileName(
            self,
            "Abrir archivo",
            ".",
            "JSON (*.json)"
        )[0]
        #print(ubicacion)
        if self.adminParticulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Abrir",
                "Archivo abierto con éxito" + '\n' + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo" + ubicacion
            )
        

    @Slot()
    def action_guardar_archivo(self):
        #print("Guardar Archivo")
        ubicacion = QFileDialog.getSaveFileName(
            self,
            "Guardar Archivo",
            ".",
            "JSON (*.json)"
        )[0]
        #print(ubicacion)
        if self.adminParticulas.guardarParticulas(ubicacion):
            QMessageBox.information(
                self,
                "Guardado con éxito", 
                "Archivo creado con éxito" + '\n' + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al crear el archivo " + ubicacion
            )
    
    @Slot()
    def click_mostrar(self):
        #self.adminParticulas.mostrar()
        self.ui.salida_plainTextEdit.clear()
        self.ui.algoritmos_plainTextEdit.clear()
        self.ui.salida_plainTextEdit.insertPlainText(str(self.adminParticulas))
        self.ui.algoritmos_plainTextEdit.insertPlainText(self.adminParticulas.imprimir_grafo())
        #self.adminParticulas.imprimir_grafo()

    @Slot()
    def click_agregar_final(self):
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red_color = self.ui.red_color_spinBox.value()
        green_color = self.ui.green_color_spinBox.value()
        blue_color = self.ui.blue_color_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, 
                            destino_y, velocidad, red_color,
                            green_color, blue_color)
        self.adminParticulas.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):  
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red_color = self.ui.red_color_spinBox.value()
        green_color = self.ui.green_color_spinBox.value()
        blue_color = self.ui.blue_color_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, 
                            destino_y, velocidad, red_color,
                            green_color, blue_color)
        self.adminParticulas.agregar_inicio(particula)