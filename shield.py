import pygame
import random

class Shield(pygame.sprite.Sprite):
  def __init__(self, player):
    super().__init__()
    self.shield_image = pygame.image.load("images/shield.png")
    self.image = self.shield_image
    self.rect = self.image.get_rect()
    self.rect.center = player.rect.centerx, player.rect.centery

    self.player = player
    self.rotate = 0
    self.tmr = 0
    self.x, self.y = 0, 0
  
  def update(self):
    self.tmr += 1
    if self.tmr == 30 * 10:
      self.kill()
    if self.tmr >= 30 * 8:
      self.x, self.y = random.randint(-10, 10), random.randint(-10, 10)
    self.rect.center = self.player.rect.centerx + self.x, self.player.rect.centery + self.y
    self.rotate = (self.rotate + 90) % 360
    self.image = pygame.transform.rotozoom(self.shield_image, self.rotate, 1)
