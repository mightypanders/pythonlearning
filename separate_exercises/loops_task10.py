max = 10
for i in range(1, max):
	for j in range(i, max * i, i):
		if (j < 10):
			print(" ", end="")
		print(j, end=" ")
	print()
