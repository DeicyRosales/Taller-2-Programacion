class Usuario:
    def __init__(self, cedula, nombre, correo_electronico):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__correo_electronico = correo_electronico

    def get_cedula(self):
        return self.__cedula

    def get_nombre(self):
        return self.__nombre

    def get_correo_electronico(self):
        return self.__correo_electronico

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_correo_electronico(self, correo_electronico):
        if "@" in correo_electronico:
            self.__correo_electronico = correo_electronico
        else: 
            raise ValueError("Correo invalido")
        
    def max_libros(self) -> int:
        return 2 
    
    def datos(self) -> str:
        return (f"{self.__cedula}, {self.__nombre}, {self.__correo_electronico}")

    @classmethod
    def crear_usuario(cls):
        cedula = input("Ingrese el numero de cedula: ")
        nombre = input("Ingrese el nombre: ")
        usuario =  cls(cedula, nombre, "")
        while True:
            try:
                correo = input("Ingrese el correo: ")
                usuario.set_correo_electronico(correo)
                break
            except ValueError as e:
                print(e)
        
        
        return usuario