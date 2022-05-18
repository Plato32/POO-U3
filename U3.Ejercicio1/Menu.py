from Carrera import Carrera
from Facultad import Facultad
from ManejadorFacultad  import ManejadorFacultades

class Menu:
    __op:int

    def __init__(self) -> None:
        self.__op=-1
    
    def opciones(self):
        M=ManejadorFacultades()
        while(self.__op!=0):
            print("")
            print("--------------------------------------------------------------------------------")
            self.__op=int(input("    Ingrese 1 para mostrar carreras por codigo de facutlad.\n    Ingrese 2 mostrar datos de una carrera por nombre.\n    Ingrese 0 para finalizar la ejecucion\n\n"))
            print("--------------------------------------------------------------------------------")
            print("")
            if(self.__op==1):
                self.opcion1(M)
            elif(self.__op==2):
                self.opcion2(M)
            elif(self.__op==0):
                print("Opcion de salida seleccionada")
            else:print("Opcion incorrecta seleccionada")
        print("")     
        print("--------FINALIZANDO EJECUCION--------")
    def opcion1(self,M):
        cod=input("Opcion 1 seleccionada\nIngrese el codigo de una facultad: ")
        M.mostrarcarrerascodigo(cod)

    def opcion2(self,M):
        nom=input("Opcion 2 seleccionada\nIngrese el nombre de una facultad: ")
        M.buscacarrera(nom)



    



'''D. A través de un menú de opciones implementar las siguientes funcionalidades:
1. Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.
2.  Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.
'''