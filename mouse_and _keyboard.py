import pygame

black = [0, 0, 0]
white = [255, 255, 255]


def draw_stickfigure(screen, x, y):
	# HEAD
	pygame.draw.ellipse(screen, white, [x, y, 10, 10], 0)
	# LEGS
	pygame.draw.line(screen, white, [x + 4, y + 17], [x + 9, y + 27], 2)
	pygame.draw.line(screen, white, [x + 4, y + 17], [x + 1, y + 27], 2)
	# BODY
	pygame.draw.line(screen, white, [x + 4, y + 17], [x + 4, y + 7], 2)
	# ARMS
	pygame.draw.line(screen, white, [x + 4, y + 7], [x + 8, y + 17], 2)
	pygame.draw.line(screen, white, [x + 4, y + 7], [x, y + 17], 2)


def draw_sticks(screen, sticklist):
	for x in range(len(sticklist)):
		coords = sticklist[x]
		draw_stickfigure(screen, coords[0], coords[1])


def main():
	pygame.init()
	size = [700, 500]
	screen = pygame.display.set_mode(size)
	done = False
	clock = pygame.time.Clock()
	pygame.mouse.set_visible(False)
	sticklist = []
	y_speed = 0
	x_speed = 0
	x_coord = 100
	y_coord = 100
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					coords = pygame.mouse.get_pos()
					sticklist.append(coords)
				if event.button == 3:
					sticklist.clear()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_speed = -3
				elif event.key == pygame.K_RIGHT:
					x_speed = 3
				elif event.key == pygame.K_UP:
					y_speed = -3
				elif event.key == pygame.K_DOWN:
					y_speed = 3
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_speed = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_speed = 0
		screen.fill(black)
		pos = pygame.mouse.get_pos()
		draw_sticks(screen, sticklist)
		draw_stickfigure(screen, pos[0], pos[1])
		x_coord+=x_speed
		y_coord+=y_speed
		draw_stickfigure(screen, x_coord,y_coord)
		pygame.display.flip()
		clock.tick(60)


if __name__ == '__main__':
	main()
