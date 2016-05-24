import pygame
import random
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
size = [700,500]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
snow_list=[]
done = False
for i in range(500):
		x = random.randrange(0,size[0])
		y = random.randrange(0,size[1])
		snow_list.append([x,y])
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(black)
	for i in range(len(snow_list)):

		pygame.draw.circle(screen,white,snow_list[i],2)
		snow_list[i][1] += 1

	pygame.display.flip()
	clock.tick(20)