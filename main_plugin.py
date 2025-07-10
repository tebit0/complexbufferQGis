from qgis.PyQt.QtWidgets import QLineEdit, QPushButton
from qgis.PyQt.QtWidgets import QAction, QDialog, QVBoxLayout, QLabel

class BufferPlugin:
    def __init__(self, iface):
        self.iface = iface
        
    def initGui(self):
        self.action = QAction("Mi Buffer Tool", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        
    def run(self):
        dlg = QDialog()
        layout = QVBoxLayout()
    
        self.input_distancia = QLineEdit("100")
        layout.addWidget(QLabel("Distancia del buffer:"))
        layout.addWidget(self.input_distancia)
    
        btn_ejecutar = QPushButton("Crear Buffer")
        btn_ejecutar.clicked.connect(self.crear_buffer)
        layout.addWidget(btn_ejecutar)
    
        dlg.setLayout(layout)
        dlg.exec_()
        
    def crear_buffer(self):
        distancia = float(self.input_distancia.text())
        print(f"Creando buffer de {distancia} metros")
        
    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action
