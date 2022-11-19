import pygame

class ObstacleController(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.tmr = 0

    self.images = [
      ""
    ]
  
  def update(self):
    self.tmr += 1
