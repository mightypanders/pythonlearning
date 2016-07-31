import pygame

pygame.init()


class ingamesounds:
	def __init__(self):
		self.bomb_place = pygame.mixer.Sound("sounds/bomb_place.wav")
		self.bomb_explode = pygame.mixer.Sound("sounds/explosion_1.wav")
		# self.walk_step = pygame.mixer.Sound("")
		self.walk_bump = pygame.mixer.Sound("sounds/walk_bump.wav")
		self.player_die = pygame.mixer.Sound("sounds/player_die.wav")
		self.item_pick = pygame.mixer.Sound("sounds/item_pickup.wav")

	# self.bad_item_pick = pygame.mixer.Sound("")
	# self.bomb_throw = pygame.mixer.Sound("")
	# self.bomb_pick_up = pygame.mixer.Sound("")


class menusounds:
	def __init__(self):
		self.menu_highlight = pygame.mixer.Sound("sounds/select_menu_item.wav")
		self.menu_pick = pygame.mixer.Sound("sounds/confirm.wav")

		# self.menu_invalid_pick = pygame.mixer.Sound("")
		# self.menu_scroll = pygame.mixer.Sound("")
		self.menu_start_game = pygame.mixer.Sound("sounds/start_game.wav")
