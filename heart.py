import pygame

class Heart(pygame.sprite.Sprite):
  def __init__(self):
    self.image = pygame.image.load("images/heart.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = 0
    self.rect.centery = 0

    self.playerHeart = 5
  
  def update(self):
    ...
  
  def setPlayerHeart(self, playerHeart):
    self.playerHeart = playerHeart
