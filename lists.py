# my_list = ["a","b","c","d"]
# print(my_list)
# my_list.append("e")
# print(my_list)

# second_list = []
# for i in range(5):
# 	second_list.append(int(input ("Enter int: ")))
# print(second_list)

third_list = [1,2,3,4,4,5,6,6,7,8,9]
list_total =0

for i in range(len(third_list)):
	list_total += third_list[i]

print(list_total)
print(len(third_list))
print(third_list[5:])