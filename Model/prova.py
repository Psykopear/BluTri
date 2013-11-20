import matrix_generator
import alghoritm
from matrix_generator import *
from alghoritm import *


size=20
startPoint=[10,10]
arrivePoint=[5,5]
matrice = matrix_generator(size,startPoint,arrivePoint)
print_matrix(matrice,size)
triangolator(matrice,startPoint)
