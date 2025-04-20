from Model.Usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, cedula: str, nombre: str, correo: str, carrera: str, semestre: int ):
        super().__init__(cedula, nombre, correo)
        self.__carrera = carrera
        self.__semestre = semestre 
    
    def get_carrera(self) -> str:
        return self.__carrera
    
    def set_carrera(self, carrera: str):
        self.__carrera = carrera
        
    def get_semestre(self) -> int:
        return self.__semestre
    
    def set_semestre(self, semestre: int):
        self.__semestre = semestre      
    
    def mostrar(self):
        print(f"Estudiante: {self.datos()}, {self.__carrera}, {self.__semestre} ") 
            
    @classmethod
    def crear_estudiante(cls):
        usuario = Usuario.crear_usuario()
        carrera = input("Ingrese la carrera del estudiante: ")
        semestre = input("Ingrese el semestre que cursa el estudiante: ")
        
        return cls(usuario.get_cedula(), usuario.get_nombre(), usuario.get_correo_electronico(), carrera, semestre)         
         