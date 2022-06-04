from ClaseEquipo import Equipo
import csv
from numpy import array, ndarray
import numpy as np


class ManejadorEquipo:
    __arrayE=[]

    def __init__(self):
        list=[]
        archivo = open("equipos.csv")
        reader=csv.reader(archivo,delimiter=";")
        fila=next(reader)
        cant=int(fila[0])
        for i in range(cant):
            fila=next(reader)
            e=Equipo(fila[0], fila[1])
            list.append(e)
        archivo.close()
        self.__arrayE=np.array(list)

        # for el in self.__arrayE:
        #     print(el)
        # self.__arrayE=np.array(0,dtype=Equipo)
        # archivo = open("equipos.csv")
        # reader=csv.reader(archivo,delimiter=";")
        # fila=next(reader)
        # cant=int(fila[0])
        # for i in range(cant):
        #     fila=next(reader)
        #     e=Equipo(fila[0], fila[1])
        #     self.__arrayE=np.append(self.__arrayE,e)
        # archivo.close()
        # for el in self.__arrayE:
        #     print(el)
        
        
    def getequipo(self,nomb):
        band=False
        equ=None
        i=0
        while i<len(self.__arrayE)and (not band):
            if nomb== self.__arrayE[i].getnom():
               band=True
               equ=self.__arrayE[i]
            i+=1
            
        return(equ)
        

        
       

    # def getequipo(self, nomequipo):
    #     i=0
    #     bandera = True
    #     valorretorno = None
    #     while i<len(self.__arreEquipo) and bandera:
    #         print(self.__arreEquipo[i].getnombre())
    #         if self.__arreEquipo[i].getnombre() == nomequipo:
    #             valorretorno = self.__arreEquipo[i]
    #             bandera = False
    #         else:
    #             valorretorno = None
    #         i+=1

    #     return valorretorno
