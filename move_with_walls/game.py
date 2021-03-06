import pygame

import colors
import setup
from entity import Player

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

CLOCK = pygame.time.Clock()
DONE = False

all_sprites = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

walls = setup.makeouterwalls(colors.BLOCK, SCREEN_SIZE)
blocks = setup.makeinnerblocks(colors.BLOCK, SCREEN_SIZE, 5)

player = Player(colors.PLAYER, 20, 20)
player.walls = wall_list

wall_list.add(walls, blocks)
all_sprites.add(walls, blocks, player)

while not DONE:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			DONE = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.changespeed(-3, 0)
			elif event.key == pygame.K_RIGHT:
				player.changespeed(3, 0)
			elif event.key == pygame.K_UP:
				player.changespeed(0, -3)
			elif event.key == pygame.K_DOWN:
				player.changespeed(0, 3)
			if event.key == pygame.K_SPACE:
				all_sprites.add(player.putbomb())

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.changespeed(3, 0)
			elif event.key == pygame.K_RIGHT:
				player.changespeed(-3, 0)
			elif event.key == pygame.K_UP:
				player.changespeed(0, 3)
			elif event.key == pygame.K_DOWN:
				player.changespeed(0, -3)

	all_sprites.update()

	SCREEN.fill(colors.BACKGROUND)
	all_sprites.draw(SCREEN)
	pygame.display.flip()

	CLOCK.tick(60)
