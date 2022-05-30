from ClaseFlores import Flor

class Ramo:
    __tamaño:int
    __tipo_de_tamaño:str
    __flores=[]


    def __init__(self,tamaño) -> None:
        self.__tamaño=tamaño
        if self.__tamaño == 1 or self.__tamaño < 3:
            self.__tipo_de_tamaño = 'Chico'
        if self.__tamaño >= 3:
            self.__tipo_de_tamaño = 'Mediano'
        if self.__tamaño >= 5:
            self.__tipo_de_tamaño = 'Grande'
        self.__flores = []
        
        
    def muestrafloresenramo(self):
        for f in self.__flores:
            print(f)
            
    def addFlor(self,flor):
        self.__flores.append(flor)
 
    

    