### Importación de archivos
from biblioteca import biblioteca
from libro import libro
from usuario import usuario
from funciones_validaciones import validar_registro_libro, validar_registro_usuario
from prestamos import prestamo
from devoluciones import devolucion

### crear la biblioteca
biblioteca_general = biblioteca("BIBLIOTECA GENERAL")

# Objetos extras

# Usuarios
usuario1 = usuario("202600001", "Carlos Lopez", "carlos@gmail.com")
usuario2 = usuario("202600002", "Maria Garcia", "maria@gmail.com")

biblioteca_general.agregar_usuario(usuario1)
biblioteca_general.agregar_usuario(usuario2)


# Libros
libro1 = libro("001", "It", "Stephen King", "13/10/2020")
libro2 = libro("002", "1984", "George Orwell", "08/06/1949")
libro3 = libro("003", "El Principito", "Antoine de Saint Exupery", "06/04/1943")

biblioteca_general.agregar_libro(libro1)
biblioteca_general.agregar_libro(libro2)
biblioteca_general.agregar_libro(libro3)


### MENÚ
def menu():
    while True:
        print("""\n
ESTE ES EL MENÚ PRINCIPAL
-----ELIJA UNA OPCIÓN-----
opción 1: agregar libro a la biblioteca
opción 2: buscar libro
opción 3: eliminar libro
opción 4: mostrar libros
opción 5: registrar usuario
opción 6: buscar usuario
opción 7: eliminar usuario
opción 8: mostrar usuarios
opcion 9: prestar libro
opción 10: devoluciones
opción 11: salir del programa
\n""")
        opcion = int(input())

        match opcion:

            case 1:
                codigo, titulo, autor, fecha_lanzamiento = validar_registro_libro()
                nuevo_libro = libro(codigo, titulo, autor, fecha_lanzamiento)
                biblioteca_general.agregar_libro(nuevo_libro)

            case 2:
                codigo_libro = input("ingrese el código del libro: ")
                libro_encontrado = biblioteca_general.buscar_libro(codigo_libro)
                if libro_encontrado:
                    libro_encontrado.mostrar_informacion_libro()
                else:
                    print("no se encontró el libro")

            case 3:
                codigo_libro = input("ingrese el código del libro para eliminarlo: ")
                biblioteca_general.eliminar_libro(codigo_libro)

            case 4:
                biblioteca_general.mostrar_libros()

            case 5:
                carnet, nombre, correo = validar_registro_usuario()
                nuevo_usuario = usuario(carnet, nombre, correo)
                biblioteca_general.agregar_usuario(nuevo_usuario)

            case 6:
                carnet_usuario = input("ingrese el ID o carnet de usuario: ")
                usuario_encontrado = biblioteca_general.buscar_usuario(carnet_usuario)
                if usuario_encontrado:
                    usuario_encontrado.mostrar_informacion_usuario()
                else:
                    print("no se encontró al usuario")

            case 7:
                carnet_usuario = input("ingrese el ID o carnet de usuario para eliminarlo: ")
                biblioteca_general.eliminar_usuario(carnet_usuario)

            case 8:
                biblioteca_general.mostrar_usuarios()

            case 9:
                codigo_libro = input("ingrese el código del libro: ")
                libro_encontrado = biblioteca_general.buscar_libro(codigo_libro)

                carnet_usuario = input("ingrese el carnet o ID del usuario: ")
                usuario_encontrado = biblioteca_general.buscar_usuario(carnet_usuario)

                if libro_encontrado and usuario_encontrado:
                    nuevo_prestamo = prestamo(libro_encontrado, usuario_encontrado)

                    if biblioteca_general.agregar_generar_prestamo(nuevo_prestamo):
                        libro_encontrado.estado = "prestado"

            case 10:
                codigo_libro = input("ingrese el código del libro: ")
                libro_encontrado = biblioteca_general.buscar_libro(codigo_libro)

                carnet_usuario = input("ingrese el carnet del usuario: ")
                usuario_encontrado = biblioteca_general.buscar_usuario(carnet_usuario)

                if libro_encontrado and usuario_encontrado:
                    nueva_devolucion = devolucion(libro_encontrado, usuario_encontrado)
                    if biblioteca_general.agregar_generar_devolucion(nueva_devolucion):
                        libro_encontrado.estado = "disponible"

            case 11:
                print("saliendo del programa")
                break
            case _:
                print("opción inválida")

### correr el programa
menu()
