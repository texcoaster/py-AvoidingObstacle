import pygame
import random

class Obstacle(pygame.sprite.Sprite):
  def __init__(self, type):
    super().__init__()

    image = pygame.image.load("images/" + type + ".png")
    self.image = pygame.transform.rotozoom(image, 225, 0.6)

    self.rect = self.image.get_rect()
    self.rect.centerx = random.randint(0, 600)
    self.rect.centery = -50

    self.type = type
    self.speed = 10
  
  def update(self):
    if self.rect.centery >= 650:
      self.kill()
    self.rect.centery += self.speed
