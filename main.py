import pygame

from player import *
from obstacleController import *
from obstacle import *
from heart import *
from ground import *


tmr = 0
index = 0

bg_img = pygame.image.load("images/background.png")


def main():
  global tmr, index

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
  hearts = pygame.sprite.Group()
  AllGroup = pygame.sprite.RenderUpdates()

  player = Player()
  obstacleController = ObstacleController()
  ground = Ground()
  for i in range(5):
    heart = Heart(player, i)
    hearts.add(heart)
    AllGroup.add(heart)

  AllGroup.add(player)
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

    obstacleController.update()
    receive = obstacleController.send()
    for i in range(len(receive)):
      obstacle = Obstacle(receive[i])
      AllGroup.add(obstacle)
      obstacles.add(obstacle)
      if obstacle.type == "arrow":
        arrows.add(obstacle)
      if obstacle.type == "arrow2":
        arrow2s.add(obstacle)

    AllGroup.update()
    dirty = AllGroup.draw(screen)

    pygame.sprite.spritecollide(ground, obstacles, True)
    if pygame.sprite.spritecollide(player, arrows, True):
      player.heart -= 1
    if pygame.sprite.spritecollide(player, arrow2s, True):
      player.heart -= 2


    pygame.display.update(dirty)
    clock.tick(30)


if __name__ == '__main__':
  main()
