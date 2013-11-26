import matrix_generator
import alghoritm
import searchforit
from searchforit import *
from matrix_generator import *
from alghoritm import *



size=40
startPoint=[5,5]
arrivePoint=[15,17]
matrice = matrix_generator(size,startPoint,arrivePoint)
direction1 = farAlg(matrice,startPoint)
print direction1

