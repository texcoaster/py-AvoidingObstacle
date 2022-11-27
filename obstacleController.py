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
  
  def update(self):
    self.tmr += 1
  
  def send(self):
    send = []

    if self.tmr % self.random == 0:
      self.random = random.randint(20, 40)
      send.append(self.images[random.randint(0, 1)])
    
    return send
