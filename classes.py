from enum import Enum
import pygame


def colors():
		black = (0, 0, 0)
		white = (255, 255, 255)
		red = (255, 0, 0)
		green = (0, 255, 0)
		blue = (0, 0, 255)
		return black, white, red, green, blue


class Global:
	size = [700,500]
	screen = pygame.display.set_mode(size)


class Sex(Enum):
	male = 0
	female = 1
	other = 2


class Player:

	def __init__(self, name, sex, maxHP, maxSP, armor):
		self.name = name
		self.sex = sex
		self.max_hit_points = maxHP
		self.current_hit_point = self.max_hit_points
		self.max_speed = maxSP
		self.armor = armor

	def print_me(self):
		print(self.name, self.sex.name, self.current_hit_point, "/",
		      self.max_hit_points, self.max_speed, self.armor)


class Ball():

	def __init__(self,screen,color):
		self.x=0
		self.y=0
		self.x_vector=0
		self.y_vector=0
		self.size=10
		self.color = color
		self.screen = screen

	def move(self):
		self.x+=self.x_vector
		self.y+=self.y_vector

	def draw_self(self):
		pygame.draw.circle(self.screen, self.color,[self.x,self.y],self.size)

def main():
	pygame.init()
	size = Global.size
	screen = Global.screen
	black, white, red, green, blue = colors()
	theBall = Ball(screen,red)
	theBall.draw_self()
	link = Player("Link", Sex.male, 100, 10, 10)
	link.print_me()

if __name__ == '__main__':
	main()