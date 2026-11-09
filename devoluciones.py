class devolucion:
    def __init__(self, libro, usuario):
        self.__libro = libro
        self.__usuario = usuario

    @property
    def libro(self):
        return self.__libro

    @property
    def usuario(self):
        return self.__usuario

    