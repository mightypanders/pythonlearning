import entity

wall_width = 10


def makeouterwalls(color, size):
	wall_list = []

	wall = entity.Wall(0, 0, wall_width, size[1],color)
	wall_list.append(wall)

	wall = entity.Wall(0, 0, size[0], wall_width,color)
	wall_list.append(wall)

	wall = entity.Wall(size[0] - wall_width, 0, wall_width, size[1],color)
	wall_list.append(wall)

	wall = entity.Wall(0, size[1] - wall_width, size[0], wall_width,color)
	wall_list.append(wall)

	return wall_list


def makeinnerblocks(color, screensize, count):
	wall_list = []

	cHor = (screensize[0] - (wall_width * 2)) / ((count * 2) + 1)  # berechne wie
	# breit ein "block" sein kann
	cVert = (screensize[1] - (wall_width * 2)) / ((count * 2) + 1)  # berechne wie
	# hoch ein "block" sein kann

	for j in range((count * 2)):
		if j % 2 == 1:  # jede zweite Reihe wird gefuellt (y-Achse)
			for i in range((count * 2)):
				if i % 2 == 1:  # jede zweite spalte wird gefuellt (x-Achse)
					wall = entity.Wall(
							wall_width + i * cHor,
		                    wall_width + j * cVert,
	                        cHor,
		                    cVert,color
					)
					wall_list.append(wall)
	return wall_list
