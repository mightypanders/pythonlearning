import pygame

black = (0, 0, 0)


class Bullet(pygame.sprite.Sprite):
	def __init__(self):
		super(Bullet,self).__init__()
		self.image = pygame.Surface([8, 18])
		self.image.fill(black)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y -= 6
		if self.rect.y <= 0:
			self.kill()
