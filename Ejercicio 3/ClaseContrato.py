import datetime

class Contrato:
    __fechainicio=""
    __fechadefin=""
    __pagomensual :float
    __jugador = None
    __equipo = None


    def __init__(self, fechai, fechaf, pagomen, jugador, equipo):
        self.__fechainicio = fechai
        self.__fechadefin = fechaf
        self.__pagomensual = float(pagomen)
        self.__jugador = jugador
        self.__equipo = equipo
    
    def getdnij(self):
        return(self.__jugador.getdni())
    
    def getnomequip(self):
        return(self.__equipo.getnom())

    def getfechaini(self):
        return self.__fechainicio

    def getfin(self):
        return self.__fechadefin

    def getdnijugador(self):
        return self.__jugador.getdni()

    def getequi(self):
        return self.__equipo.getnom()

    def getpago(self):
        return self.__pagomensual

    def getequipo(self):
        return self.__equipo

    def getjugador(self):
        return self.__jugador
