from datetime import datetime

import pygame

wall_width = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 0, 0)


class Player(pygame.sprite.Sprite):
	def __init__(self, color, x, y):
		super().__init__()
		self.image = pygame.Surface([20, 20])
		self.image.fill(color)

		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

		self.changex = 0
		self.changey = 0
		self.walls = None

		self.bomb_color = WHITE
		self.bombs = pygame.sprite.Group()
		self.bomb_max = 1
		self.bombs_placed = 0

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

	def putbomb(self):
		if (self.bomb_max >= self.bombs_placed):
			print("bombe hier")
			newbomb = Bomb(self.bomb_color, self)
			# print(newbomb.rect.x, " ", newbomb.rect.y)
			self.bombs_placed += 1
			self.bombs.add(newbomb)
			print(self.bombs)
			return self.bombs
		else:
			print("keine bombe")
			return self.bombs

	def bomb_exploded(self):
		self.bombs_placed -= 1


class Bomb(pygame.sprite.Sprite):
	def __init__(self, color, player):
		super().__init__()
		self.image = pygame.Surface([10, 10])
		self.image.fill([255, 255, 255])
		# self.image.set_colorkey([255,255,255])
		pygame.draw.ellipse(self.image, color, [0, 0, 10, 10], 2)
		self.player = player
		self.rect = self.image.get_rect()
		self.rect.x = player.rect.x
		self.rect.y = player.rect.y
		self.timeplaced = datetime.now()

	def update(self):

		delta = (datetime.now() - self.timeplaced).seconds
		if delta > 3:
			self.kill()
			self.player.bomb_exploded()


class Wall(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, color):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


