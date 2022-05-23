from ClaseFlores import Flor
import numpy as np
from numpy import ndarray
from Menu import Menu
import csv

class ManejadorFlores:
    __array=np.array(Flor,0)


    def __init__(self) -> None:
        archivo=csv.open("flores.csv")
        reader=csv.reader(archivo,delimiter=";")

        for line in reader:
            f=Flor(line[0],line[1],line[2],line[3],line[4])
            self.__array=np.append(f)
        archivo.close()
    
    def crearramo(self):
        while(fn!="0"):
            m=Menu.menuflores()
            fn=str(input("Ingrese la flor que quiere ingresar o 0 para finalizar"))
            cant=int(input("Ingrese la cantridad de flores que quiere agregar"))

            for elem in self.__array:
                if(fn==elem.getn()):
                    print("AGREGANDO")