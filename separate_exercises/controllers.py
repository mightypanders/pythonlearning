import pygame

x_coord = 10
y_coord = 10
pygame.init()
joystick_count = pygame.joystick.get_count()
done = False
if joystick_count == 0:
	print("No joysticks or controllers found")
else:
	my_joystick = pygame.joystick.Joystick(0)
	my_joystick.init()
	print(my_joystick.get_name())
	print(my_joystick.get_numbuttons())

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.JOYBUTTONDOWN:
			print("joybutton pressed")
