from ClaseRamo import Ramo


class Flor(Ramo):
    __numero:int
    __nombre:str
    __color:str
    __descripcion:str

    def __init__(self,tamaño,numero,nombre,color,descripcion) -> None:
        super().__init__(self,tamaño)
        self.__numero=numero
        self.__nombre=nombre
        self.__color=color
        self.__descripcion=descripcion
    
    def getn(self):
        return(self.__numero)
    
    
        