import pygame
from constants import *
from colors import *
pygame.init()

class GameMenu():
	def __init__(self,items,bg_color=(0,0,0)):
		self.screen = SCREEN
		self.bg_color = bg_color
		self.clock = CLOCK

		self.font = MENU_FONT
		self.font_color = RED

		self.labels = []

		for item in items:
			label = self.font.render(item,1,self.font_color)
			self.labels.append(label)
	def run(self):
		mainloop = True

		while mainloop:
			self.clock.tick(50)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					mainloop = False

				self.screen.fill(self.bg_color)
				for index,label in enumerate(self.labels):
					self.screen.blit(label,((index+1)*100,(index+1)*100))
				pygame.display.flip()

if __name__ =="__main__":
	menu_items = ("Start","Quit")
	gm = GameMenu(menu_items)
	gm.run()