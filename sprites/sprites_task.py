import random
from Bullet import Entity
import pygame

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
size = [700, 500]
block_number = 15
screen = pygame.display.set_mode(size)
blocklist = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
bulletlist = pygame.sprite.Group()
playersprite = pygame.image.load_extended("player.png").convert()
clock = pygame.time.Clock()
done = False
score = 0
gamespeed = 1
pygame.mouse.set_visible(False)


class Block(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super(Block,self).__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()

	def reset(self):
		self.rect.y = random.randrange(-100, -10)
		self.rect.x = random.randrange(0, size[0])

	def update(self):
		self.rect.y += gamespeed
		if self.rect.y > size[1]:
			self.reset()




class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player,self).__init__()
		self.image = playersprite
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.bulletlevel = 1

	def update(self):
		self.rect.x = pygame.mouse.get_pos()[0]
		self.rect.y = pygame.mouse.get_pos()[1]

	def destroy(self):
		print("I died")

	def shotLvlOne(self):
		bulletsshot = []
		bulletleft = Entity.Bullet()
		bulletright = Entity.Bullet()
		bulletright.rect.x = player.rect.right
		bulletright.rect.y = player.rect.centery
		bulletleft.rect.x = player.rect.x
		bulletleft.rect.y = player.rect.centery
		bulletsshot.append(bulletright)
		bulletsshot.append(bulletleft)
		return bulletsshot

	def shotLvlTwo(self):
		bulletsshot = []
		bulletmiddle = Entity.Bullet()
		bulletmiddle.rect.x = player.rect.centerx
		bulletmiddle.rect.y = player.rect.y
		bulletsshot.append(bulletmiddle)
		return bulletsshot

	def shoot(self, allsprites, bulletlist):
		bulletsshot = []
		if self.bulletlevel == 1:
			bulletsshot = self.shotLvlOne()
		if self.bulletlevel == 2:
			bulletsshot = self.shotLvlOne()
			bulletsshot.append(self.shotLvlTwo())
		for bullet in bulletsshot:
			allsprites.add(bullet)
			bulletlist.add(bullet)


class Scoreboard(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.font = pygame.font.SysFont("Hack", 25, True, False)
		self.score = 0
		self.color = red

	def update(self):
		self.score += 1


for i in range(block_number):
	block = Block(black, 20, 15)
	block.rect.x = random.randrange(size[0])
	block.rect.y = random.randrange(size[1])
	blocklist.add(block)
	all_sprites.add(block)

player = Player()
all_sprites.add(player)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			player.shoot(all_sprites, bulletlist)
			print(player.bulletlevel)
	screen.fill(white)
	blocklist.update()
	all_sprites.update()
	for bullet in bulletlist:
		block_hit_list = pygame.sprite.spritecollide(bullet, blocklist, False)
		for block in block_hit_list:
			bulletlist.remove(bullet)
			all_sprites.remove(bullet)
			score += 1
			print(score)
			block.reset()
	gamespeed = (score / 30) + 1

	block_hit_list = pygame.sprite.spritecollide(player, blocklist, False)
	if len(block_hit_list) > 0:
		player.destroy()
		for block in block_hit_list:
			block.reset()
	if score >= 20:
		player.bulletlevel=2
	all_sprites.draw(screen)
	pygame.display.flip()

	clock.tick(60)
