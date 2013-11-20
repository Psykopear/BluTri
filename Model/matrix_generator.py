#Genera una matrice quadrata sizeXsize piena di 0
#Mette un -1 all'indice startPoint e -2 in arrivePoint
import math
import fpformat

def matrix_generator(size, startPoint, arrivePoint):
 matrix = [ [ 0 for i in range(size)] for j in range(size) ]
 for i in range(size):
  for j in range(size):
   matrix[i][j] = [fpformat.fix(math.sqrt(math.fabs(pow((arrivePoint[0] - i),2) + pow((arrivePoint[1] - j), 2))),3),"*"]
 matrix[startPoint[0]][startPoint[1]][1] = "S"
 matrix[arrivePoint[0]][arrivePoint[1]] = [-2.22,"A"]
 return matrix


def print_matrix(matrix, size):
 for i in range(size):
  for j in range(size):
   print "[",matrix[i][j][1],"]",
  print
