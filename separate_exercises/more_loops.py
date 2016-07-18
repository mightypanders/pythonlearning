x = 10
i = j = k = 0
# for i in range(0,x):
# 	print("*", end=" ")
# print("")
# for j in range(0, int(x/2)):
# 	print("*", end=" ")
# print("")
# for k in range(0,2*x):
# 	print("*", end=" ")
max = 11
for i in range(max):
	for k in range(i):
		print(" ", end=" ")
	for j in range(max - (i + 1)):
		print(j, end=" ")
	print()
