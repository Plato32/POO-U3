
from ClaseFlores import Flor
import numpy as np
from numpy import ndarray
'''from classMenu import Menu'''
import csv

class ManejadorFlores:
    __array=np.array(0,dtype=Flor)
    

    def __init__(self) -> None:
        print("ave")
        archivo=csv.open("flores.csv")
        reader=csv.reader(archivo,delimiter=";")

        for line in reader:
            f=Flor(line[0],line[1],line[2],line[3],line[4])
            self.__array=np.append(f)
        archivo.close()

    def menuflores(self):
        print("1;Rosas\n2;Girasoles\n3;Dondiego de noche\n4;Hortensias\n5;Petunias\n6;Gladiolos\n7;Nomeolvides\n"
        "8;Cactus de navidad\n9;Ave del paraiso\n10;Jacintos\n11;Aguileña\n12;Boca de dragon")

    def crearramo(self):
        fn=-1
        while(fn!="0"):
            self.menuflores()
            fn=str(input("Ingrese la flor que quiere ingresar o 0 para finalizar"))
            cant=int(input("Ingrese la cantridad de flores que quiere agregar"))

            for elem in self.__array:
                if(fn==elem.getn()):
                    print("AGREGANDO")