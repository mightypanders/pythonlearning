def volume_sphere(radius):
	pi = 3.141592653589
	volume = (4 / 3) * pi * radius ** 3
	print("The volume is ", volume)


def volume_cylinder(radius, height):
	pi = 3.141592653589
	volume = pi * radius ** 2 * height
	print("The volume is ", volume)


if (input("Sphere or Cylinder") == "S"):
	radius = int(input("Radius eingeben "))
	volume_sphere(radius)
else:
	radius = int(input("Radius eingeben "))
	height = int(input("Höhe eingeben "))
	volume_cylinder(radius, height)
