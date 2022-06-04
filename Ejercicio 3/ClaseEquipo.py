
class Equipo:
    __nombre = ""
    __ciudad = ""

    def __init__(self, nom, ciu):
        self.__nombre = nom
        self.__ciudad = ciu

    def getnom(self):
        return self.__nombre

    def getciudad(self):
        return self.__ciudad
    
    def __str__(self) -> str:
        return("Nombre: {}  Ciudad: {}".format(self.__nombre,self.__ciudad))
