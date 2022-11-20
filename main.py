import pygame

from player import *
from obstacleController import *
from obstacle import *


tmr = 0
index = 0

bg_img = pygame.image.load("images/background.png")

def main():
  global tmr, index

  pygame.init()
  pygame.display.set_caption("AvodingArrow")
  screen = pygame.display.set_mode((600, 800))
  clock = pygame.time.Clock()

  player = Player()

  arrows = pygame.sprite.Group()
  arrow2s = pygame.sprite.Group()
  AllGroup = pygame.sprite.RenderUpdates()
  AllGroup.add(player)

  obstacleController = ObstacleController()

  background = pygame.image.load("images/background.png")
  screen.blit(background, (0, 0))
  pygame.display.flip()

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
    AllGroup.update()

    receive = obstacleController.send()
    if receive != None:
      obstacle = Obstacle(receive)
      AllGroup.add(obstacle)
      if obstacle.type == "arrow":
        arrows.add(obstacle)
      if obstacle.type == "arrow2":
        arrow2s.add(obstacle)

    if pygame.sprite.spritecollide(player, arrows, True):
      player.heart -= 1
    if pygame.sprite.spritecollide(player, arrow2s, True):
      player.heart -= 2

    dirty = AllGroup.draw(screen)


    pygame.display.update(dirty)
    clock.tick(30)


if __name__ == '__main__':
  main()
