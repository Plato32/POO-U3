import json
from pathlib import Path
from Lista import Lista
from Televisor import Televisor
from Lavarropas import Lavarropas
from Heladera import Heladera

class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Lista':
                aparatos=d['aparatos']
                daparato = aparatos[0]
                manejador=class_()
                for i in range(len(aparatos)):
                    daparato=aparatos[i]
                    class_name=daparato.pop('__class__')
                    class_=eval(class_name)
                    atributos=daparato['__atributos__']
                    unAparato=class_(**atributos)
                    manejador.AgregarElemento(unAparato)
        return manejador
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
        return diccionario
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)