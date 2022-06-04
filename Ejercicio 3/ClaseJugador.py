import datetime

class Jugador:
    __nombre = ""
    __DNI = ""
    __ciudNatal = ""
    __paisOrg = ""
    __fechaN=""

    def __init__(self, nom, dni, ciud, pais, fecha):
        self.__nombre = nom
        self.__DNI = dni
        self.__ciudNatal = ciud
        self.__paisOrg = pais
        self.__fechaN = fecha


    def getdni(self):
        return self.__DNI

    def getnom(self):
        return self.__nombre

    def setdate(self, fecha):
        f = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
        return f

    def __str__(self) -> str:
        return("Nombre: {} Dni: {} Ciudad Natal: {} Pais: {} FechaNa:{}".format(self.__nombre,self.__DNI,self.__ciudNatal,self.__paisOrg,self.__fechaN))
        '''
        Equipo a
        Nombre 3
        22/10/2025
        22/11/2026
        50086
        '''