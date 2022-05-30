from Manejador_Flores import ManejadorFlores
from Manejador_Ramos import ManejadorRamos
class Menu:
    __op=-1

    def __init__(self) -> None:
        while(self.__op!=0):
            print("")
            print("Seleccione una opcion")
            self.__op=int(input("1 Registrar un ramo vendido.\n2 Mostrar el nombre de las 5 flores  más pedidas en un ramo.\n"
            "3 Mostrar flores vendidas segun tipo de ramo.\n0 Finalizar ejecucion.\n"))
            print("")
            self.opciones()

    def opciones(self):
        mf=ManejadorFlores()
        mr=ManejadorRamos()
        
        if(self.__op==1):
            self.opcion1(mf,mr)
        elif(self.__op==2):
            self.opcion2(mf)
        elif(self.__op==3):
            self.opcion3()
        elif(self.__op==0):
            print("finalizando ejecucion")
        else:print("Opcion incorrecta")    
    
    def opcion1(self,mf,mr):
        print("Opcion 1 comenzando")
        mr.crearramo(mf)
    def opcion2(self,mf):
        print("Opcion 2 comenzando")
        mf.muestramasvend()
    def opcion3(self):
        print("Opcion 3 comenzando")
    
    
