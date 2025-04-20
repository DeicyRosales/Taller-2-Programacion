from Model.InterfaceBibliteca import InterfaceBibliteca
from Model.Usuario import Usuario
from Model.Prestamo import Prestamo
from Model.Libro import Libro
from Model.Estudiante import Estudiante
from Model.Profesor import Profesor

class Biblioteca(InterfaceBibliteca):
    def __init__(self, lista_usuario: list , lista_libros: list, lista_libros_prestados:list):
        self.__lista_usuarios = lista_usuario
        self.__lista_libros = lista_libros
        self.__lista_libros_prestados = lista_libros_prestados
        self.crear_inventario_inicial_libros()
        self.crear_usuarios_iniciales()
         
    def mostrar_libros(self):
        if (len(self.__lista_libros) == 0 ):
            print ("\nNo hay libros " )
            return
        
        for item in self.__lista_libros:
            item.mostrar()
    
    def mostrar_libros_prestados(self):
        if (len(self.__lista_libros_prestados) > 0 ):   
            for prestamo in self.__lista_libros_prestados:
                prestamo.libro.mostrar()
                prestamo.usuario.mostrar()
        else:
            print ("\nNo hay Libros Prestados " )
    
    def total_prestados_por_usuario(self, cedula):
        contador = 0
        if (len(self.__lista_libros_prestados) > 0 ):   
            for prestamo in self.__lista_libros_prestados:
                if (prestamo.usuario.get_cedula() == cedula):
                    contador += 1
        return contador            

    def mostrar_usuarios(self):
        if (len(self.__lista_usuarios) == 0 ):
            print ("\nNo hay ususarios creados " )
            return
         
        for item in self.__lista_usuarios:
            item.mostrar()
            

    def buscar_usuario(self, cedula) -> Usuario:
        if (len(self.__lista_usuarios) == 0 ):
            print ("\n Aun no has creado usuarios en la biblioteca " )
            return None
        
        for item in self.__lista_usuarios:
            if (item.get_cedula() == cedula):
                item.mostrar()
                return item
            
        print (f"\n El usuario con cedula {cedula} no existe " )    
        return None
        
        
    def agregar_usuario(self, usuario):
        self.__lista_usuarios.append(usuario)
        print(f"\nUsuario agregado a la lista.")
        usuario.mostrar()
       
    def buscar_libro(self, isbn) -> Libro:
        if (len(self.__lista_libros) == 0 ):
            print ("\n No existen libros en la biblioteca " )
            return None
        
        for item in self.__lista_libros:
            if (item.get_isbn() == isbn):
                item.mostrar()
                return item
            
        print (f"\n El libro con  isbn {isbn} no existe " )    
        return None
        
    def agregar_libro(self, libro):
        
        self.__lista_libros.append(libro)
        print(f"\nLibro agregado a la lista.")
        libro.mostrar()

    def buscar_libro_prestado(self, libro) -> Prestamo: 
        if (len(self.__lista_libros_prestados) == 0 ):
            return None
        
        for item in self.__lista_libros_prestados:
            if (item.libro.get_isbn() == libro.get_isbn()):
                return item
                     
        return None
    
    
    def prestar_libro(self, usuario, libro):
        
        prestamo = self.buscar_libro_prestado(libro)
        
        if (prestamo is None ):
            prestamo = Prestamo(usuario, libro)
            self.__lista_libros_prestados.append(prestamo)   
            print(f"\nEl libro fue prestado' ")
            usuario.mostrar()
            libro.mostrar()
        else:
            print(f"\nEl libro '{libro.get_titulo()}' ya esta prestado al usuario' ")
            prestamo.usuario.mostrar()
    

    def devolucion_libro(self, libro):
       
       prestamo = self.buscar_libro_prestado(libro)
       if (prestamo == "" ):
           print("\nEl libro no esta prestado")
       else:
           self.__lista_libros_prestados.remove(prestamo)
           print("\nDevolucion correcta de libro")
           libro.mostrar()
           
           
    def crear_inventario_inicial_libros(self):
      
        libro = Libro("01", "Cien años de soledad", "Gabriel García Márquez", "1967")
        self.agregar_libro(libro)

        libro = Libro("02", "1984", "George Orwell", "1949")
        self.agregar_libro(libro)

        libro = Libro("03", "Don Quijote de la Mancha", "Miguel de Cervantes", "1605")
        self.agregar_libro(libro)

        libro = Libro("04", "Crónica de una muerte anunciada", "Gabriel García Márquez", "1981")
        self.agregar_libro(libro)

        libro = Libro("05", "Fahrenheit 451", "Ray Bradbury", "1953")
        self.agregar_libro(libro)

        libro = Libro("06", "La sombra del viento", "Carlos Ruiz Zafón", "2001")
        self.agregar_libro(libro)

        libro = Libro("07", "El código Da Vinci", "Dan Brown", "2003")
        self.agregar_libro(libro)

        libro = Libro("08", "Orgullo y prejuicio", "Jane Austen", "1813")
        self.agregar_libro(libro)

        libro = Libro("09", "El alquimista", "Paulo Coelho", "1988")
        self.agregar_libro(libro)

        libro = Libro("10", "Los juegos del hambre", "Suzanne Collins", "2008")
        self.agregar_libro(libro)

        libro = Libro("11", "Harry Potter y la piedra filosofal", "J.K. Rowling", "1997")
        self.agregar_libro(libro)

        libro = Libro("12", "La ladrona de libros", "Markus Zusak", "2005")
    
        libro = Libro("13", "El nombre del viento", "Patrick Rothfuss", "2007")
        self.agregar_libro(libro)

        libro = Libro("14", "It", "Stephen King", "1986")
        self.agregar_libro(libro)

        libro = Libro("15", "El señor de los anillos", "J.R.R. Tolkien", "1954")
        self.agregar_libro(libro)

        libro = Libro("16", "Matar a un ruiseñor", "Harper Lee", "1960")
        self.agregar_libro(libro)

        libro = Libro("17", "Las ventajas de ser invisible", "Stephen Chbosky", "1999")
        self.agregar_libro(libro)

        libro = Libro("18", "La naranja mecánica", "Anthony Burgess", "1962")
        self.agregar_libro(libro)

        libro = Libro("19", "Rebelión en la granja", "George Orwell", "1945")
        self.agregar_libro(libro)

        libro = Libro("20", "El psicoanalista", "John Katzenbach", "2002")
        self.agregar_libro(libro)
        
    def crear_usuarios_iniciales(self):
        usuario1 = Estudiante("123", "Carlos Perez", "carlos@gmail.com", "Sistemas", "Tercero")
        usuario2 = Estudiante("124", "Teresa Lopez", "tere@gmail.com", "Biologia", "Tercero")
        usuario3 = Profesor("125", "Diego Delgado", "diego@hotmail.com", "artes")
        self.agregar_usuario(usuario1)
        self.agregar_usuario(usuario2)
        self.agregar_usuario(usuario3)
