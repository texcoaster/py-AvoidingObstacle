import pygame

class Expolusion(pygame.sprite.Sprite):
  def __init__(self, num, x, y):
    super().__init__()
    if num == 0: self.image = pygame.image.load("images/expolusion.png")
    else: self.image = pygame.image.load("images/expolusion2.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y

    self.tmr = 0
  
  def update(self):
    self.tmr += 1
    if self.tmr == 45:
      self.kill()
