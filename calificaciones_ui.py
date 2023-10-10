from cgitb import reset
from tracemalloc import reset_peak
from calificaciones import *

def solicita_nota():
    nombre = input("Introduzca su nombre: ")
    notas_teoria = lee_notas("Teorico: ",4)
    notas_practica = lee_notas("Practico:",2)
    return ( nombre,notas_teoria, notas_practica)


def lee_notas(tipo_examen, numero_examenes):
    res = []
    for Indice in range(1, numero_examenes+1):
        valor =input(f"Introduzca la nota del examen teorico {tipo_examen} {Indice} (- si no se ha presentado): ")
        valor = a_decimal(valor)
        res.append(valor)
    return res 


def a_decimal(valor):
    if valor == "-":
        res =  None
    else:
        res = float(valor)
    return res

def mostrar_notas(entrada):  
    nombre = entrada[0]
    ntc1 = nota_teoria(entrada[1][0], entrada [1][1])
    p1 = entrada [2][0]
    c1 = nota_cuatrimestre(entrada[1][:2], p1)

    ntc2 = nota_teoria(entrada[1][2], entrada [1][3])
    p2 = entrada [2][1]
    c2 = nota_cuatrimestre(entrada[1][:2], p2)

    nota_final = nota_continua(entrada[1], entrada[2])



    print(f"Hola, {nombre}")
    print("Tus notas del primer cuatrimestre son:")
    print(f"Teoria {ntc1}, Practica {p1}, Cuatrimestre {c1}")
    print("Tus notas del segundo cuatrimestre son:")
    print(f"Teoria {ntc2} Practica {p2}, Cuatrimestre {c2}")
    print(f"Tu notaa final de la asignatura es {nota_final}")

if __name__ == "__main__":
    notas = solicita_nota()
    mostrar_notas(notas)
