class Carrera:
    __codigo: int
    __nombre:str
 #   __fecha_inicio:str
    __duracion:str
    __titulo:str
    __tipo=str
    def __init__(self,codigo, nombre,titulo,duracion,tipo):
        self.__codigo=codigo
        # print("codigo:",self.__codigo)
        self.__nombre=nombre
        # print("nombre:",self.__nombre)
        self.__titulo=titulo
        #self.__fecha_inicio=fecha
        self.__duracion=duracion
        self.__tipo=tipo
    
    def __str__(self) -> str:
        return("{} {} {} {} {}".format(self.__codigo,self.__nombre,self.__titulo,self.__duracion,self.__tipo))
    
    def getname(self):
        return(self.__nombre)
    
    def getcode(self):
        return(self.__codigo)




