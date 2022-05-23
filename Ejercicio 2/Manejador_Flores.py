from ClaseFlores import Flor
import numpy as np
from numpy import ndarray
import csv

class ManejadorFlores:
    __array=np.array(Flor,0)


    def __init__(self) -> None:
        archivo=csv.open("flores.csv")
        reader=csv.reader(archivo,delimiter=";")

        for line in reader:
            f=Flor(line[0],line[1],line[2],line[3],line[4])
            self.__array=np.append(f)
        