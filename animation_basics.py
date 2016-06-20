import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
size = [700, 500]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("Hack", 25, False, False)
clock = pygame.time.Clock()
pos_x = 50
pos_x_change = 5
pos_y = 50
pos_y_change = 5
len_x = 50
len_y = 50

done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(black)
	pygame.draw.rect(screen, white, [pos_x, pos_y, len_x, len_y])
	if pos_y > (size[1] - len_y) or pos_y <= 0:
		pos_y_change *= (-1)
	if pos_x > (size[0] - len_x) or pos_x <= 0:
		pos_x_change *= (-1)
	pos_x += pos_x_change
	pos_y += pos_y_change

	pygame.display.flip()
	clock.tick(30)
