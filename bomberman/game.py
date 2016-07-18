# import pygame

from graphics.handler import *
from sounds.handler import *


def main():
	print()
	done = False
	sound = ingamesounds()
	graphics = playersprite(0)
	graphics.print_me()
	while not done:
		sound.bomb_place.play()


if __name__ == '__main__':
	main()
