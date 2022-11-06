import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("images/player.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = 300
    self.rect.centery = 650

    self.speed = 10
    self.jump = 0
    self.up = 20
    self.down = 0
  
  def update(self):
    self.keyInput()

    if self.jump == True:
      if self.up >= 0:
        self.rect.centery -= self.up
        self.up -= 2
      else:
        self.jump = 2

    if self.jump == 2 and self.rect.centery < 650:
      self.rect.centery += self.down
      self.down += 2
    elif self.rect.centery >= 650:
      self.rect.centery = 650
      self.jump = False
      self.up = 20
      self.down = 0
  
  def keyInput(self):
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and self.rect.centerx > 0 + self.image.get_width() / 2:
      self.rect.centerx -= self.speed
    if key[pygame.K_RIGHT] and self.rect.centerx < 600 - self.image.get_width() / 2:
      self.rect.centerx += self.speed
    if key[pygame.K_UP] and self.jump == 0:
      self.jump = 1
