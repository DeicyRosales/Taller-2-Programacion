from abc import ABC, abstractmethod

class InterfaceBibliteca(ABC):
    
    @abstractmethod
    def prestar_libro(self):
        pass
    
    @abstractmethod
    def buscar_libro_prestado(self):
        pass
    
    @abstractmethod
    def devolucion_libro(self):
        pass
    
    
    