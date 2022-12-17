import pygame
import random

class Obstacle(pygame.sprite.Sprite):
  def __init__(self, type):
    super().__init__()
    self.image = pygame.image.load("images/" + type + ".png")
    self.rect = self.image.get_rect()

    if type == "arrow" or type == "arrow2":
      self.rect.centerx = random.randint(0, 600)
      self.rect.centery = -50
      self.speed = random.randint(10, 15)
    if type == "bomb":
      self.rect.centerx = random.choice([0, 600])
      if self.rect.centerx == 0: self.direction = "right"
      if self.rect.centerx == 600: self.direction = "left"
      self.rect.centery = 300
      self.xSpeed = random.randint(1, 30)
      self.ySpeed = 0

    self.type = type
  
  def update(self):
    if self.type == "arrow"or self.type == "arrow2":
      self.rect.centery += self.speed
    if self.type == "bomb":
      if self.direction == "right":
        if self.rect.centerx >= 600:
          self.direction = "left"
        else:
          self.rect.centerx += self.xSpeed
      if self.direction == "left":
        if self.rect.centerx <= 0:
          self.direction = "right"
        else:
          self.rect.centerx -= self.xSpeed

      self.rect.centery += self.ySpeed
      self.ySpeed += 0.5
