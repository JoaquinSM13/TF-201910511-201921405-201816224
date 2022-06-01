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

np.savetxt('matrix.txt', matrix, fmt="%i", delimiter=",")