import pygame

black = (0, 0, 0)
red = (255, 0, 0)


class Bullet(pygame.sprite.Sprite):
	def __init__(self):
		super(Bullet, self).__init__()
		self.image = pygame.Surface([8, 18])
		self.image.fill(black)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y -= 6
		if self.rect.y <= 0:
			self.kill()


class SuperBullet(Bullet):
	def __init__(self):
		super(SuperBullet, self).__init__()
		self.image = pygame.Surface([20, 30])
		self.image.fill(red)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y -= 10
		if self.rect.y <= 0:
			self.kill()


class Player(pygame.sprite.Sprite):
	def __init__(self, playersprite):
		super(Player, self).__init__()
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
		bulletleft = Bullet()
		bulletright = Bullet()
		bulletright.rect.x = self.rect.right
		bulletright.rect.y = self.rect.centery
		bulletleft.rect.x = self.rect.x
		bulletleft.rect.y = self.rect.centery
		bulletsshot.append(bulletright)
		bulletsshot.append(bulletleft)
		return bulletsshot

	def shotLvlTwo(self):
		bulletsshot = []
		bulletmiddle = Bullet()
		bulletmiddle.rect.x = self.rect.centerx
		bulletmiddle.rect.y = self.rect.y
		bulletsshot.append(bulletmiddle)
		return bulletsshot

	def shotLvlThree(self):
		bulletsshot = []
		bulletleft = SuperBullet()
		bulletright = SuperBullet()
		bulletmiddle = SuperBullet()
		bulletright.rect.x = self.rect.right
		bulletright.rect.y = self.rect.centery
		bulletleft.rect.x = self.rect.x
		bulletleft.rect.y = self.rect.centery
		bulletmiddle.rect.x = self.rect.centerx
		bulletmiddle.rect.y = self.rect.y
		bulletsshot.append(bulletright)
		bulletsshot.append(bulletleft)
		bulletsshot.append(bulletmiddle)
		return bulletsshot

	def shoot(self, allsprites, bulletlist):
		bulletsshot = []
		if self.bulletlevel == 1:
			bulletsshot = self.shotLvlOne()
		if self.bulletlevel == 2:
			bulletsshot = self.shotLvlOne()
			bulletsshot.append(self.shotLvlTwo())
		if self.bulletlevel == 3:
			bulletsshot = self.shotLvlThree()
		for bullet in bulletsshot:
			allsprites.add(bullet)
			bulletlist.add(bullet)
