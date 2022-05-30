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
                    '''print(florcita)'''
                    r.addFlor(mf.getarray()[fn-1])
                self.__listaR.append(r)
                r.muestrafloresenramo()

    
    

    '''def __init__(self) -> None:
            archivo=csv.open("flores.csv")
            reader=csv.reader(archivo,delimiter=";")

            for line in reader:
                f=Flor(line[0],line[1],line[2],line[3],line[4])
                self.__array=np.append(f)
            archivo.close()'''

    