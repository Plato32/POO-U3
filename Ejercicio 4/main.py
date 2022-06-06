import csv
import CalefactoraGas
import  CalefactorElectrico
import Manejadorcalefactores

if __name__=="__main__":
    archivo=open("calefactor-electrico.csv")
    reader=csv.reader(archivo, delimiter=",")
    dimension=int(input("Ingrese la dimension del arreglo\n"))
    listacalefactores=Manejadorcalefactores.Manejadorcalefactores(dimension)
    for fila in reader:
        auxiliar=CalefactorElectrico.CalefactorElectrico(fila[0], fila[1], int(fila[2]))
        listacalefactores.Agregarcalefactor(auxiliar)
    archivo.close()
    archivo=open("calefactor-a-gas.csv")
    reader=csv.reader(archivo, delimiter=",")
    for fila in reader:
        auxiliar=CalefactoraGas.CalefactoraGas(fila[0], fila[1], fila[2], int(fila[3]))
        listacalefactores.Agregarcalefactor(auxiliar)
    listacalefactores.calcularconsumoagas()
    print("El calefactor a gas natural de menor costo de consumo es: {}".format(listacalefactores.menoragas()))
    listacalefactores.calcularconsumoelectricos()
    print("El calefactor eléctrico de menor consumo es: {}".format(listacalefactores.menorelectrico()))
    print("El calefactor de menor consumo de todos es {}".format(listacalefactores.menor()))