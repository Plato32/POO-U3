from Carrera import Carrera


class Facultad:
    __codigo: int
    __nombre:str
    __direccion:str
    __localidad:str
    __telefono:str
    __listacarre=[]

    def __init__(self,codigo,nombre,direccion,localidad,telefono,listc):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        #print("facultad{}{}".format(self.__nombre,len(listc)))
        for carrera in listc:
            self.__listacarre.append(carrera)
       

    def __str__(self) -> str:
        return("{} {} {} {} {}".format(self.__codigo,self.__nombre,self.__direccion,self.__localidad,self.__telefono))

    def getcodigo(self):
        return(self.__codigo)
    
    def getnom(self):
        return(self.__nombre)

    def muestracarre(self):
        for el in self.__listacarre:
            print(el)

    def getcarrera(self,name):
        band=False
        for el in self.__listacarre:
            if(el.getname()==name):
                band=True
                cb=(str(self.__codigo)+","+str(el.getcode()))
                print("Codigo carrera:{} Facultad:{} Localidad:{}".format(cb,self.__nombre,self.__localidad))
                '''mostrar código ( código de Facultad + código de carrera),
                 nombre y localidad de la facultad donde esta se dicta.'''
        return(band)
            

        
