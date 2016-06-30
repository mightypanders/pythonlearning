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
bulletlist = pygame.sprite.Group()
playersprite = pygame.image.load_extended("player.png").convert()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


class Block(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()

	def reset(self):
		self.rect.y = random.randrange(-100, -10)
		self.rect.x = random.randrange(0, size[0])

	def update(self):
		self.rect.y += 1
		if self.rect.y > size[1]:
			self.reset()


class Bullet(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([4, 10])
		self.image.fill(black)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y -= 3


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = playersprite
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.x = pygame.mouse.get_pos()[0]
		self.rect.y = pygame.mouse.get_pos()[1]


for i in range(block_number):
	block = Block(black, 20, 15)
	block.rect.x = random.randrange(size[0])
	block.rect.y = random.randrange(size[1])
	blocklist.add(block)
	all_sprites.add(block)

player = Player()
all_sprites.add(player)

done = False
score = 0

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			bulletleft = Bullet()
			bulletright = Bullet()
			bulletright.rect.x = player.rect.right
			bulletright.rect.y = player.rect.y
			bulletleft.rect.x = player.rect.x
			bulletleft.rect.y = player.rect.y
			all_sprites.add(bulletright)
			all_sprites.add(bulletleft)
			bulletlist.add(bulletright)
			bulletlist.add(bulletleft)

	screen.fill(white)
	all_sprites.update()
	for bullet in bulletlist:
		block_hit_list = pygame.sprite.spritecollide(bullet, blocklist, False)
		for block in block_hit_list:
			bulletlist.remove(bullet)
			all_sprites.remove(bullet)
			score += 1
			print(score)
			block.reset()

	all_sprites.draw(screen)
	pygame.display.flip()

	clock.tick(60)
