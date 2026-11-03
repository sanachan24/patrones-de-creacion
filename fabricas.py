
from abc import ABC, abstractmethod

from productos import (
    FacturaEntrada,
    CompraEntrada,
    FacturaSalida,
    CompraSalida,
    FacturaMixta,
    CompraMixta,
    PedidoEntrada
)

# Fabrica abstracta

class FabricaInformes(ABC):

    @abstractmethod
    def crear_factura(self):
        pass

    @abstractmethod
    def crear_compra(self):
        pass


# Fabrica concreta: ENTRADA

class FabricaEntrada(FabricaInformes):

    def crear_factura(self):
        return FacturaEntrada()

    def crear_compra(self):
        return CompraEntrada()
    
    def crear_pedido(self):
        return PedidoEntrada()


# Fabrica concreta: SALIDA

class FabricaSalida(FabricaInformes):

    def crear_factura(self):
        return FacturaSalida()

    def crear_compra(self):
        return CompraSalida()

# Fábrica concreta: MIXTA
class FabricaMixta(FabricaInformes):
    def crear_factura(self):
        return FacturaMixta()

    def crear_compra(self):
        return CompraMixta()