from ClaseRamo import Ramo
from ClaseFlores import Flor
import csv
class ManejadorRamos:
    __listaR=[]

    def __init__(self) -> None:
        __listaR=[]
    
    def crearramo(self,mf):
        cant=-1
        while(cant!=0):

            cant=int(input("Ingrese la cantidad de flores que quiere agregar o 0 para finalizar: "))
            
            if cant!=0:
                r=Ramo(cant)
                for i in range(cant):
                    mf.menuflores()
                    fn=int(input("Ingrese la flor que quiere ingresar: "))
                    while fn < 0 or fn >len(mf.getarray()):
                        fn=input("OPCION INCORRECTA -> Elija entre 1 y {}\nIngrese el numero correcto: ".format(len(mf.getarray())))
                    print("AGREGANDO")
                    
                    mf.getarray()[fn-1].cantventas()
                    
                    r.addFlor(mf.getarray()[fn-1])
                self.__listaR.append(r)
                #r.muestrafloresenramo()
    
    def mostrarportamanio(self,t):
        band=False
        for ram in self.__listaR:
            if ram.gettam()==t:
                band=True
                ram.muestrafloresenramo()
        if not band:
            print("No hay ramos de ese tamaño")



    


    