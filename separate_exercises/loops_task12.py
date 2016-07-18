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
max = 11

for m in range(1, max):
	print(" ", end=" ")
	for n in range(m):
		print(" ", end=" ")
	for p in range(1, max - (m + 1)):
		print(p, end=" ")
	for s in range(max - (m + 3), 0, -1):
		print(s, end=" ")
	print()
