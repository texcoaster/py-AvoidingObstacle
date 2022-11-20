import pygame
import random

from obstacle import *

class ObstacleController():
  def __init__(self):
    super().__init__()
    self.tmr = 0
    self.random = random.randint(20, 40)

    self.images = [
      "arrow", "arrow2",
      "bomb", "bomb2",
      "bullet",
      "fist",
    ]
  
  def send(self):
    self.tmr += 1

    if self.tmr % self.random == 0:
      self.random = random.randint(20, 40)
      return self.images[random.randint(0, 1)]
    else:
      return None
