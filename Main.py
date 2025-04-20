from Model.Biblioteca import Biblioteca
from Model.Usuario import Usuario
from Model.Libro import Libro
from Model.Prestamo import Prestamo
from Model.Profesor import Profesor
from Model.Estudiante import Estudiante

biblioteca = Biblioteca([],[],[])

def crear_estudiante():
    estudiante = Estudiante.crear_estudiante()
    resultado = biblioteca.buscar_usuario(estudiante.get_cedula())
    if (resultado is None):
        biblioteca.agregar_usuario(estudiante)
        
    else:
        print ( "\nEl estudiante ya existe ")
    
    stop()
    
def mostrar_usuarios():
    biblioteca.mostrar_usuarios() 
    stop()
    
def buscar_usuario():
    cedula = input("\nIngrese el numero de cedula: ")
    biblioteca.buscar_usuario(cedula)
    stop()  
    
def crear_libro():
    libro = Libro.crear_libro()
    resultado = biblioteca.buscar_libro(libro.get_isbn())
    if (resultado is None):
        biblioteca.agregar_libro(libro)
        
    else:
        print ( "El libro con isbn ya existe ")
           
    stop()
    
    
def buscar_libro():
    isbn = input("\nIngrese el numero de isbn: ")
    biblioteca.buscar_libro(isbn)  
    stop()  
    
def mostrar_libros():
    biblioteca.mostrar_libros()
    stop()
    
def prestar_libro():
    cedula = input("\nIngrese numero de cedula ")
    usuario = biblioteca.buscar_usuario(cedula)
     
    if (usuario is None):
        stop()
        return
    
    if (biblioteca.total_prestados_por_usuario(cedula) >= usuario.max_libros()):
        print(f"\nExcediste la cantidad de libros prestados maximo {usuario.max_libros()}")
        stop()
        return
    
    isbn = input( "\ningrese isbn " )
    libro = biblioteca.buscar_libro(isbn)
    if (libro is None ):
        stop()
        return
    
    biblioteca.prestar_libro(usuario,libro) 
    stop()  
    
def mostrar_libros_prestados():
    biblioteca.mostrar_libros_prestados() 
    stop()
    
def devolucion_libro():
    isbn = input( "\ningrese el isbn " )
    libro = biblioteca.buscar_libro(isbn)
    
    if (libro is None):
        stop()
        return
    
    biblioteca.devolucion_libro(libro)
    stop()      
    
def crear_profesor():
    profesor = Profesor.crear_profesor()
    resultado = biblioteca.buscar_usuario(profesor.get_cedula())
    if (resultado is None):
        biblioteca.agregar_usuario(profesor) 
        
    else:
        print ( "\nEl profesor ya existe ")
    
    stop()   
    
def stop():
    input("\nPresione enter para continuar ")        
        
       

while True:
    print("\n_________________________________________")
    print("\nSistema Bibliocate prestamo de libros")
    print("Universidad de Manizalesate prestamo de libros")
    
    print("1. Crear estudiante")
    print("2. Crear profesor")
    print("3. Crear libro")
    print("4. Mostar libros")
    print("5. Mostar libros prestados")
    print("6. Mostar usuarios")
    print("7. Busca usuarios")
    print("8. Buscar libro")
    print("9. Prestar libro")
    print("10. Devolucion Libro")
    print("11. Salir\n")
    
    main_option = input("Seleccione una opcion: ")

    if main_option == "1":
        crear_estudiante()
    elif main_option == "2":
        crear_profesor()
    elif main_option == "3":
        crear_libro()
    elif main_option == "4":
        mostrar_libros()
    elif main_option == "5":
        mostrar_libros_prestados()
    elif main_option == "6":
        mostrar_usuarios()
    elif main_option == "7":
        buscar_usuario()
    elif main_option == "8":
        buscar_libro()
    elif main_option == "9":
        prestar_libro()
    elif main_option == "10":
        devolucion_libro()
    elif main_option == "11": 
        break
    else:
        print("Opcion invalida")

