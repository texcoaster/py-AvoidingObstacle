import pygame
import random

class PlusHeart(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("images/plusHeart.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = random.randint(0, 600)
    self.rect.centery = -100
    
    self.tmr = 150
    self.dropGround = False

  def update(self):
    if self.dropGround == True:
      if self.tmr <= 0:
        self.kill()
      else:
        self.tmr -= 1
    else:
      self.rect.centery += 15
