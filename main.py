import pygame

from player import *
from arrow import *


tmr = 0
index = 0

SCREENRECT = pygame.Rect(0, 0, 600, 800)
bg_img = pygame.image.load("images/background.png")

def main():
  global tmr, index

  pygame.init()
  pygame.display.set_caption("AvodingArrow")
  screen = pygame.display.set_mode((600, 800))
  clock = pygame.time.Clock()

  AllGroup = pygame.sprite.RenderUpdates()
  Player.containers = AllGroup

  player = Player()

  background = pygame.image.load("images/background.png")
  screen.blit(background, (0, 0))

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

    pygame.display.update()
    clock.tick(30)


if __name__ == '__main__':
  main()
