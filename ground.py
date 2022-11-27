import pygame

class Ground(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("images/ground.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = 300
    self.rect.centery = 740
