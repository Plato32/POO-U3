from classMenu import Menu
from ManejadorEquipo import ManejadorEquipo
from ManejadorJugador import ManejadorJugador
from ManejadorContrato import ManejadorContrato

if __name__=="__main__":
    me=ManejadorEquipo()
    mj=ManejadorJugador()
    mc=ManejadorContrato(mj,me)

    fin=input("Ingrese cualquier tecla para definir un contrato, s para salir\n")
    while fin !="s":
        equip=input("Ingrese nombre de equipo\n")
        jugad=input("Ingrese nombre de jugador\n")
        fechainicio=input("Ingrese fecha de inicio de contrato (dd/mm/aaaa)\n")
        fechafin=input("Ingrese fecha de fin de contrato (dd/mm/aaaa)\n")
        pago=float(input("Ingrese el pago mensual\n"))
        mc.crearcontrato(mj.getjugador(jugad),me.getequipo(equip),fechainicio,fechafin,pago)
        fin=input("\nIngrese cualquier tecla para definir un contrato, s para salir\n")
    mc.prueba()
    m=Menu(me,mj,mc)
    
    '''

Equipo a
Nombre 3
22/10/2025
22/11/2026
50086

Equipo c
Nombre 8
21/10/2021
17/11/2023
509845
s
1
DNI 3


    '''
    
    