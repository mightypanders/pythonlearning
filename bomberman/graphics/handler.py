import pygame

pygame.init()


class playersprite(int):
	def __init__(self,plnumber):
		self.playernumer = plnumber
		print()
	def print_me(self):
		print(self.playernumer)