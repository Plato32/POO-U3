
class Palindromo:
    __palabra = None
    def __init__(self, palabra=None):
        self.__palabra = palabra
    def esPalindromo(self):
        i=0
        j=len(self.__palabra)-1
        bandera = True
        if len(self.__palabra)!=0:
            while i<=j and bandera:
                print("Comparando {} con {}".format(self.__palabra[i], self.__palabra[j]))
                if self.__palabra[i] != self.__palabra[j]:
                    bandera=False
                else:
                    i += 1
                    j -= 1
        else: bandera=False
        return bandera
        
    def setPalabra(self, nuevaPalabra):
        self.__palabra = nuevaPalabra