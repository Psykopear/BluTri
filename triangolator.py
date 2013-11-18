#IDEA: Dati tre dispositivi messi in triangolo, che restituiscono 0
#quando si e abbastanza vicini, e valori negativi il resto del tempo,
#si misurano le intensita di tutti e tre, e quando tutte rimangono
#su 0 per un tot di misurazioni consecutive significa che
#ci si e avvicinati

import os
import time
#Random serve solo per provare perche non ho bluetooth
import random
from random import randint

def triangolator() :
 MACS = ["10:BF:48:EA:6A:E2"]
 RSSI = []
 notarrived = True
 direzione = 0
 while notarrived:
  for i in MACS:
   x = randint(-256,50)
#vedi anche "rfcomm connect 0 <MAC> <CHANNEL>" per connettersi, forse meglio di hcitool
#e riconnettere solo in caso non sia piu connesso
   #os.system("hcitool cc "+i)
   time.sleep(0.1)
   #x = os.system("hcitool rssi "+i+" 2> /dev/null") 
   #if x != 256:
   # x = x.split(': ')[1]
   #else:
   # x = -256
   #os.system("hcitool dc "+i)
   RSSI.append(x)
  if len(RSSI) > 5:
   RSSI.pop(0)
   direzione = muoviInDirezione(RSSI, direzione)
   RSSI = []
   if direzione == 8:
    notarrived = False
 


def muoviInDirezione(ar, direzione):
#direzioni:
# 0 = E
# 1 = NE
# 2 = N
# 3 = NO
# 4 = O
# 5 = SO
# 6 = S
# 7 = SE
# 8 = ARRIVATI
 arrived = True
 for i in ar:
  if i < 0:
   arrived = False
 if arrived == True:
   print "Atterraggio..."
   return 8 
 dev = ar
 avv1 = 0
 all1 = 0
 j = 0
 for i in dev:
  if j != 0:
   if i > dev[j-1]:
    avv1 = avv1 + 1
   else: 
    all1 = all1 + 1
  j = j+1
 if avv1 > all1:
  print dev
  print "Ti stai avvicinando al device"
  print "Muovi in direzione "+`direzione`
  return direzione
 else:
  print dev
  print "Ti stai allontanando dal device, cambio direzione..."
  print "Muovi in direzione "+`(direzione+1)%8`
  return (direzione + 1)%8



 
 
 
 
 

triangolator()
   
  
 
