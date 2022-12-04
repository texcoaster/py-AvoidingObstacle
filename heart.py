import pygame

class Heart(pygame.sprite.Sprite):
  def __init__(self, player, number):
    super().__init__()
    self.image = pygame.image.load("images/heart.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = 30 + number * 55
    self.rect.centery = 30

    self.player = player
    self.number = number + 1
  
  def update(self):
    if self.player.heart < self.number:
      self.rect.centery = -30
    else:
      self.rect.centery = 30
