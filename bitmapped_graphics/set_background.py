import pygame

def main():
	pygame.init()
	size = [700, 500]
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Background images")
	done = False
	clock = pygame.time.Clock()
	background_image = pygame.image.load("saturn_family1.jpg").convert()
	player_image = pygame.image.load("player.png").convert()
	click_sound = pygame.mixer.Sound("laser5.ogg")
	player_image.set_colorkey([0, 0, 0])

	while not done:
		# Main Loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				print(str(event.key))
			if event.type == pygame.K_RETURN:
				print("user pressed Return")
			if event.type == pygame.MOUSEBUTTONDOWN:

				click_sound.play()
				print("bang")
		screen.blit(background_image, [0, 0])
		player_pos = pygame.mouse.get_pos()
		x = player_pos[0]
		y = player_pos[1]
		screen.blit(player_image, [x, y])
		pygame.display.flip()
		clock.tick(60)


if __name__ == '__main__':
	main()
