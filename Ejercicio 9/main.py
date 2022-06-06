from ClassPalindromo import Palindromo
import unittest

class TestPalindromos(unittest.TestCase):
    def setUp(self):
        self.__palindromo=Palindromo(None)
    def testvacio(self):
        self.__palindromo.setPalabra("")
        self.assertFalse(self.__palindromo.esPalindromo())
    def testpalindromopar(self):
        self.__palindromo.setPalabra("narran")
        self.assertTrue(self.__palindromo.esPalindromo)
    def testpalindromoimpar(self):
        self.__palindromo.setPalabra("radar")
        self.assertTrue(self.__palindromo.esPalindromo)
    def testNopalindromopar(self):
        self.__palindromo.setPalabra("ejercito")
        self.assertFalse(self.__palindromo.esPalindromo())
    def testNopalindromoimpar(self):
        self.__palindromo.setPalabra("piedra")
        self.assertFalse(self.__palindromo.esPalindromo())


if __name__=="__main__":
    unittest.main()

# if __name__=="__main__":
#     c=1
#     t=input("Test Ingrese 1 para test manual o 2 para test automatico: ")
#     if t==2:
#         unittest.main()
#     elif t == 1:
#         while(c!=0):
#             pal=Palindromo()
#             palabra=str(input("Ingrese un palindromo: "))
#             pal.setPalabra(palabra)
#             band=pal.esPalindromo()
#             if band:
#                 print("La palabra ingresada es un  palindromo")
#             else: print("La palabra ingresada no es un  palindromo")
#             c=int(input("Si desea finalizar presione 0 si desea seguir con el test presione 1: "))
    
'''
    Dada la Clase Palindromo, que tiene como atributo una palabra y
     una función para chequear que la palabra es palíndromo o no, 
     dicha función devuelve True si la palabra es palíndromo, False en caso contrario.

Regla de Negocio: una palabra es palíndromo si se puede chequear que se escribe igual de adelante hacia atrás 
y de atrás hacia adelante. Ejemplos: ana, ANA, anana, MENEM.

La implementación provista por una empresa subcontratista, “Mi Softw@re siempre @nda”, es la siguiente:

class Palindromo:
    __palabra = None
    def __init__(self, palabra):
        self.__palabra = palabra
    def esPalindromo(self):
        i=0
        j=-len(self.palabra)
        bandera = True
        while i<abs(j) and bandera:
           if self.__palabra[i] != self.__palabra[i]:
               bandera=False
           else:
               i += 1
               j += 1
        return bandera
    def setPalabra(self, nuevaPalabra):
        self.__palabra = nuevaPalabra

 Su tarea consiste en diseñar los tests para probar la implementación realizada por la empresa,
  en caso de que alguno no funcione, deberá corregir la función correspondiente.'''