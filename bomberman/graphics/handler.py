import pygame

pygame.init()


class playersprite(pygame.sprite.Sprite):
	def __init__(self, plnumber):
		super().__init__()
		self.playernumer = plnumber
		print()

	def print_me(self):
		print(self.playernumer)
