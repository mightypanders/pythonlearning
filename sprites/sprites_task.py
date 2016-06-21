import random

import pygame

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
size = [700, 500]
block_number = 50
screen = pygame.display.set_mode(size)
blocklist = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
playersprite = pygame.image.load_extended("player.png").convert()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


class Block(pygame.sprite.Sprite):
	def __init__(self, color, width, height, image):
		super().__init__()
		if image == "":
			self.image = pygame.Surface([width, height])
			self.image.fill(color)
		elif image == playersprite:
			self.image = image
			self.image.set_colorkey(black)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += 1
		if self.rect.y > size[1]:
			self.rect.y = random.randrange(-100, -10)
			self.rect.x = random.randrange(0, size[0])


for i in range(block_number):
	block = Block(black, 20, 15, "")

	block.rect.x = random.randrange(size[0])
	block.rect.y = random.randrange(size[1])

	blocklist.add(block)
	all_sprites.add(block)

player = Block(red, 20, 15, playersprite)
all_sprites.add(player)

done = False
score = 0

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(white)
	pos = pygame.mouse.get_pos()

	player.rect.x = pos[0]
	player.rect.y = pos[1]
	blocklist.update()

	block_hit_list = pygame.sprite.spritecollide(player, blocklist, True)

	for block in block_hit_list:
		score += 1
		print(score)
	all_sprites.draw(screen)
	pygame.display.flip()
	if score >= block_number:
		done = True

	clock.tick(60)
