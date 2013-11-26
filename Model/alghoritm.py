#Ancora incasinato, pusho per backup piu che altro

import time


punti=[ [0,0,0], [0,0,0] ]
modifier = { 0 : (1,0), 1 : (1,1), 2 : (0,1), 3 : (-1,1), 4 : (-1,0), 5 : (-1,-1), 6 : (0,-1), 7 : (1,-1) }

def triangolator(matrix,startPoint) :
 distance = []
 notarrived = True
 direction = 0
 punti[0] = [startPoint[0],startPoint[1],0]
 punti[1] = [startPoint[0] + modifier[direction][0], startPoint[1] + modifier[direction][1],0]
 x = matrix[punti[0][0]][punti[0][1]][0]
 distance.append(x)
 y = matrix[punti[1][0]][punti[1][1]][0]
 distance.append(y)
 direction= mooveTo(distance, direction)
 distance = []
 while notarrived:
  print punti[-1]
  time.sleep(0.5)
  x = matrix[punti[-1][0] + modifier[direction][0]][punti[-1][1] + modifier[direction][1]][0]
  distance.append(x)
  y = matrix[punti[-2][0] + modifier[direction][0]][punti[-2][1] + modifier[direction][1]][0]
  distance.append(y)
  direction= mooveTo(distance, direction)
  distance = []
  if direction == 8:
   notarrived = False
 


def mooveTo(distance, direction):
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
 print distance
 arrived = True
 for i in distance:
  if i != -2.22:
   arrived = False
 if arrived == True:
   print "Atterraggio..."
   return 8 
 if distance[1] < distance[0]:
  print "Ti stai avvicinando al device"
  print "Muovi in direction "+`direction`
  xcoord = punti[-1][0] + modifier[direction][0]
  ycoord = punti[-1][1] + modifier[direction][1]
  punti.append([xcoord, ycoord, punti[-1][2]])
  raw_input("Wait for enter")
  return direction
 else:
  print "Ti stai allontanando dal device, cambio direction..."
  direction = (direction + 2) % 8
  xcoord = punti[-1][0] + modifier[direction][0]
  ycoord = punti[-1][1] + modifier[direction][1]
  punti.append([xcoord, ycoord, punti[-1][2]])
  print "Muovi in direction "+`direction`
  raw_input("Wait for enter")
  return direction

def boh():
 xcoord = punti[-1][0] + modifier[direction][0]
 ycoord = punti[-1][1] + modifier[direction][1]
 if distance[1] < distance[0]:
  print "Ti stai avvicinando al device"
  punti.append([xcoord,ycoord,punti[-1][2]+1])
  print punti
  print "Muovi in direction "+`direction`
  raw_input("Wait for enter")
  return direction
 else:
  direction = (direction + 2) % 8
  xcoord = punti[-1][0] + modifier[direction][0]
  ycoord = punti[-1][1] + modifier[direction][1]
  for i in punti:
   if i[0] == xcoord and ycoord == i[1] and i[2] < punti[-1][2]:
    direction = (direction + 1) % 8
    xcoord = punti[-1][0] + modifier[direction][0]
    ycoord = punti[-1][1] + modifier[direction][1]
  punti.append([xcoord,ycoord,punti[-1][2]-1])
  print punti
  print "Ti stai allontanando dal device, cambio direction..."
  print "Muovi in direction "+`direction`
  raw_input("Wait for enter")
  return direction
   
  
 
