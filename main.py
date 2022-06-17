from math import radians, sin, asin, sqrt, cos
import numpy as np
import heapq as hq

matrix = np.ones([12, 144])
hora = 0



def removeEdgeMatrix(firstVertice, secondVertice):
    matrix[firstVertice][secondVertice] = 0


for i in range(18):
    for x in range(4, 12):
        removeEdgeMatrix(x, i)

for i in range(18, 29):
    for x in range(7, 12):
        removeEdgeMatrix(x, i)

for i in range(45, 97):
    for x in range(3, 6):
        removeEdgeMatrix(x, i)

for i in range(133, 144):
    removeEdgeMatrix(6, i)

##Save Matrix
##np.savetxt('matrix.txt', matrix, fmt="%i", delimiter=",")


# Algoritmo para calcular coordenada segun una arista
def get_value_cordenada(x, y):
    lat = round(40.831556 - (x * 0.011111 / 2), 6)
    lon = round(73.942969 - (y * 0.011111 / 2), 6)
    return lat, lon


# Obtener el trafico actual segun la hora
def get_value_trafico_actual(x, y):
    if 1 <= hora <= 5:
        if 1 <= hora <= 5:
            # x = 0 , 3
            if 1 <= x <= 2 and 5 <= y <= 20:
                return 3.1
            elif 2 <= x <= 3 and 21 <= y <= 35:
                return 2.2
            elif 0 <= x <= 3 and 36 <= y <= 45:
                return 1.9
            elif 1 <= x <= 2 and 46 <= y <= 70:
                return 2.4
            elif 0 <= x <= 2 and 71 <= y <= 96:
                return 3.1
            elif 0 <= x <= 1 and 97 <= y <= 108:
                return 2
            elif 2 <= x <= 3 and 97 <= y <= 108:
                return 4.1
            elif 0 <= x <= 1 and 109 <= y <= 125:
                return 1.2
            elif 2 <= x <= 3 and 109 <= y <= 125:
                return 0.8
            elif 0 <= x <= 1 and 126 <= y <= 134:
                return 1.7
            elif 2 <= x <= 3 and 126 <= y <= 134:
                return 2.5
            elif 0 <= x <= 3 and 134 <= y <= 143:
                return 3.2
            # 4-7
            elif 4 <= x <= 6 and 18 <= y <= 26:
                return 1.2
            elif 4 <= x <= 5 and 27 <= y <= 34:
                return 2.3
            elif 4 <= x <= 5 and 35 <= y <= 45:
                return 1.6
            elif 6 <= x <= 7 and 35 <= y <= 45:
                return 2.5
            elif 5 <= x <= 6 and 46 <= y <= 70:
                return 1.6
            elif 6 <= x <= 7 and 71 <= y <= 96:
                return 2.7
            elif 4 <= x <= 5 and 97 <= y <= 107:
                return 3.1
            elif 6 <= x <= 7 and 97 <= y <= 107:
                return 1.6
            elif 4 <= x <= 5 and 108 <= y <= 118:
                return 3
            elif 6 <= x <= 7 and 108 <= y <= 118:
                return 1.1
            elif 4 <= x <= 5 and 119 <= y <= 128:
                return 0.7
            elif 6 <= x <= 7 and 119 <= y <= 128:
                return 0.4
            elif 4 <= x <= 6 and 129 <= y <= 134:
                return 1.7
            elif 5 <= x <= 7 and 135 <= y <= 143:
                return 0.9
                # 8- 11
            elif 8 <= x <= 9 and 28 <= y <= 41:
                return 0.1
            elif 10 <= x <= 11 and 28 <= y <= 41:
                return 0.6
            elif 9 <= x <= 10 and 42 <= y <= 51:
                return 0.9
            elif 10 <= x <= 11 and 52 <= y <= 64:
                return 1.6
            elif 8 <= x <= 9 and 65 <= y <= 78:
                return 2.1
            elif 8 <= x <= 11 and 79 <= y <= 92:
                return 1.1
            elif 8 <= x <= 9 and 93 <= y <= 109:
                return 3.2
            elif 10 <= x <= 11 and 93 <= y <= 109:
                return 0.4
            elif 9 <= x <= 10 and 110 <= y <= 120:
                return 1.3
            elif 10 <= x <= 11 and 121 <= y <= 132:
                return 2.3
            elif 8 <= x <= 9 and 133 <= y <= 140:
                return 3.6
            elif 8 <= x <= 11 and 141 <= y <= 143:
                return 1.6
            else:
                return 1
    elif 6 <= hora <= 12:
        # x = 0 , 3
        if 1 <= x <= 2 and 5 <= y <= 20:
            return 2.4
        elif 2 <= x <= 3 and 21 <= y <= 35:
            return 1.7
        elif 0 <= x <= 3 and 36 <= y <= 45:
            return 0.5
        elif 1 <= x <= 2 and 46 <= y <= 70:
            return 2.6
        elif 0 <= x <= 2 and 71 <= y <= 96:
            return 1.3
        elif 0 <= x <= 1 and 97 <= y <= 108:
            return 1.7
        elif 2 <= x <= 3 and 97 <= y <= 108:
            return 0.3
        elif 0 <= x <= 1 and 109 <= y <= 125:
            return 0.7
        elif 2 <= x <= 3 and 109 <= y <= 125:
            return 2.1
        elif 0 <= x <= 1 and 126 <= y <= 134:
            return 3.1
        elif 2 <= x <= 3 and 126 <= y <= 134:
            return 0.6
        elif 0 <= x <= 3 and 134 <= y <= 143:
            return 0.7
        # 4-7
        elif 4 <= x <= 6 and 18 <= y <= 26:
            return 2.3
        elif 4 <= x <= 5 and 27 <= y <= 34:
            return 3.7
        elif 4 <= x <= 5 and 35 <= y <= 45:
            return 4.2
        elif 6 <= x <= 7 and 35 <= y <= 45:
            return 1.2
        elif 5 <= x <= 6 and 46 <= y <= 70:
            return 5.2
        elif 6 <= x <= 7 and 71 <= y <= 96:
            return 4.5
        elif 4 <= x <= 5 and 97 <= y <= 107:
            return 3.8
        elif 6 <= x <= 7 and 97 <= y <= 107:
            return 5.7
        elif 4 <= x <= 5 and 108 <= y <= 118:
            return 3.9
        elif 6 <= x <= 7 and 108 <= y <= 118:
            return 4.2
        elif 4 <= x <= 5 and 119 <= y <= 128:
            return 3.1
        elif 6 <= x <= 7 and 119 <= y <= 128:
            return 5.3
        elif 4 <= x <= 6 and 129 <= y <= 134:
            return 4.5
        elif 5 <= x <= 7 and 135 <= y <= 143:
            return 3.2
            # 8- 11
        elif 8 <= x <= 9 and 28 <= y <= 41:
            return 3.2
        elif 10 <= x <= 11 and 28 <= y <= 41:
            return 3.6
        elif 9 <= x <= 10 and 42 <= y <= 51:
            return 2.3
        elif 10 <= x <= 11 and 52 <= y <= 64:
            return 3.5
        elif 8 <= x <= 9 and 65 <= y <= 78:
            return 2.4
        elif 8 <= x <= 11 and 79 <= y <= 92:
            return 1.8
        elif 8 <= x <= 9 and 93 <= y <= 109:
            return 2.7
        elif 10 <= x <= 11 and 93 <= y <= 109:
            return 3.3
        elif 9 <= x <= 10 and 110 <= y <= 120:
            return 0.4
        elif 10 <= x <= 11 and 121 <= y <= 132:
            return 1.1
        elif 8 <= x <= 9 and 133 <= y <= 140:
            return 3.2
        elif 8 <= x <= 11 and 141 <= y <= 143:
            return 4.4
        else:
            return 1
    elif 13 <= hora <= 18:
        # x = 0 , 3
        if 1 <= x <= 2 and 5 <= y <= 20:
            return 5.2
        elif 2 <= x <= 3 and 21 <= y <= 35:
            return 4.1
        elif 0 <= x <= 3 and 36 <= y <= 45:
            return 3.8
        elif 1 <= x <= 2 and 46 <= y <= 70:
            return 4.4
        elif 0 <= x <= 2 and 71 <= y <= 96:
            return 2.5
        elif 0 <= x <= 1 and 97 <= y <= 108:
            return 1.3
        elif 2 <= x <= 3 and 97 <= y <= 108:
            return 3.2
        elif 0 <= x <= 1 and 109 <= y <= 125:
            return 1.9
        elif 2 <= x <= 3 and 109 <= y <= 125:
            return 5.1
        elif 0 <= x <= 1 and 126 <= y <= 134:
            return 3.4
        elif 2 <= x <= 3 and 126 <= y <= 134:
            return 4.6
        elif 0 <= x <= 3 and 134 <= y <= 143:
            return 4.8
        # 4-7
        elif 4 <= x <= 6 and 18 <= y <= 26:
            return 5.4
        elif 4 <= x <= 5 and 27 <= y <= 34:
            return 3.4
        elif 4 <= x <= 5 and 35 <= y <= 45:
            return 3.6
        elif 6 <= x <= 7 and 35 <= y <= 45:
            return 3.1
        elif 5 <= x <= 6 and 46 <= y <= 70:
            return 5.7
        elif 6 <= x <= 7 and 71 <= y <= 96:
            return 4.2
        elif 4 <= x <= 5 and 97 <= y <= 107:
            return 4.1
        elif 6 <= x <= 7 and 97 <= y <= 107:
            return 4.8
        elif 4 <= x <= 5 and 108 <= y <= 118:
            return 5.5
        elif 6 <= x <= 7 and 108 <= y <= 118:
            return 3.8
        elif 4 <= x <= 5 and 119 <= y <= 128:
            return 2.4
        elif 6 <= x <= 7 and 119 <= y <= 128:
            return 3.1
        elif 4 <= x <= 6 and 129 <= y <= 134:
            return 4.4
        elif 5 <= x <= 7 and 135 <= y <= 143:
            return 5
            # 8- 11
        elif 8 <= x <= 9 and 28 <= y <= 41:
            return 2.4
        elif 10 <= x <= 11 and 28 <= y <= 41:
            return 1.7
        elif 9 <= x <= 10 and 42 <= y <= 51:
            return 3.3
        elif 10 <= x <= 11 and 52 <= y <= 64:
            return 3.9
        elif 8 <= x <= 9 and 65 <= y <= 78:
            return 4.6
        elif 8 <= x <= 11 and 79 <= y <= 92:
            return 3.1
        elif 8 <= x <= 9 and 93 <= y <= 109:
            return 5.3
        elif 10 <= x <= 11 and 93 <= y <= 109:
            return 4.9
        elif 9 <= x <= 10 and 110 <= y <= 120:
            return 2.5
        elif 10 <= x <= 11 and 121 <= y <= 132:
            return 4
        elif 8 <= x <= 9 and 133 <= y <= 140:
            return 2.2
        elif 8 <= x <= 11 and 141 <= y <= 143:
            return 5.2
        else:
            return 1
    elif 19 <= hora <= 24:
        # x = 0 , 3
        if 1 <= x <= 2 and 5 <= y <= 20:
            return 1.1
        elif 2 <= x <= 3 and 21 <= y <= 35:
            return 2
        elif 0 <= x <= 3 and 36 <= y <= 45:
            return 1.7
        elif 1 <= x <= 2 and 46 <= y <= 70:
            return 2.3
        elif 0 <= x <= 2 and 71 <= y <= 96:
            return 0.4
        elif 0 <= x <= 1 and 97 <= y <= 108:
            return 3.2
        elif 2 <= x <= 3 and 97 <= y <= 108:
            return 1.8
        elif 0 <= x <= 1 and 109 <= y <= 125:
            return 0.4
        elif 2 <= x <= 3 and 109 <= y <= 125:
            return 2.8
        elif 0 <= x <= 1 and 126 <= y <= 134:
            return 2.9
        elif 2 <= x <= 3 and 126 <= y <= 134:
            return 4.9
        elif 0 <= x <= 3 and 134 <= y <= 143:
            return 5.3
        # 4-7
        elif 4 <= x <= 6 and 18 <= y <= 26:
            return 4.6
        elif 4 <= x <= 5 and 27 <= y <= 34:
            return 3.8
        elif 4 <= x <= 5 and 35 <= y <= 45:
            return 4.9
        elif 6 <= x <= 7 and 35 <= y <= 45:
            return 5.1
        elif 5 <= x <= 6 and 46 <= y <= 70:
            return 3.8
        elif 6 <= x <= 7 and 71 <= y <= 96:
            return 5.8
        elif 4 <= x <= 5 and 97 <= y <= 107:
            return 2.9
        elif 6 <= x <= 7 and 97 <= y <= 107:
            return 3.7
        elif 4 <= x <= 5 and 108 <= y <= 118:
            return 4.8
        elif 6 <= x <= 7 and 108 <= y <= 118:
            return 2.9
        elif 4 <= x <= 5 and 119 <= y <= 128:
            return 3.9
        elif 6 <= x <= 7 and 119 <= y <= 128:
            return 4.7
        elif 4 <= x <= 6 and 129 <= y <= 134:
            return 5.6
        elif 5 <= x <= 7 and 135 <= y <= 143:
            return 7
        # 8- 11
        elif 8 <= x <= 9 and 28 <= y <= 41:
            return 3.5
        elif 10 <= x <= 11 and 28 <= y <= 41:
            return 2.8
        elif 9 <= x <= 10 and 42 <= y <= 51:
            return 3.5
        elif 10 <= x <= 11 and 52 <= y <= 64:
            return 2.9
        elif 8 <= x <= 9 and 65 <= y <= 78:
            return 4.5
        elif 8 <= x <= 11 and 79 <= y <= 92:
            return 2.8
        elif 8 <= x <= 9 and 93 <= y <= 109:
            return 4.1
        elif 10 <= x <= 11 and 93 <= y <= 109:
            return 3.4
        elif 9 <= x <= 10 and 110 <= y <= 120:
            return 3.8
        elif 10 <= x <= 11 and 121 <= y <= 132:
            return 3.2
        elif 8 <= x <= 9 and 133 <= y <= 140:
            return 4.2
        elif 8 <= x <= 11 and 141 <= y <= 143:
            return 5.7
        else:
            return 1


# Actividades de implementación de algoritmo de cálculo de peso de arista en función
# de su longitud y factor de tráfico calculado.
def get_peso_arista_segun_trafico(x, y):
    trafico = get_value_trafico_actual(x, y)
    if trafico == None:
        return 0
    return trafico


# Obtener el longitud segun coordenadas
def get_value_longitud_trafico_segun_coordenadas(coord_1,coord_2):
    def haversine(lon1, lat1, lon2, lat2):
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r

    return  round(haversine(coord_1[0], coord_1[1], coord_2[0], coord_2[1]),6)

def get_longitud_entre_aristas(x,y,x1,y1):
    return  round(get_value_longitud_trafico_segun_coordenadas(get_value_cordenada(x,y), get_value_cordenada(x1,y1)) * get_peso_arista_segun_trafico(x, y),6)


# Actividades de implementación de algoritmos para actualizar pesos de aristas en
# función a la hora del día.
def update_peso_arista_segun_trafico(hora, nuevo):
    hora = nuevo


#a. Actividades de implementación de algoritmos para calcular la ruta más corta y 2 rutas
#alternativas

#Rutas Mas Corta
def dijkstra(x1,y1,x2,y2, type):
    queue = []

    queue.append([x1, y1])

    fatherX = np.zeros([12, 144])
    fatherY = np.zeros([12, 144])

    visited = np.zeros([12, 144])
    peso = np.zeros([12, 144])

    xFather = x1
    yFather = y1

    while queue:

        [x,y] = queue[len(queue)-1]
        queue.remove([x,y])

        if visited[x,y] == 0 and matrix[x][y] == 1 and  x1 <= x <= x2 and y1 <= y <=y2:
            visited[x,y] = 1

            peso[x,y] = peso[xFather, yFather] + get_longitud_entre_aristas(x,y,xFather,yFather)
            print(" ")
            print("------")
            print("x,y:",x,y)
            print("Padre: ",xFather,yFather)
            print("peso acomulado: ", peso[x, y])
            print("longitud(x,y): ", get_longitud_entre_aristas(x, y, xFather, yFather))
            print("------")
            print(" ")

            fatherX[x,y] = xFather
            fatherY[x,y] = yFather

            xFather = x
            yFather = y
            if type == "corto":
                set_append_segun_peso_corto(queue, x, y)
            elif type == "alterna1":
                set_append_segun_peso_alterna_1(queue,x , y)
            elif type == "alterna2":
                set_append_segun_peso_alterna_2(queue, x, y)
            if x == x2 and y == y2:
                break


#ordernar segun sus pesos en el queue
def set_append_segun_peso_corto(queue, x,y):
    lista = []
    if 12 > x >= 0 and 144 > y - 1 >= 0:
        lista.append([x, y - 1, get_longitud_entre_aristas(x,y,x,y-1)])

    if 12 > x + 1 >= 0 and 144 > y >= 0:
        lista.append([x + 1, y, get_longitud_entre_aristas(x,y,x + 1,y)])

    if 12 > x >= 0 and 144 > y + 1 >= 0:
        lista.append([x, y + 1, get_longitud_entre_aristas(x,y,x, y + 1)])

    if 12 > x - 1 >= 0 and 144 > y >= 0:
        lista.append([x - 1, y, get_longitud_entre_aristas(x,y,x - 1, y)])


    while len(lista) > 0:
        menor = lista[0]
        for x in range(len(lista)):
            if menor[2] < lista[x][2]:
                menor = lista[x]
        queue.append([menor[0],menor[1]])
        lista.remove(menor)


#alterna 1
def set_append_segun_peso_alterna_1(queue, x,y):
    lista = []
    if 12 > x >= 0 and 144 > y - 1 >= 0:
        lista.append([x, y - 1, get_longitud_entre_aristas(x,y,x,y-1)])

    if 12 > x + 1 >= 0 and 144 > y >= 0:
        lista.append([x + 1, y, get_longitud_entre_aristas(x,y,x + 1,y)])

    if 12 > x >= 0 and 144 > y + 1 >= 0:
        lista.append([x, y + 1, get_longitud_entre_aristas(x,y,x, y + 1)])

    if 12 > x - 1 >= 0 and 144 > y >= 0:
        lista.append([x - 1, y, get_longitud_entre_aristas(x,y,x - 1, y)])


    while len(lista) > 0:
        mayor = lista[0]
        for x in range(len(lista)):
            if mayor[2] > lista[x][2]:
                mayor = lista[x]
        queue.append([mayor[0],mayor[1]])
        lista.remove(mayor)


#alterna 2
def set_append_segun_peso_alterna_2(queue, x,y):
    if 12 > x - 1 >= 0 and 144 > y >= 0:
        hq.heappush(queue,[x - 1, y])
    if 12 > x + 1 >= 0 and 144 > y >= 0:
        hq.heappush(queue,[x + 1, y])
    if 12 > x >= 0 and 144 > y - 1 >= 0:
        hq.heappush(queue,[x, y - 1])
    if 12 > x >= 0 and 144 > y + 1 >= 0:
        hq.heappush(queue,[x, y + 1])


# Ejemplos

#print(get_longitud_entre_aristas(0,0,1,0))
#print(get_longitud_entre_aristas(1,0,0,0))

'''
hora = 8

#Camino mas corto
dijkstra(1,44,8,73,"corto")

#Camnio Alterno 1
dijkstra(1,44,8,73,"alterna1")

#Camino Alterno 2
dijkstra(1,44,8,73,"alterna2")
'''

#Cambio de hora 4
hora = 4

#Camino mas corto
dijkstra(1,20,10,142,"corto")

#Camnio Alterno 1
dijkstra(1,20,10,142,"alterna1")

#Camino Alterno 2
dijkstra(1,20,10,142,"alterna2")

print("-------------- OTRA HORA --------")


#Cambio de hora 4
hora = 23

#Camino mas corto
dijkstra(1,20,10,142,"corto")

#Camnio Alterno 1
dijkstra(1,20,10,142,"alterna1")

#Camino Alterno 2
dijkstra(1,20,10,142,"alterna2")