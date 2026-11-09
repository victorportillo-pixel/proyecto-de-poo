class libro:
    def __init__(self, codigo, titulo, autor, fecha_lanzamiento):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__fecha_lanzamiento = fecha_lanzamiento
        self.__estado = "disponible"

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def fecha_lanzamiento(self):
        return self.__fecha_lanzamiento

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def mostrar_informacion_libro(self):
        print(f"""
código: {self.codigo}
título: {self.titulo}
autor: {self.autor}
estado: {self.estado}
fecha de publicación: {self.fecha_lanzamiento}
""")