import pygame


class Player(pygame.sprite.Sprite):
	def __init__(self, color, x, y):
		super().__init__()
		self.image = pygame.Surface([50, 50])
		self.image.fill(color)

		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

		self.changex = 0
		self.changey = 0
		self.walls = None

	def changespeed(self, x, y):
		self.changex += x
		self.changey += y

	def update(self):
		self.rect.x += self.changex
		block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
		for block in block_hit_list:
			if self.changex > 0:
				self.rect.right = block.rect.left
			elif self.changex < 0:
				self.rect.left = block.rect.right

		self.rect.y += self.changey
		block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
		for block in block_hit_list:
			if self.changey > 0:
				self.rect.bottom = block.rect.top
			elif self.changey < 0:
				self.rect.top = block.rect.bottom


class Wall(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, color):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


def makesomewalls(color):
	wall_list = []
	wall = Wall(0, 0, 10, 600, color)
	wall_list.append(wall)
	wall = Wall(10, 0, 790, 10, color)
	wall_list.append(wall)
	wall = Wall(10, 200, 100, 10, color)
	wall_list.append(wall)
	return wall_list