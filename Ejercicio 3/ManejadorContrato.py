from ClaseContrato import Contrato
from ManejadorEquipo import ManejadorEquipo
from ManejadorJugador import ManejadorJugador
import datetime
import numpy as np




class ManejadorContrato:
    __controljugador: ManejadorJugador
    __controlequipo: ManejadorEquipo
    __arrayc: np.ndarray


    def __init__(self, manjug, maneq):
        self.__controljugador = manjug
        self.__controlequipo = maneq
        self.__arrayc = np.empty(0, Contrato)


    def crearcontrato(self, jugador, equipo, fechaini, fechafinal, pagomensual):

        if jugador!= None and equipo != None:
            c = Contrato(fechaini, fechafinal, pagomensual, jugador, equipo)
            self.__arrayc = np.append(self.__arrayc, c)
        else:
            print("Nombre de jugador o equipo invalidos")


    def prueba(self):
        print(len(self.__arrayc))

    def mostrarequipo(self, dni):
        i=0
        band=False
        while not band and i< len(self.__arrayc):
            if self.__arrayc[i].getdnij()==dni:
                band=True
                print("El equipo del Jugador de dni:{} es el:{} y tiene contrato hasta{}".format(dni,self.__arrayc[i].getnomequip(),self.__arrayc[i].getfin()))
            i+=1
        if not band:
            print("Jugador no enconrtrado")

    def mostrarcontratos(self, nom):
        bandera = False
        i=0
        for i in range(len(self.__arrecontrato)):
            fechaactual = datetime.date.today()
            vence6meses = fechaactual + datetime.timedelta(days=365/2)
            fechafin = self.__arrecontrato[i].getfechafin()
            eq = self.__arrecontrato[i].getequipo()
            if eq.getnombre() == nom:
                if fechafin >= fechaactual and fechafin <= vence6meses:
                    jugador = self.__arrecontrato[i].getjugador()
                    print("Jugador: {}, su contrato vence en {} mes/meses".format(jugador, fechafin.month - fechaactual.month))
                    bandera = True
        if not bandera:
            print("El equipo, {} no posee contratos que tiene una fecha de vencimiento dentro de los proximos 6 meses".format(eq.getnombre()))



    def obtenerimporte(self, nom):
        total: float = 0
        for elem in self.__arrecontrato:
            if elem.getnomequipo() == nom:
                total+=elem.getpago()

        print("Para el equipo: {}, el importe total es: {}".format(nom, total))


    def guardarcontrato(self):

        with open("contratoguardar.txt", "w") as file:
            file.write("PagoMensual;FechaInicio;FechaFin;DNIjugador;NombreEquipo\n")

            for contrato in self.__arrecontrato:
                file.write(
                    str(contrato.getpago()) + ";" +
                    str(contrato.getfechaini()) + ";" +
                    str(contrato.getfechafin()) +  ";" +
                    contrato.getdnijugador() + ";" +
                    contrato.getnomequipo() + ";" + "\n"
                )
