from ClaseRamo import Ramo
import csv
class ManejadorRamos:
    __listaR=[]

    def __init__(self,ramo) -> None:
        __listaR=self.__listaR.append(ramo)
    
    
    '''def __init__(self) -> None:
            archivo=csv.open("flores.csv")
            reader=csv.reader(archivo,delimiter=";")

            for line in reader:
                f=Flor(line[0],line[1],line[2],line[3],line[4])
                self.__array=np.append(f)
            archivo.close()'''

    