#Genera una matrice quadrata sizeXsize piena di 0
#Mette un -1 all'indice startPoint e -2 in arrivePoint


def matrix_generator(size, startPoint, arrivePoint):
 matrix = [ [ 0 for i in range(size)] for j in range(size) ]
 matrix[startPoint[0]][startPoint[1]] = -1
 matrix[arrivePoint[0]][arrivePoint[1]] = -2
 print matrix

matrix_generator(5,[0,0],[2,2])
