from math import radians, sin, asin, sqrt, cos
import numpy as np
matrix = np.ones([144,12])
def removeEdgeMatrix(firstVertice, secondVertice):
    matrix[firstVertice][secondVertice] = 0

for i in range(18):
  for x in range(4,12):
    removeEdgeMatrix(i,x)

for i in range(18,29):
  for x in range(7,12):
    removeEdgeMatrix(i,x)

for i in range(45,97):
  for x in range(2,6):
    removeEdgeMatrix(i,x)

for i in range(133,144):
    removeEdgeMatrix(i,6)

#np.savetxt('matrix.txt', matrix, fmt="%i", delimiter=",")

# Algoritmo para calcular coordenada segun una arista
def get_value_cordenada(x, y):
    lat = round(40.831556 - (x * 0.011111 / 2), 6)
    lon = round(73.942969 - (y * 0.011111 / 2), 6)
    return lat, lon


# Obtener el trafico actual segun la hora
def get_value_trafico_actual(hora):
    if 1 <= hora <= 5:
        return 1
    elif 6 <= hora <= 12:
        return 2
    elif 13 <= hora <= 18:
        return 3
    elif 19 <= hora <= 24:
        return 4


# Obtener el longitud segun coordenadas
def get_value_longitud_segun_coordenada(coord_1):

    def haversine(lon1, lat1, lon2, lat2):
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r

    return haversine(40.831556, 73.94296, coord_1[0], coord_1[1])
