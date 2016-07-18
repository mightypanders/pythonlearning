leer = ""
for i in range(1, 10):
	for a in range(20 - (2 * i)):
		leer += " "
	print(leer, end="")
	for j in range(1, i):
		print(j, end=" ")
	for k in range(i, 0, -1):
		print(k, end=" ")
	print()
	leer = ""
