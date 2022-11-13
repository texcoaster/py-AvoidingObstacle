import pygame

class Obstacle(pygame.sprite.Sprite):
  def __init__(self, type):
    super().__init__()

    self.image = pygame.image.load("images/arrow.png")

    self.rect = self.image.get_rect()
    self.rect.topleft = (0, 0)
