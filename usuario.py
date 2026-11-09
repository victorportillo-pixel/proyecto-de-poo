class usuario:
    def __init__(self, carnet, nombre, correo):
        self.__carnet = carnet
        self.__nombre = nombre
        self.__correo = correo

    @property
    def carnet(self):
        return self.__carnet

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    def mostrar_informacion_usuario(self):
        print(f"""
carnet: {self.carnet}
nombre: {self.nombre}
correo: {self.correo}
""")