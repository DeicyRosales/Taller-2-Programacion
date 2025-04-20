### Sistemas gestion de prestamo de libros para una biblioteca

El sistema permite crear usuarios tanto profesores como estudiantes, agregar libros, prestar libros y devolución de libros, mostrar usuarios y libros .
Un estudiante puede tener maximo 2 libros prestados miestras que un profesor puede pedir hasta 3 libros.
La clase estudiante y profesor heredan del la clase ususario.

Ademas se incluye las siguientes validaciones: 

- Un libro no se puede prestar si ya está asignado a otro usuario
- Para poder prestar un libro se valida que exista el usuario y el libro
- Validar email al crear usuario
- Validar por cedula que el profesor o estudiante no exista cuando se crea usuarios 
- No permite crear libros repetidos con el mismo isbn
- Validar deacuerdo al usuario que no sobrepase el máximo de libros permitidos

  Se incluye algunos usuarios y libros iniciales en al iniciar el sistema.
  
### VIDEO PRUEBA SISTEMA

https://github.com/user-attachments/assets/e86b01ae-d9a0-4fe8-848e-6c2d6df5d142

