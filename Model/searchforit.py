#Ancora incasinato, pusho per backup piu che altro

import time
import collections
import matrix_generator
import os
from matrix_generator import print_matrix
from collections import namedtuple

punti = []

Point =  namedtuple('Point', ['x','y','w'])
#Il sistema di riferimento e' il quarto quadrante, quindi andando a SUD, Y aumenta, mentre a NORD diminuisce
modifier = { 0 : (1,0), 1 : (1,-1), 2 : (0,-1), 3 : (-1,-1), 4 : (-1,0), 5 : (-1,1), 6 : (0,1), 7 : (1,1) }

#direzioni:
# 0 = E (+1,0)
# 1 = NE (+1,+1)
# 2 = N (0,+1)
# 3 = NO (-1,+1)
# 4 = O (-1,0)
# 5 = SO (-1,-1)
# 6 = S (0,-1)
# 7 = SE (+1,-1)
# 8 = ARRIVATI

def addPoints(p, matrix):
 punti.append(p)
 x = getattr(p, 'x')
 y = getattr(p, 'y')
 val = matrix[x][y][1]
 if val != 'S':
  matrix[x][y][1] = 'O'

 if len(punti) >= 2 :
  pprev = punti[-2]
  xprev = getattr(pprev, 'x')
  yprev = getattr(pprev, 'y')
  valprev = matrix[xprev][yprev][1]
  if valprev != 'S': 
   matrix[xprev][yprev][1] = '+'
  

 os.system('clear')
 print_matrix(matrix)
 raw_input()

#[p]unto di partenza, [m]atrice, [d]irezione
def move(p,m,d):
 pass

def farAlg(matrix, SP):
#This is a comment
 direction = 0
 distance = []
 
 x1 = SP[0]
 y1 = SP[1]
 ps = Point(x1,y1,0)
 distance.append(matrix[x1][y1][0])
 addPoints(ps, matrix)

 x2 = x1 + modifier[direction][0]
 y2 = y1 + modifier[direction][1]
 p = Point(x2,y2,0)
 distance.append(matrix[x2][y2][0])
 addPoints(p, matrix)
 

 direction = direction + 2

 x3 = x2 + modifier[direction][0]
 y3 = y2 + modifier[direction][1]
 p = Point(x3,y3,0)
 addPoints(p, matrix)
 distance.append(matrix[x3][y3][0])
 
 addPoints(ps, matrix)

 dist1 = distance[0]
 dist2 = distance[1]
 dist3 = distance[2]
 
 xdir = 0
 ydir = 0
 if dist1 > dist2:
  xdir = '+'
 else:
  xdir = '-'
 if dist2 < dist3:
  ydir = '+'
 else:
  ydir = '-'

 if xdir == '+':
  if ydir == '+':
   direction = 7
  elif ydir == '-':
   direction = 1
  else:
   direction = 0
 elif xdir == '-':
  if ydir == '+':
   direction = 5
  elif ydir == '-':
   direction = 3
  else:
   direction = 4
 else:
  if ydir == '+':
   direction = 6
  elif ydir == '-':
   direction = 2
  else:
   direction = 8

 return direction

 
