from ManejadorEquipo import ManejadorEquipo
from ManejadorJugador import ManejadorJugador
from ManejadorContrato import ManejadorContrato


class Menu:
    __op: int
    __controlE: ManejadorEquipo
    __controlJ: ManejadorJugador
    __controlC: ManejadorContrato

    def __init__(self,me,mj,mc):
        self.__op=0
        self.__controlE = me
        self.__controlJ = mj
        self.__controlC = mc

    def mostrar(self):
        centinela=None
        while(centinela!=0):
            self.__op=int(input("""
            **Menu**        
Opcion ->[0] : [Finalizar]
Opcion ->[1] : Consultar jugadores Contratados: Ingresar el DNI de un jugador, si está contratado, mostrar el nombre del Equipo en el que fue contratado, y la fecha de finalización de contrato.
Opcion ->[2] : Consultar Contratos: Ingresar el identificador de un Equipo y listar los datos de los Jugadores cuyo contrato vence en 6 meses.
Opcion ->[3] : Obtener importe de contratos: Para un nombre de equipo leído desde teclado, determinar el importe total de los contratos que posee con los jugadores del equipo.
Opcion ->[4] : Guardar Contratos: Generar un nuevo archivo que contenga los siguientes datos de los contratos: DNI del jugador, Nombre del equipo, fecha de inicio, fecha de fin, y el pago mensual.


Ingrese Opcion-> """))

            if(self.__op==1):
               self.opcion1()

            elif(self.__op==2):
                self.opcion2()

            elif(self.__op==3):
                self.opcion3()

            elif(self.__op==4):
                self.opcion4()

            elif(self.__op==0):
                centinela=0
            else:
                print("Error")

    def opcion1(self):
        
        dni = input("Ingrese DNI: ")
        self.__controlC.mostrarequipo(dni)

    def opcion2(self):
       
        nom = input("Ingrese el nombre de un equipo: ")


    def opcion3(self):
       
        nom = input("Ingrese un nombre de equipo: ")
        self.__controlC.obtenerimporte(nom)

    def opcion4(self):
        
        self.__controlC.guardarcontrato()

'''
DNI 1
Equipo a
14/4/2022
14/4/2025
4500
'''
