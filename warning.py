import pygame

class Warning(pygame.sprite.Sprite):
  def __init__(self, img, x, y, tmr):
    super().__init__()
    self.image = pygame.image.load("images/" + img + ".png")
    self.rect = self.image.get_rect()
    self.rect.center = x, y

    self.x = x
    self.y = y
    self.tmr = tmr
    self.type = 0
  
  def update(self):
    if self.tmr < 0:
      self.kill()

    if self.tmr % 10 == 0:
      self.type += 1
    if self.type % 2 == 0:
      self.rect.center = self.x, self.y
    else:
      self.rect.center = self.x, -1000
      
    self.tmr -= 1
