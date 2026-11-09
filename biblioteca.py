class biblioteca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = []
        self.__usuarios = []
        self.__prestamos = []
        self.__devoluciones = []
### validaciones de libros
    def tiene_libro(self, codigo_libro):
        for i in self.__libros:
            if i.codigo == codigo_libro:
                return True
        return None 

    def agregar_libro(self, libro):
        if self.tiene_libro(libro.codigo):
            print(f"el libro {libro.titulo} con código: {libro.codigo} ya esta en la biblioteca")
            return
        
        self.__libros.append(libro)
        print(f"el libro {libro.titulo} con código: {libro.codigo} se agregó la biblioteca")

    def buscar_libro(self, codigo_libro):
        for i in self.__libros:
            if i.codigo == codigo_libro:
                return i
        return None

    def eliminar_libro(self, codigo_libro):
        libro = self.buscar_libro(codigo_libro)
        if libro:
            self.__libros.remove(libro)
            print(f"el libro {libro.titulo} ha sido eliminado de la biblioteca")
        else:
            print(f"el libro no está en la biblioteca")
        
    def mostrar_libros(self):
        print(f"""-----BIBLIOTECA-----
{self.__nombre}
""")
        for i in self.__libros:
            print("---------------------------------------------")
            print(f"código: {i.codigo}")
            print(f"título: {i.titulo}")
            print(f"autor: {i.autor}")
            print(f"fecha de publicación: {i.fecha_lanzamiento}")
            print(f"estado: {i.estado}")
            print("---------------------------------------------")

### validaciones de usuarios
    def tiene_usuario(self, carnet_usuario):
        for i in self.__usuarios:
            if i.carnet == carnet_usuario:
                return True
        return None

    def agregar_usuario(self, usuario):
        if self.tiene_usuario(usuario.carnet):
            print(f"el usuario: {usuario.nombre} con carnet: {usuario.carnet} ya esta en el sistema")
            return

        self.__usuarios.append(usuario)
        print(f"el usuario: {usuario.nombre} con carnet: {usuario.carnet} se agregó al sistema")

    def buscar_usuario(self, carnet_usuario):
        for i in self.__usuarios:
            if i.carnet == carnet_usuario:
                return i
        return None

    def eliminar_usuario(self, carnet_usuario):
        usuario = self.buscar_usuario(carnet_usuario)
        if usuario:
            self.__usuarios.remove(usuario)
            print(f"el usuario: {usuario.nombre} con carnet: {usuario.carnet} fue eliminado del sistema")
        else:
            print(f"el usuario no existe en el sistema")

    def mostrar_usuarios(self):
        print(f"""-----BIBLIOTECA-----
{self.__nombre}
""")
        for i in self.__usuarios:
            print("---------------------------------------------")
            print(f"carnet: {i.carnet}")
            print(f"nombre: {i.nombre}")
            print(f"correo: {i.correo}")
            print("---------------------------------------------")

### agregar prestamos y validarlos
    def agregar_generar_prestamo(self, prestamo):
        if prestamo.libro not in self.__libros:
            print("no se encontró el libro")
            return False

        if prestamo.usuario not in self.__usuarios:
            print("no se encontró al usuario")
            return False

        self.__prestamos.append(prestamo)
        print("se hizo un prestamo exitosamente")
        return True

### agregar devoluciones y validarlas
    def agregar_generar_devolucion(self, devolucion):
        if devolucion.libro not in self.__libros:
            print("no se encontró el libro")
            return False

        if devolucion.usuario not in self.__usuarios:
            print("no se encontró al usuario")
            return False

        self.__devoluciones.append(devolucion)
        print("se devolvió el libro exitosamente")
        return True
