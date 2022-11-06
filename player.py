import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("images/player.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = 300
    self.rect.centery = 650

    self.speed = 10
    self.maxJump = 1
    self.jump = 0
    self.pressKey_UP = False
    self.resetJump()
  
  def update(self):
    self.keyInput()

    if 1 <= self.jump <= self.maxJump:
      if self.up > 0:
        self.rect.centery -= self.up
        self.up -= 2
      else:
        self.isDown = True

    if self.isDown == True and self.rect.centery < 650:
      self.rect.centery += self.down
      self.down += 2
    elif self.isDown == True and self.rect.centery >= 650:
      self.rect.centery = 650
      self.jump = 0
      self.pressKey_UP = False
      self.resetJump()
  
  def keyInput(self):
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and self.rect.centerx > 0 + self.image.get_width() / 2:
      self.rect.centerx -= self.speed
    if key[pygame.K_RIGHT] and self.rect.centerx < 600 - self.image.get_width() / 2:
      self.rect.centerx += self.speed

    if key[pygame.K_UP] == False:
      self.pressKey_UP = False
    if key[pygame.K_UP] and self.jump < self.maxJump and self.pressKey_UP == False:
      self.pressKey_UP = True
      self.jump += 1
      self.resetJump()
  
  def resetJump(self):
    self.up = 15
    self.down = 0
    self.isDown = False
