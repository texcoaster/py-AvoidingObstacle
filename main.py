import pygame
import random

from player import *
from gameController import *
from obstacle import *
from bomb2 import *
from expolusion import *
from heart import *
from ground import *
from plusHeart import *
from minusHeart import *
from shield import *


tmr = 0
index = 0
bomb2Tmr = 0
shieldTmr = 0
isShield = False


def main():
  global tmr, index, bomb2Tmr, shieldTmr, isShield

  pygame.init()
  pygame.display.set_caption("AvodingArrow")
  screen = pygame.display.set_mode((600, 800))
  clock = pygame.time.Clock()

  background = pygame.image.load("images/background.png")
  screen.blit(background, (0, 0))
  pygame.display.flip()

  obstacles = pygame.sprite.Group()
  arrows = pygame.sprite.Group()
  arrow2s = pygame.sprite.Group()
  bombs = pygame.sprite.Group()
  bomb2s = pygame.sprite.Group()
  hearts = pygame.sprite.Group()
  plusHearts = pygame.sprite.Group()
  minusHearts = pygame.sprite.Group()
  expolusions = pygame.sprite.Group()
  bullets = pygame.sprite.Group()
  grounds = pygame.sprite.Group()
  shields = pygame.sprite.Group()
  players = pygame.sprite.Group()
  lasers = pygame.sprite.Group()
  fists = pygame.sprite.Group()
  AllGroup = pygame.sprite.RenderUpdates()

  player = Player()
  gameController = GameController()
  ground = Ground()
  grounds.add(ground)
  for i in range(5):
    heart = Heart(player, i)
    hearts.add(heart)
    AllGroup.add(heart)

  AllGroup.add(player)
  players.add(player)
  AllGroup.add(ground)


  going = True
  while going:
    tmr = tmr + 1
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        going = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
          screen = pygame.display.set_mode((600, 800), pygame.FULLSCREEN)
        if event.key == pygame.K_F2:
          screen = pygame.display.set_mode((600, 800))

    AllGroup.clear(screen, background)

    if bomb2Tmr > 0:
      bomb2Tmr -= 1
    if shieldTmr > 0:
      shieldTmr -= 1

    gameController.update()

    receive = gameController.send()
    for i in range(len(receive)):
      if receive[i] != "plusHeart" and receive[i] != "minusHeart" and receive[i] != "laser":
        obstacle = Obstacle(AllGroup, receive[i])
        AllGroup.add(obstacle)
        obstacles.add(obstacle)
        if obstacle.type == "arrow":
          arrows.add(obstacle)
        if obstacle.type == "arrow2":
          arrow2s.add(obstacle)
        if obstacle.type == "bomb":
          bombs.add(obstacle)
        if obstacle.type == "bullet":
          bullets.add(obstacle)
      else:
        if receive[i] == "plusHeart":
          plusHeart = PlusHeart()
          AllGroup.add(plusHeart)
          plusHearts.add(plusHeart)
        if receive[i] == "minusHeart":
          minusHeart = MinusHeart()
          AllGroup.add(minusHeart)
          minusHearts.add(minusHeart)
        if receive[i] == "laser":
          x = random.randint(0, 600)
          for i in range(5):
            obstacle = Obstacle(AllGroup, "laser", i, x)
            AllGroup.add(obstacle)
            obstacles.add(obstacle)
            lasers.add(obstacle)

    key = pygame.key.get_pressed()
    if key[pygame.K_b] and bomb2Tmr == 0:
      bomb2Tmr = 30 * 30
      bomb = Bomb2()
      AllGroup.add(bomb)
      bomb2s.add(bomb)
    if key[pygame.K_n] and shieldTmr == 0:
      shieldTmr = 30 * 20
      isShield = True
      shield = Shield(player)
      AllGroup.add(shield)
      shields.add(shield)

    AllGroup.update()

    if not len(players.sprites()) == 0:
      if pygame.sprite.spritecollide(player, arrows, True):
        player.heart -= 1
        player.hurt()
      if pygame.sprite.spritecollide(player, arrow2s, True):
        player.heart -= 2
        player.hurt()
      if pygame.sprite.spritecollide(player, bombs, False):
        player.heart -= 3
        player.hurt()
        expolusion = Expolusion(0, bombs.sprites()[0].rect.centerx, bombs.sprites()[0].rect.centery)
        AllGroup.add(expolusion)
        expolusions.add(expolusion)
        bombs.sprites()[0].kill()
      if pygame.sprite.spritecollide(player, bullets, True):
        player.heart -= 1
        player.hurt()
      if pygame.sprite.spritecollide(player, lasers, True):
        player.heart -= 1
        player.hurt()
      if pygame.sprite.spritecollide(player, plusHearts, True):
        player.health()
        if player.heart < 5:
          player.heart += 1
      if pygame.sprite.spritecollide(player, minusHearts, True):
        player.heart -= 1
        player.hurt()

    if pygame.sprite.spritecollide(ground, bomb2s, True):
      gameController.bomb2 = 45
      AllGroup.add(Expolusion(1, 300, 435))
      for i in range(len(obstacles.sprites())):
        obstacles.sprites()[0].kill()
      for i in range(len(arrows.sprites())):
        arrows.sprites()[0].kill() 
      for i in range(len(arrow2s.sprites())):
        arrow2s.sprites()[0].kill()
      for i in range(len(bombs.sprites())):
        bombs.sprites()[0].kill()
      for i in range(len(plusHearts.sprites())):
        plusHearts.sprites()[0].kill()
      for i in range(len(minusHearts.sprites())):
        minusHearts.sprites()[0].kill()
      for i in range(len(bullets.sprites())):
        bullets.sprites()[0].kill()
      for i in range(len(lasers.sprites())):
        lasers.sprites()[0].kill()

    if pygame.sprite.spritecollide(ground, bombs, False):
      expolusion = Expolusion(0, bombs.sprites()[0].rect.centerx, bombs.sprites()[0].rect.centery)
      AllGroup.add(expolusion)
      expolusions.add(expolusion)
      bombs.sprites()[0].kill()
    for i in range(len(plusHearts.sprites())):
      if pygame.sprite.spritecollide(plusHearts.sprites()[i], grounds, False):
        plusHearts.sprites()[i].dropGround = True
    for i in range(len(minusHearts.sprites())):
      if pygame.sprite.spritecollide(minusHearts.sprites()[i], grounds, False):
        minusHearts.sprites()[i].dropGround = True

    if not len(shields.sprites()) == 0:
      pygame.sprite.spritecollide(shield, obstacles, True)
    pygame.sprite.groupcollide(expolusions, plusHearts, False, True)
    pygame.sprite.groupcollide(expolusions, minusHearts, False, True)
    pygame.sprite.spritecollide(ground, obstacles, True)

    dirty = AllGroup.draw(screen)


    pygame.display.update(dirty)
    clock.tick(30)


if __name__ == '__main__':
  main()
