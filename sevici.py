import csv
import math
from collections import namedtuple

Coordenadas = namedtuple('Coordenadas', 'Latitud', 'Longitud')
Estacion = namedtuple( 'Estacion', 'Nombre,bornetas, bornetas_vacias, bicis_disponibles')

def lee_estaciones(fichero):
    res[]
    with open(fichero, encoding='utf-8') as f:
        lector = cvs.reader