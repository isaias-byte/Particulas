# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(758, 556)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionGrafo = QAction(MainWindow)
        self.actionGrafo.setObjectName(u"actionGrafo")
        self.actionRecorrido_Profundidad_Amplitud = QAction(MainWindow)
        self.actionRecorrido_Profundidad_Amplitud.setObjectName(u"actionRecorrido_Profundidad_Amplitud")
        self.actionPrim = QAction(MainWindow)
        self.actionPrim.setObjectName(u"actionPrim")
        self.actionKruskal = QAction(MainWindow)
        self.actionKruskal.setObjectName(u"actionKruskal")
        self.actionDijkstra = QAction(MainWindow)
        self.actionDijkstra.setObjectName(u"actionDijkstra")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.blue_color_spinBox = QSpinBox(self.groupBox)
        self.blue_color_spinBox.setObjectName(u"blue_color_spinBox")
        self.blue_color_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.blue_color_spinBox, 11, 1, 1, 2)

        self.rojo = QLabel(self.groupBox)
        self.rojo.setObjectName(u"rojo")

        self.gridLayout.addWidget(self.rojo, 9, 0, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 14, 0, 1, 3)

        self.red_color_spinBox = QSpinBox(self.groupBox)
        self.red_color_spinBox.setObjectName(u"red_color_spinBox")
        self.red_color_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.red_color_spinBox, 9, 1, 1, 2)

        self.origen_x_spinBox = QSpinBox(self.groupBox)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origen_x_spinBox, 2, 1, 1, 2)

        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(999999999)

        self.gridLayout.addWidget(self.velocidad_spinBox, 7, 1, 1, 2)

        self.origen_y_spinBox = QSpinBox(self.groupBox)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origen_y_spinBox, 3, 1, 1, 2)

        self.id = QLabel(self.groupBox)
        self.id.setObjectName(u"id")

        self.gridLayout.addWidget(self.id, 1, 0, 1, 1)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 13, 0, 1, 3)

        self.verde = QLabel(self.groupBox)
        self.verde.setObjectName(u"verde")

        self.gridLayout.addWidget(self.verde, 10, 0, 1, 1)

        self.azul = QLabel(self.groupBox)
        self.azul.setObjectName(u"azul")

        self.gridLayout.addWidget(self.azul, 11, 0, 1, 1)

        self.destinoY = QLabel(self.groupBox)
        self.destinoY.setObjectName(u"destinoY")

        self.gridLayout.addWidget(self.destinoY, 6, 0, 1, 1)

        self.origenX = QLabel(self.groupBox)
        self.origenX.setObjectName(u"origenX")

        self.gridLayout.addWidget(self.origenX, 2, 0, 1, 1)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMaximum(999999999)

        self.gridLayout.addWidget(self.id_spinBox, 1, 1, 1, 2)

        self.destino_y_spinBox = QSpinBox(self.groupBox)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destino_y_spinBox, 6, 1, 1, 2)

        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout.addWidget(self.agregar_final_pushButton, 12, 0, 1, 3)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.velocidad = QLabel(self.groupBox)
        self.velocidad.setObjectName(u"velocidad")

        self.gridLayout.addWidget(self.velocidad, 7, 0, 1, 1)

        self.destinoX = QLabel(self.groupBox)
        self.destinoX.setObjectName(u"destinoX")

        self.gridLayout.addWidget(self.destinoX, 5, 0, 1, 1)

        self.origenY = QLabel(self.groupBox)
        self.origenY.setObjectName(u"origenY")

        self.gridLayout.addWidget(self.origenY, 3, 0, 1, 1)

        self.green_color_spinBox = QSpinBox(self.groupBox)
        self.green_color_spinBox.setObjectName(u"green_color_spinBox")
        self.green_color_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.green_color_spinBox, 10, 1, 1, 2)

        self.destino_x_spinBox = QSpinBox(self.groupBox)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destino_x_spinBox, 5, 1, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 4, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.salida_plainTextEdit = QPlainTextEdit(self.tab)
        self.salida_plainTextEdit.setObjectName(u"salida_plainTextEdit")

        self.gridLayout_2.addWidget(self.salida_plainTextEdit, 1, 1, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)

        self.algoritmos_plainTextEdit = QPlainTextEdit(self.tab)
        self.algoritmos_plainTextEdit.setObjectName(u"algoritmos_plainTextEdit")

        self.gridLayout_2.addWidget(self.algoritmos_plainTextEdit, 3, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_4.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.buscar_tabla_pushButton = QPushButton(self.tab_2)
        self.buscar_tabla_pushButton.setObjectName(u"buscar_tabla_pushButton")

        self.gridLayout_4.addWidget(self.buscar_tabla_pushButton, 1, 1, 1, 1)

        self.ordenar_distan_pushButton = QPushButton(self.tab_2)
        self.ordenar_distan_pushButton.setObjectName(u"ordenar_distan_pushButton")

        self.gridLayout_4.addWidget(self.ordenar_distan_pushButton, 3, 1, 1, 1)

        self.tabla_tableWidget = QTableWidget(self.tab_2)
        self.tabla_tableWidget.setObjectName(u"tabla_tableWidget")

        self.gridLayout_4.addWidget(self.tabla_tableWidget, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.ordenar_id_pushButton = QPushButton(self.tab_2)
        self.ordenar_id_pushButton.setObjectName(u"ordenar_id_pushButton")

        self.gridLayout_4.addWidget(self.ordenar_id_pushButton, 2, 1, 1, 1)

        self.ordenar_veloci_pushButton = QPushButton(self.tab_2)
        self.ordenar_veloci_pushButton.setObjectName(u"ordenar_veloci_pushButton")

        self.gridLayout_4.addWidget(self.ordenar_veloci_pushButton, 2, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar_pushButton = QPushButton(self.tab_3)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")

        self.gridLayout_5.addWidget(self.dibujar_pushButton, 1, 0, 1, 1)

        self.limpiar_pushButton = QPushButton(self.tab_3)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout_5.addWidget(self.limpiar_pushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 758, 21))
        self.menuArchivo = QMenu(self.menuBar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuVer = QMenu(self.menuBar)
        self.menuVer.setObjectName(u"menuVer")
        self.menuAlgoritmos = QMenu(self.menuBar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuVer.menuAction())
        self.menuBar.addAction(self.menuAlgoritmos.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuVer.addAction(self.actionGrafo)
        self.menuAlgoritmos.addAction(self.actionRecorrido_Profundidad_Amplitud)
        self.menuAlgoritmos.addAction(self.actionPrim)
        self.menuAlgoritmos.addAction(self.actionKruskal)
        self.menuAlgoritmos.addAction(self.actionDijkstra)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionGrafo.setText(QCoreApplication.translate("MainWindow", u"Grafo", None))
#if QT_CONFIG(shortcut)
        self.actionGrafo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.actionRecorrido_Profundidad_Amplitud.setText(QCoreApplication.translate("MainWindow", u"Busqueda (Profundidad/Amplitud)", None))
        self.actionPrim.setText(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.actionKruskal.setText(QCoreApplication.translate("MainWindow", u"Kruskal", None))
        self.actionDijkstra.setText(QCoreApplication.translate("MainWindow", u"Dijkstra", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edcula", None))
        self.rojo.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.id.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.verde.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.azul.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.destinoY.setText(QCoreApplication.translate("MainWindow", u"Destino en y:", None))
        self.origenX.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Color (RGB):", None))
        self.velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.destinoX.setText(QCoreApplication.translate("MainWindow", u"Destino en x:", None))
        self.origenY.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n Registrada", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Salida", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.buscar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.ordenar_distan_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Distancia", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el Id", None))
        self.ordenar_id_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Id", None))
        self.ordenar_veloci_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por velocidad", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuVer.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
    # retranslateUi

