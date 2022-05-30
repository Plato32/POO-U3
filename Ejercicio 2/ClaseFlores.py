

class Flor():
    __numero:int
    __nombre:str
    __color:str
    __descripcion:str
    __cantvent:int

    def __init__(self,numero,nombre,color,descripcion) -> None:
    
        self.__numero=numero
        self.__nombre=nombre
        self.__color=color
        self.__descripcion=descripcion
        self.__cantvent=0
    
    def __str__(self) -> str:
        return "{}, {}, {}, {}".format(self.__numero,self.__nombre,self.__color,self.__descripcion)
    
    def getn(self):
        return(self.__numero)
    
    def cantventas(self):
        self.__cantvent+=1
        print("lleva vendidas",self.__cantvent,"unidades")

    def getnom(self):
        return(self.__nombre)

    def getvent(self):
        return(self.__cantvent)
    
    def __gt__(self,otro):
        b=False
        if (type(self)==type(otro)) and (type(otro) == Flor):
            b=self.getvent()>otro.getvent()
        return(b)
    
    
        