import pygame

class Arrow(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.rect = self.image.get_rect()
    self.rect.topleft = (0, 0)
