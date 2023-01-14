import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("images/player.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = 300
    self.rect.centery = 650

    self.heart = 5
    self.speed = 10
    self.maxJump = 1
    self.jump = 0
    self.pressKey_UP = False
    self.resetJump()

    self.isHurt = False
    self.hurtTmr = 0
  
  def update(self):
    self.keyInput()

    if self.isHurt:
      self.hurtTmr += 1
    if self.hurtTmr == 2:
      self.hurtTmr = 0
      self.isHurt = False
      self.rect.centerx += 5
      self.rect.centery += 5
      self.image = pygame.image.load("images/player.png")

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
    
    if self.heart <= 0:
      self.kill()
  
  def keyInput(self):
    key = pygame.key.get_pressed()

    if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.rect.centerx > 0 + self.image.get_width() / 2:
      self.rect.centerx -= self.speed
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.rect.centerx < 600 - self.image.get_width() / 2:
      self.rect.centerx += self.speed

    if key[pygame.K_UP] == False or key[pygame.K_w] == False:
      self.pressKey_UP = False
    if (key[pygame.K_UP] or key[pygame.K_w]) and self.jump < self.maxJump and self.pressKey_UP == False:
      self.pressKey_UP = True
      self.jump += 1
      self.resetJump()
  
  def hurt(self):
    self.hurtTmr = 0
    self.isHurt = True
    self.image = pygame.image.load("images/player2.png")
    self.rect.centerx -= 5
    self.rect.centery -= 5

  def health(self):
    self.hurtTmr = 0
    self.isHurt = True
    self.image = pygame.image.load("images/player3.png")

  def resetJump(self):
    self.up = 18
    self.down = 0
    self.isDown = False
