from Manejador_Flores import ManejadorFlores
from Manejador_Ramos import ManejadorRamos
class Menu:
    __op=-1

    def __init__(self) -> None:
        mf=ManejadorFlores()
        mr=ManejadorRamos()
        while(self.__op!=0):
            print("")
            print("Seleccione una opcion")
            self.__op=int(input("1 Registrar un ramo vendido.\n2 Mostrar el nombre de las 5 flores  más pedidas en un ramo.\n"
            "3 Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos.\n0 Finalizar ejecucion.\n"))
            print("")
            self.opciones(mf,mr)

    def opciones(self,mf,mr):
        if(self.__op==1):
            self.opcion1(mf,mr)
        elif(self.__op==2):
            self.opcion2(mf)
        elif(self.__op==3):
            self.opcion3(mr)
        elif(self.__op==0):
            print("finalizando ejecucion")
        else:print("Opcion incorrecta")    
    
    def opcion1(self,mf,mr):
        print("Opcion 1 comenzando")
        mr.crearramo(mf)
    def opcion2(self,mf):
        print("Opcion 2 comenzando")
        mf.muestramasvend()
    def opcion3(self,mr):
        print("Opcion 3 comenzando")
        tam=str(input("Ingrese el tamaño a mostrar: "))
        mr.mostrarportamanio(tam)
    
    
