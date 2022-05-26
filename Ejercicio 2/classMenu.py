from Manejador_Flores import ManejadorFlores
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
        mf=ManejadorFlores
        if(self.__op==1):
            self.opcion1(mf)
        elif(self.__op==2):
            self.opcion2()
        elif(self.__op==3):
            self.opcion3()
        elif(self.__op==0):
            print("finalizando ejecucion")
        else:print("Opcion incorrecta")    
    
    def opcion1(self,mf):
        print("Opcion 1 comenzando")
        mf.crearramo()
    def opcion2(self):
        print("Opcion 2 comenzando")
    def opcion3(self):
        print("Opcion 3 comenzando")
    
    
