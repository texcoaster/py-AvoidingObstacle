import pygame
import random

from obstacle import *

class GameController:
  def __init__(self):
    super().__init__()
    self.arrowsTmr = 0
    self.bombsTmr = 0
    self.heartTmr = 0
    self.bulletTmr = 0
    self.laserTmr = 0

    self.arrowsRandom = random.randint(10, 30)
    self.bombsRandom = random.randint(180, 240)
    self.heartRandom = random.randint(30, 45)
    self.bulletRandom = random.randint(30, 60)
    self.laserRandom = random.randint(150, 300)

    self.bomb2 = 0

    self.types = [
      "arrow", "arrow2",
      "bomb", "bullet", "fist", "laser",
      "plusHeart", "minusHeart"
    ]
  
  def update(self):
    self.arrowsTmr += 1
    self.bombsTmr += 1
    self.heartTmr += 1
    self.bulletTmr += 1
    self.laserTmr += 1

  def send(self):
    send = []

    if self.bomb2 > 0:
      self.bomb2 -= 1

    if self.bomb2 == 0:

      if self.arrowsTmr % self.arrowsRandom == 0:
        self.arrowsTmr = 0
        self.arrowsRandom = random.randint(10, 30)
        send.append(self.types[random.randint(0, 1)])

      if self.bombsTmr % self.bombsRandom == 0:
        self.bombsTmr = 0
        self.bombsRandom = random.randint(150, 210)
        send.append(self.types[2])

      if self.bulletTmr % self.bulletRandom == 0:
        self.bulletTmr = 0
        self.bulletRandom = random.randint(50, 100)
        send.append(self.types[3])
      
      if self.laserTmr % self.laserRandom == 0:
        self.laserTmr = 0
        self.laserRandom = random.randint(210, 360)
        send.append(self.types[5])

      if self.heartTmr % self.heartRandom == 0:
        self.heartTmr = 0
        self.heartRandom = random.randint(60, 105)
        
        heartNum = random.randint(1, 100)
        if heartNum <= 50:
          send.append(self.types[7])
        else:
          send.append(self.types[6])
    
    return send
