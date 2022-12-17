import pygame

class Bomb2(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("images/bomb2.png")
    self.rect = self.image.get_rect()

    self.rect.centerx = 300
    self.rect.centery = -50

  def update(self):
    self.rect.centery += 20
