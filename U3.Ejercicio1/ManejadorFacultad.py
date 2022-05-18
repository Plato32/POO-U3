import csv
from Facultad import Facultad
from Carrera import Carrera

class ManejadorFacultades:
    __lista=[]

    def __init__(self) -> None:
        self.__lista=self.lecturaArchivos()
        #print("LA lista tiene carrreras:",len(self.__lista))
    

    def lecturaArchivos(self):
        
        listaf=[]
        archivo = open( 'Facultades.csv')
        reader = csv.reader( archivo, delimiter = ',' )
        fila=next(reader)
        bandera = True
        while bandera:
            #print('Facultad')
            #print(fila)
            
            #print('Carreras:')
            listac=[]
            filaCarrera=next(reader)
            
            while bandera and fila[0]==filaCarrera[0]:
                #print(filaCarrera)
                try:
                    # print(filaCarrera[1])
                    # print(filaCarrera[2])
                    c=Carrera(filaCarrera[1],filaCarrera[2],filaCarrera[3],filaCarrera[3],filaCarrera[4])
                    filaCarrera=next(reader)
                    listac.append(c)

                except StopIteration:
                    bandera=False
            f=Facultad(fila[0],fila[1],fila[2],fila[3],fila[4],listac)
            listaf.append(f)  
            fila=filaCarrera
        archivo.close()
        # print("en carga:",len(listaf))
        return(listaf)
        
    def mostrarcarrerascodigo(self,cod):
        print("")
        for elem in self.__lista:
            print(elem.getnom())
            print("")
            if(elem.getcodigo()==cod):
                elem.muestracarre()
    def buscacarrera(self, nom):
        i=0
        band=False
        while(not(band))and(i<len(self.__lista)):
            band=self.__lista[i].getcarrera(nom)
            i+=1
        if(not(band)):
            print("Carrera no encontrada")



    


        '''for elem in listaf:

            print(elem)
            print(elem.muestracarre())'''