import pygame
import random

class Obstacle(pygame.sprite.Sprite):
  def __init__(self, type):
    super().__init__()

    self.image = pygame.image.load("images/" + type + ".png")

    self.rect = self.image.get_rect()
    self.rect.centerx = random.randint(0, 600)
    self.rect.centery = -50

    self.type = type
    self.speed = random.randint(10, 15)
  
  def update(self):
    self.rect.centery += self.speed
