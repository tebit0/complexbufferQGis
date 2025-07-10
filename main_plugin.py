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
        layout.addWidget(QLabel("¡Funciona! Mi primer plugin"))
        dlg.setLayout(layout)
        dlg.exec_()
        
    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action
