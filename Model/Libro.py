class Libro:
    def __init__(self, isbn, titulo, autor, año_publicacion):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__año_publicacion = año_publicacion

    def get_isbn(self):
        return self.__isbn

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_año_publicacion(self):
        return self.__año_publicacion

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_año_publicacion(self, año_publicacion):
        self.__año_publicacion = año_publicacion


    def mostrar(self):
        print(f"ISBN: {self.__isbn}, Título: {self.__titulo}, Autor: {self.__autor}, Año: {self.__año_publicacion}")
        
    @classmethod
    def crear_libro(cls):
        isbn = input("Ingrese el isbn del libro: ")
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        Año = input("Ingrese el Año del libro: ")

        
        return cls(isbn, titulo, autor, Año)     
