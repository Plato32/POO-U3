'''from ClaseFlores import Flor'''
class Ramo:
    __tamaño:int
    __flores=[]


    def __init__(self,tamaño,flor=None) -> None:
        self.__tamaño=tamaño
        
        if flor!=None:
            self.addFlor(flor,1)
 
    def addFlor(self, flor, cantidad):
        for i in range(cantidad):
            self.__flores.append(flor)
 
    