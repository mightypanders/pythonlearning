import pygame

import move_with_walls.entity

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 0, 0)
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
pygame.init()
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
CLOCK = pygame.time.Clock()
DONE = False
all_sprites = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
walls = move_with_walls.entity.makesomewalls(BLUE, SCREEN_SIZE)
walls.append(move_with_walls.entity.makesomeblocks(WHITE, SCREEN_SIZE, 8))

for wall in walls:
	wall_list.add(wall)
	all_sprites.add(wall)

player = move_with_walls.entity.Player(RED, 20, 20)
player.walls = wall_list

all_sprites.add(player)

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
	SCREEN.fill(BLACK)
	all_sprites.draw(SCREEN)
	pygame.display.flip()
	CLOCK.tick(60)
