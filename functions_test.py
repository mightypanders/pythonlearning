def a(my_list):
	print("function a, list =  ", my_list)
	my_list[0] = 1000
	print("function a, list =  ", my_list)


my_list = [5, 2, 4]

print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)