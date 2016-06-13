import pygame
import random
import math
def colors():
	black = (0, 0, 0)
	white = (255, 255, 255)
	red = (255, 0, 0)
	green = (0, 255, 0)
	blue = (0, 0, 255)
	return black, white, red, green, blue

def main():
	pygame.init()
	black, white, red, green, blue = colors()

	size = [700, 500]
	screen = pygame.display.set_mode(size)
	PI=3.141592652

	font = pygame.font.SysFont('Hack', 25, False, False)

	pygame.display.set_caption("My cool Game")

	done = False

	clock = pygame.time.Clock()

	while not done:
		# Main Loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				print(str(event.key))
			if event.type == pygame.K_RETURN:
				print("user pressed Return")
		# Logic
		# /Logic
		# Draw
		screen.fill(white)
		pygame.draw.rect(screen,red,[100,100,100,100],2)
		pygame.draw.ellipse(screen,green,[100,100,100,100],2)

		pygame.draw.rect(screen,black,[200,200,200,200],2)
		pygame.draw.arc(screen,green,[200,200,200,200], PI/2 ,PI, 2)
		pygame.draw.arc(screen,red,[200,200,200,200], 0, PI/2, 2)
		pygame.draw.arc(screen,blue,[200,200,200,200], 3*PI/2, 2*PI,2)
		pygame.draw.arc(screen,black,[200,200,200,200], PI, 3*PI/2, 2)

		pygame.draw.polygon(screen, blue, [[400,200], [200,100], [200,200]],5)

		text = font.render("My Text", True, black)
		pygame.draw.line(screen, green, [100,100], [200,200],5)
		pygame.draw.line(screen, blue, [200,100], [100, 200], 5)

		y_offset=0
		for y_offset in range (0,100,10):
			pygame.draw.line(screen,black,[0,10+y_offset],[100,110+y_offset],10)

		for i in range(200):
			rad_x = i / 20
			rad_y = i / 6

			x = int(75 * math.sin(rad_x)) + 200
			y = int(75 * math.cos(rad_y)) + 200

			pygame.draw.line(screen, black, [100 + x, 100 + y], [102 + x, 100 + y], 21)

		screen.blit(text, [300, 300])
		pygame.display.flip()
		# /Draw
		clock.tick(20)
	pygame.quit()

if __name__ == '__main__':
	main()



