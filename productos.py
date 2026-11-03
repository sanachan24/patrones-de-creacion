
from abc import ABC, abstractmethod


# Productos abstractos

class InformeFactura(ABC):

    @abstractmethod
    def procesar(self):
        pass


class InformeCompra(ABC):

    @abstractmethod
    def procesar(self):
        pass


# Productos concretos: categoría ENTRADA

class FacturaEntrada(InformeFactura):

    def procesar(self):
        print("Procesando informe de ENTRADA de tipo FACTURA")


class CompraEntrada(InformeCompra):

    def procesar(self):
        print("Procesando informe de ENTRADA de tipo COMPRA")


# Productos concretos: categoría SALIDA

class FacturaSalida(InformeFactura):

    def procesar(self):
        print("Procesando informe de SALIDA de tipo FACTURA")


class CompraSalida(InformeCompra):

    def procesar(self):
        print("Procesando informe de SALIDA de tipo COMPRA")

# Productos concretos: categoría MIXTA
class FacturaMixta(InformeFactura):
    def procesar(self):
        print("Procesando informe de MIXTA de tipo FACTURA")


class CompraMixta(InformeCompra):
    def procesar(self):
        print("Procesando informe de MIXTA de tipo COMPRA")
        
# Producto concreto: categoría ENTRADA, tipo PEDIDO
class PedidoEntrada:
    def procesar(self):
        print("Procesando informe de ENTRADA de tipo PEDIDO")