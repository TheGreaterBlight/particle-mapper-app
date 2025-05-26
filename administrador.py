from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsScene 
from PySide2.QtCore import Slot
from PySide2.QtGui import QColor, QPen, QBrush
import json 
import random
from mainwindow import Ui_MainWindow  
from particula import Particula  
from graficadorWindow import Ui_GraficadorWindow
from algoritmos import distancia_euclidiana 
from Utils import UnionFind, Graph

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.particulas = []  
        self.particulasTulpa = []
        self.puntos = []
        self.selected_particles = [] 

        self.ui.agregarInicioButton.clicked.connect(self.click_agregar_inicio)
        self.ui.agregaFinalButton.clicked.connect(self.click_agregar_final)
        self.ui.leerArchivoButton.clicked.connect(self.click_leer_archivo)
        self.ui.guardarSesionButton.clicked.connect(self.click_guardar_sesion)
        self.ui.busquedaButton.clicked.connect(self.click_busqueda)
        self.ui.refrescarButton.clicked.connect(self.click_refrescar)
        self.ui.generarListaAdyacenciaButton.clicked.connect(self.click_generar_lista_adyacencia)

        self.ui.abrirGraficadorButton.clicked.connect(lambda: self.click_graficador(show_only_points=False, show_nearest_points=False))
        self.ui.abrirGraficadorButtonButOnlyPointsButton.clicked.connect(lambda: self.click_graficador(show_only_points=True, show_nearest_points=False))
        self.ui.abrirGraficadorButtonButNearestPoints.clicked.connect(lambda: self.click_graficador(show_only_points=False, show_nearest_points=True))
        self.ui.abrirGraficadorButtonKrusk.clicked.connect(self.click_CallToKrusk)
        self.ui.abrirGraficadorButtonPrimm.clicked.connect(self.click_CallToPrimm)
    
    def puntos_mas_cercanos(self, puntos):
        nearest_pairs = []
        for i, punto_i in enumerate(puntos):
            nearest_dist = float('inf')
            closest_point = None
            for j, punto_j in enumerate(puntos):
                if i != j:
                    dist = distancia_euclidiana(punto_i[0], punto_i[1], punto_j[0], punto_j[1])  
                    if dist < nearest_dist:
                        nearest_dist = dist
                        closest_point = punto_j
            if closest_point:
                nearest_pairs.append((punto_i, closest_point))
        return nearest_pairs

    def tulpaRefresh(self, option):
        self.particulasTulpa = self.particulas[:]
        switch = {
            1: lambda p: p.id,
            2: lambda p: p.origen_x,
            3: lambda p: p.origen_y,
            4: lambda p: p.destino_x,
            5: lambda p: p.destino_y,
            6: lambda p: p.velocidad,
            7: lambda p: p.red,
            8: lambda p: p.green,
            9: lambda p: p.blue,
            10: lambda p: (-p.distancia)  
        }
        sort_key = switch.get(option, lambda p: p.id) 
        self.particulasTulpa.sort(key=sort_key)
        self.updateTablaConsole(self.particulasTulpa)

    def generate_random_id(self):
        return str(random.randint(1000, 9999))

    def updateTablaConsole(self, particulas_to_display=None):
        headers = ["ID", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.consolaTabla.setColumnCount(len(headers))
        self.ui.consolaTabla.setHorizontalHeaderLabels(headers)
        particles_to_show = particulas_to_display if particulas_to_display is not None else self.particulas
        self.ui.consolaTabla.setRowCount(len(particles_to_show))
        self.ui.consolaTabla.horizontalHeader().sectionClicked.connect(self.handle_header_click)
        for row, particula in enumerate(particles_to_show):
            self.ui.consolaTabla.setItem(row, 0, QTableWidgetItem(str(particula.id)))
            self.ui.consolaTabla.setItem(row, 1, QTableWidgetItem(str(particula.origen_x)))
            self.ui.consolaTabla.setItem(row, 2, QTableWidgetItem(str(particula.origen_y)))
            self.ui.consolaTabla.setItem(row, 3, QTableWidgetItem(str(particula.destino_x)))
            self.ui.consolaTabla.setItem(row, 4, QTableWidgetItem(str(particula.destino_y)))
            self.ui.consolaTabla.setItem(row, 5, QTableWidgetItem(str(particula.velocidad)))
            self.ui.consolaTabla.setItem(row, 6, QTableWidgetItem(str(particula.red)))
            self.ui.consolaTabla.setItem(row, 7, QTableWidgetItem(str(particula.green)))
            self.ui.consolaTabla.setItem(row, 8, QTableWidgetItem(str(particula.blue)))
            self.ui.consolaTabla.setItem(row, 9, QTableWidgetItem(str(particula.distancia)))
    
    def convertirParticulas(self):
        grafo = {}
        for particula in self.particulas:
            origen = (particula.origen_x, particula.origen_y)
            destino = (particula.destino_x, particula.destino_y)
            distancia = particula.distancia 

            if origen not in grafo:
                grafo[origen] = []
            if destino not in grafo:
                grafo[destino] = []

            grafo[origen].append((destino, distancia))
            grafo[destino].append((origen, distancia))

            print("Lista de Adyacencia:")
        for origen, destinos in grafo.items():
            formatted_destinos = [f"({d[0][0]}, {d[0][1]})" for d in destinos] 
            print(f"{origen}---> {formatted_destinos}")

        return grafo
    @Slot()
    def click_generar_lista_adyacencia(self):
        self.ui.thirdConsole.clear()
        grafo = self.convertirParticulas()
        for nodo, conexiones in grafo.items():
            self.ui.thirdConsole.appendPlainText(f"{nodo}: {conexiones}")

    @Slot()
    def click_gLimpiar(self):
        self.graficador_ui.gSearchBar.clear()  
        self.graficador_ui.scene.clear() 
        self.drawParticulas() 

    @Slot()
    def click_gBuscar(self):
        search_id = self.graficador_ui.gSearchBar.text()  
        filtered_particulas = [p for p in self.particulas if str(p.id) == search_id]
        
        if not filtered_particulas:
            QMessageBox.warning(self, "Advertencia", f"No se encontró ninguna partícula con ID: {search_id}")
        
        self.updateTablaConsole(filtered_particulas)  

    @Slot()
    def click_graficador(self, show_only_points=False, show_nearest_points=False):
        self.graficador_window = QMainWindow()  
        self.graficador_ui = Ui_GraficadorWindow()  
        self.graficador_ui.setupUi(self.graficador_window)  
        self.graficador_ui.scene = QGraphicsScene()  
        self.graficador_ui.graphicsView.setScene(self.graficador_ui.scene)
        self.graficador_window.show()   

        if show_nearest_points:
            self.drawParticulasButOnlyNearestPoints()  
        elif show_only_points:
            self.drawParticulasButOnlyPoints()  
        else:
            self.drawParticulas()  

        self.graficador_ui.gLimpiarButton.clicked.connect(self.click_gLimpiar)
        self.graficador_ui.gBuscarButton.clicked.connect(self.click_gBuscar)
    @Slot()
    def click_CallToPrimm(self):
        self.graficador_window = QMainWindow()  
        self.graficador_ui = Ui_GraficadorWindow()  
        self.graficador_ui.setupUi(self.graficador_window)  
        self.graficador_ui.scene = QGraphicsScene()  
        self.graficador_ui.graphicsView.setScene(self.graficador_ui.scene)
        self.graficador_window.show() 

        self.drawPrimmParticles()

        self.graficador_ui.gLimpiarButton.clicked.connect(self.click_gLimpiar)
        self.graficador_ui.gBuscarButton.clicked.connect(self.click_gBuscar)
    @Slot()
    def click_CallToKrusk(self):
        self.graficador_window = QMainWindow()  
        self.graficador_ui = Ui_GraficadorWindow()  
        self.graficador_ui.setupUi(self.graficador_window)  
        self.graficador_ui.scene = QGraphicsScene()  
        self.graficador_ui.graphicsView.setScene(self.graficador_ui.scene)
        self.graficador_window.show() 

        self.drawKruskalParticles()

        self.graficador_ui.gLimpiarButton.clicked.connect(self.click_gLimpiar)
        self.graficador_ui.gBuscarButton.clicked.connect(self.click_gBuscar)
    @Slot()
    def drawKruskalParticles(self):
        self.scene = QGraphicsScene()
        self.graficador_ui.graphicsView.setScene(self.scene)
        edges = []
        for i, particula_i in enumerate(self.particulas):
            for j, particula_j in enumerate(self.particulas):
                if i < j:  
                    distance = ((particula_i.origen_x - particula_j.origen_x) ** 2 + 
                                (particula_i.origen_y - particula_j.origen_y) ** 2) ** 0.5
                    edges.append((distance, i, j))
        edges.sort()
        uf = UnionFind(len(self.particulas))
        mst_edges = []
        for distance, i, j in edges:
            if uf.union(i, j):
                mst_edges.append((self.particulas[i], self.particulas[j], distance))
        for particula in self.particulas:
            color = QColor(particula.red, particula.green, particula.blue)
            origin = QGraphicsEllipseItem(particula.origen_x, particula.origen_y, 5, 5)
            origin.setBrush(QBrush(color))
            origin.setPen(QPen(color))
            self.scene.addItem(origin)

        for particula_i, particula_j, distance in mst_edges:
            x1, y1 = particula_i.origen_x, particula_i.origen_y
            x2, y2 = particula_j.origen_x, particula_j.origen_y

            line = QGraphicsLineItem(x1 + 3, y1 + 3, x2 + 3, y2 + 3)
            line.setPen(QPen(QColor(0, 0, 255), 1)) 
            self.scene.addItem(line)
    @Slot()
    def drawPrimmParticles(self):
        self.scene = QGraphicsScene()
        self.graficador_ui.graphicsView.setScene(self.scene)

        # Run Prim's algorithm
        graph = Graph(self.particulas)
        mst_edges = graph.prims_algorithm()

        # Draw particles (nodes)
        for particula in self.particulas:
            color = QColor(particula.red, particula.green, particula.blue)
            origin = QGraphicsEllipseItem(particula.origen_x, particula.origen_y, 5, 5)
            origin.setBrush(QBrush(color))
            origin.setPen(QPen(color))
            self.scene.addItem(origin)

        # Draw the edges of the MST
        for u, v, weight in mst_edges:
            p1 = self.particulas[u]
            p2 = self.particulas[v]
            line = QGraphicsLineItem(p1.origen_x + 3, p1.origen_y + 3, p2.origen_x + 3, p2.origen_y + 3)
            line.setPen(QPen(QColor(0, 0, 255), 1))  #Azulito
            self.scene.addItem(line)
    @Slot()
    def drawParticulas(self):
        self.scene = QGraphicsScene()
        self.graficador_ui.graphicsView.setScene(self.scene)
        for particula in self.particulas:
            color = QColor(particula.red, particula.green, particula.blue)
            origin = QGraphicsEllipseItem(particula.origen_x, particula.origen_y, 5, 5)
            origin.setBrush(QBrush(color))
            origin.setPen(QPen(color))
            self.scene.addItem(origin)
            destination = QGraphicsEllipseItem(particula.destino_x, particula.destino_y, 5, 5)
            destination.setBrush(QBrush(color))
            destination.setPen(QPen(color))
            self.scene.addItem(destination)

            line = QGraphicsLineItem(particula.origen_x + 2.5, particula.origen_y + 2.5,
                                    particula.destino_x + 2.5, particula.destino_y + 2.5)
            line.setPen(QPen(color, 1))
            self.scene.addItem(line)
    @Slot()
    def drawParticulasButOnlyPoints(self):
        self.scene = QGraphicsScene()
        self.graficador_ui.graphicsView.setScene(self.scene)
        for particula in self.particulas:
            color = QColor(particula.red, particula.green, particula.blue)
            origin = QGraphicsEllipseItem(particula.origen_x, particula.origen_y, 5, 5)
            origin.setBrush(QBrush(color))
            origin.setPen(QPen(color))  
            self.scene.addItem(origin)
            destination = QGraphicsEllipseItem(particula.destino_x, particula.destino_y, 5, 5)
            destination.setBrush(QBrush(color))
            destination.setPen(QPen(color))  
            self.scene.addItem(destination)
    @Slot()
    def drawParticulasButOnlyNearestPoints(self):
        self.update_puntos()
        self.scene = QGraphicsScene() 
        self.graficador_ui.graphicsView.setScene(self.scene)
        nearest_pairs = self.puntos_mas_cercanos(self.puntos)
        
        for punto_i, cercano in nearest_pairs:
            x1, y1 = punto_i
            self.scene.addEllipse(x1, y1, 6, 6, QPen(), QBrush(QColor(0, 255, 0)))  
            
            x2, y2 = cercano
            self.scene.addEllipse(x2, y2, 6, 6, QPen(), QBrush(QColor(255, 0, 0)))  

            line = QGraphicsLineItem(x1 + 3, y1 + 3, x2 + 3, y2 + 3)  
            line.setPen(QPen(QColor(0, 0, 255), 1)) 
            self.scene.addItem(line)
    @Slot()
    def handle_header_click(self, index):
        column_to_option = {
            0: 1,  
            1: 2,  
            2: 3,  
            3: 4,  
            4: 5,  
            5: 6, 
            6: 7, 
            7: 8, 
            8: 9,  
        }
        option = column_to_option.get(index, 1) 
        self.tulpaRefresh(option)
        
    @Slot()
    def click_refrescar(self):
        self.ui.barraDeBusqueda.clear()  
        self.click_mostrar() 

    @Slot()
    def click_agregar_inicio(self):
        particula = self.crear_particula()
        if particula:
            self.particulas.insert(0, particula)  
            self.click_mostrar()  
            self.updateTablaConsole()

    @Slot()
    def click_agregar_final(self):
        particula = self.crear_particula()
        if particula:
            self.particulas.append(particula) 
            self.click_mostrar()  
            self.updateTablaConsole()

    @Slot()
    def click_guardar_sesion(self):  
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save JSON File", "registroDatos.json", "JSON Files (*.json);;All Files (*)", options=options)
        if file_name:
            try:
                Particula.guardar_en_json(self.particulas, file_name)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudieron guardar las partículas: {str(e)}")

    @Slot()
    def click_leer_archivo(self):  
        options = QFileDialog.Options()
        preselectoElArchivoXD, _ = QFileDialog.getOpenFileName(self, "Select JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
        if preselectoElArchivoXD:  
            with open(preselectoElArchivoXD, 'r') as f:
                particles_data = json.load(f)
                self.particulas.clear()
                for data in particles_data:
                    particula = Particula(
                        id=data.get("id", ""),
                        origen_x=data.get("origen_x", 0),
                        origen_y=data.get("origen_y", 0),
                        destino_x=data.get("destino_x", 0),
                        destino_y=data.get("destino_y", 0),
                        velocidad=data.get("velocidad", 0),
                        red=data.get("red", 0),
                        green=data.get("green", 0),
                        blue=data.get("blue", 0)
                    )
                    self.particulas.append(particula)
                self.click_mostrar()  
                self.updateTablaConsole()

    @Slot()
    def click_mostrar(self):
        self.ui.firstConsole.clear()
        self.ui.secondConsole.clear()
        for particula in self.particulas:
            message = f"{particula}\n"
            self.ui.firstConsole.insertPlainText(message)
            self.ui.secondConsole.insertPlainText(message)
        self.updateTablaConsole()  
        
    @Slot()
    def click_busqueda(self):
        search_id = self.ui.barraDeBusqueda.text()
        filtered_particulas = [p for p in self.particulas if str(p.id) == search_id]
        if not filtered_particulas:
            QMessageBox.warning(self, "Advertencia", f"No se encontró ninguna partícula con ID: {search_id}")
        self.updateTablaConsole(filtered_particulas)
    @Slot()
    def crear_particula(self):
        try:
            origen_x = self.ui.agregarOrigenX.value()
            origen_y = self.ui.agregarOrigenY.value()
            destino_x = self.ui.agregarDestinoX.value()
            destino_y = self.ui.agregarDestinoY.value()
            velocidad = float(self.ui.agregarVelocidad.text())  
            red = self.ui.agregarRed.value()
            green = self.ui.agregarGreen.value()
            blue = self.ui.agregarBlue.value()
            id = self.ui.agregarID.text()
            particula = Particula(
                id=id,
                origen_x=origen_x,
                origen_y=origen_y,
                destino_x=destino_x,
                destino_y=destino_y,
                velocidad=velocidad,
                red=red,
                green=green,
                blue=blue
            )
            return particula
        except ValueError:
            QMessageBox.warning(self, "Error", "DATOS NO VALIDOS")
            return None
    @Slot()
    def update_puntos(self):
        self.puntos.clear()
        for particula in self.particulas:
            self.puntos.append((particula.origen_x, particula.origen_y))
            self.puntos.append((particula.destino_x, particula.destino_y))

        print(f"Updated puntos: {self.puntos}")