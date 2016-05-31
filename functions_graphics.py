import pygame
import random
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brown = (140,111,86)
size = [700,500]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

def draw_tree(screen, x,y):
	pygame.draw.rect(screen, brown, [60+x, 400+y, 30, 45])
	pygame.draw.polygon(screen, green, [[150+x, 400+y], [75+x, 250+y], [x, 400+y]])
	pygame.draw.polygon(screen, green, [[140+x, 350+y], [75+x, 230+y], [10+x, 350+y]])


done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(black)
	draw_tree(screen,0,0)
	draw_tree(screen,500,10)
	pygame.display.flip()
	clock.tick(20)


