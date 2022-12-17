import pygame
import random

from obstacle import *

class ObstacleController:
  def __init__(self):
    super().__init__()
    self.arrowsTmr = 0
    self.bombsTmr = 0
    self.arrowsRandom = random.randint(10, 30)
    self.bombsRandom = random.randint(180, 240)
    self.bomb2 = 0

    self.types = [
      "arrow", "arrow2",
      "bomb", "bullet", "fist"
    ]
  
  def update(self):
    self.arrowsTmr += 1
    self.bombsTmr += 1

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
        self.bombsRandom = random.randint(180, 240)
        send.append(self.types[2])
    
    return send
