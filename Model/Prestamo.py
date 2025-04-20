from Model.Usuario import  Usuario
from Model.Libro import  Libro

class Prestamo:
    def __init__(self, usuario: Usuario, libro: Libro):
        self.usuario = usuario
        self.libro = libro

