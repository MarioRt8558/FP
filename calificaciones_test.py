from calificaciones import *

if __name__ =="_main_":
    #Pruebas para nota_teoria
    print("Prueba nota teoria")
    print(nota_teoria(9.1, 7.2))
    print(nota_teoria(4.0, 6.0))
    print(nota_teoria(4.0, 3.0))
    print(nota_teoria(None, 3.0))
    print(nota_teoria(9.0, None))

    #Pruebas para nota_cuatrimestre
    print("Pruebas nota_cuatrimestre")
    print(nota_cuatrimestre((9.1,7.2), 8.1))
    print(nota_cuatrimestre((4.0,6.0), 5.0))
    print(nota_cuatrimestre((4.0,3.8), None))
    print(nota_cuatrimestre((None,3,8), None))
    print(nota_cuatrimestre((9.0,None), 4.5))

    #Pruebas para nota_continua
    print("Pruebas nota_continua")
    print(nota_continua((.6, 9.9,10.0, 9.8),(9.7,9.5)))
    print(nota_continua((4.4, 4.9, 5.1, 4.7),(4.6,4.8)))
    print(nota_continua((4.0, 6.0, 4.0, 3.0),(5.0, None)))
    print(nota_continua((9.0, None, 4.0, 3.0),(4.5, None)))