import pygame
import random

from obstacle import *

class GameController:
  def __init__(self):
    super().__init__()
    self.arrowsTmr = 0
    self.bombsTmr = 0
    self.heartTmr = 0
    self.arrowsRandom = random.randint(10, 30)
    self.bombsRandom = random.randint(180, 240)
    self.heartRandom = random.randint(30, 45)
    self.bomb2 = 0

    self.types = [
      "arrow", "arrow2",
      "bomb", "bullet", "fist",
      "plusHeart", "minusHeart"
    ]
  
  def update(self):
    self.arrowsTmr += 1
    self.bombsTmr += 1
    self.heartTmr += 1

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

      if self.heartTmr % self.heartRandom == 0:
        self.heartTmr = 0
        self.heartRandom = random.randint(60, 105)
        
        heartNum = random.randint(1, 100)
        if heartNum <= 75:
          send.append(self.types[6])
        else:
          send.append(self.types[5])
    
    return send
