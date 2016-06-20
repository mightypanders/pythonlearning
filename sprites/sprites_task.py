import pygame

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
size = [700, 500]
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()


class Block(pygame.sprite.Sprite):
	def __init__(self, color, width, heigth, image):
		super().__init__()
		self.image = pygame.Surface([heigth, width])
		self.image.fill(color)


def main():
	block = Block(red, 10, 10, "")
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		block.draw(screen)
		pygame.display.flip()
		clock.tick(30)


if __name__ == '__main__':
	main()
