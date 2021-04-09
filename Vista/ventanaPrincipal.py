from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from Modelo.arregloProductos import *
from Modelo.arregloClientes import *
from Modelo.arregloDetalleVenta import *
from Modelo.arregloFactura import *
from Vista.ventanaClientes import *
from Vista.ventanaDetalleVentas import *
from Vista.ventanaFacturas import *
from Vista.ventanaProductos import *
from Vista.ventanaVentas import *

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaPrincipal,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/ventanaPrincipal.ui",self)
        
        self.btnProductos.clicked.connect(self.abrirVentanaProductos)
        self.btnClientes.clicked.connect(self.abrirVentanaClientes)
        self.btnVender.clicked.connect(self.abrirVentanaVentas)
        self.btnDetalleVentas.clicked.connect(self.abrirVentanaDetalleVentas)
        self.btnVentas.clicked.connect(self.abrirVentanaFacturas)
        self.btnSalir.clicked.connect(self.cerrar)
        
    def abrirVentanaProductos(self):
        vproductos = VentanaProductos(self)
        vproductos.show()
    
    def abrirVentanaClientes(self):
        vclientes = VentanaClientes(self)
        vclientes.show()

    def abrirVentanaVentas(self):
        vVentas = VentanaVentas(self)
        vVentas.show()
    
    def abrirVentanaDetalleVentas(self):
        vDetalleVentas = VentanaDetalleVentas(self)
        vDetalleVentas.show()
    
    def abrirVentanaFacturas(self):
        vFacturas = VentanaFacturas(self)
        vFacturas.show()

    def cerrar(self):
        self.close()