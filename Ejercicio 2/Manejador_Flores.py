
from ClaseFlores import Flor
import numpy as np
from numpy import array, ndarray
'''from classMenu import Menu'''
import csv

class ManejadorFlores:
    __array=[]
    

    def __init__(self) -> None:
        __array=np.array(0,dtype=Flor)
        archivo=open("flores.csv")
        reader=csv.reader(archivo,delimiter=";")

        for line in reader:
            f=Flor(line[0],line[1],line[2],line[3])
            self.__array=np.append(self.__array,f)
        archivo.close()

    def menuflores(self):
        print("1;Rosas\n2;Girasoles\n3;Dondiego de noche\n4;Hortensias\n5;Petunias\n6;Gladiolos\n7;Nomeolvides\n"
        "8;Cactus de navidad\n9;Ave del paraiso\n10;Jacintos\n11;Aguileña\n12;Boca de dragon")

    def getarray(self):
        return(self.__array)
    
    def muestramasvend(self):
        list=[]
        
        list=self.__array
        print(list[1].getvent())
        list.sort()
        i=0
        for f in list:
            if i<=5:
                print("Puesto  numero {} de mas vendida lo tiene la flor:{} con: {} ventas".format(i,f.getnom(),f.getvent()))
            i+=1


    
    def muestraflores(self):
        for elem in self.__array:
            print(elem)