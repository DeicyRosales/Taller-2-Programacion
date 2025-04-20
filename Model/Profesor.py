from Model.Usuario import Usuario

class Profesor(Usuario):
    def __init__(self, cedula: str, nombre: str, correo: str, materia: str ):
        super().__init__(cedula, nombre, correo)
        self.__materia = materia  
    

    def get_materia(self) -> str:
        return self.__materia
    
    def set_materia(self, materia: str):
        self.__materia = materia
    
    def mostrar(self):
        print(f"Profesor  : {self.datos()}, {self.__materia}. ") 
         
    def max_libros(self):
        return 3 
         
    @classmethod
    def crear_profesor(cls):
        usuario = Usuario.crear_usuario()
        materia = input("Ingrese la materia que da el profesor ")
        return cls(usuario.get_cedula(), usuario.get_nombre(), usuario.get_correo_electronico(), materia)  

    