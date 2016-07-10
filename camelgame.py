import random


def print_instructions():
	print("Welcome to Camel!")
	print(
			"You have stolen a camel to make your way across the great Mobi "
			"desert.")
	print(
			"The natives want their camel back and are chasing you down! "
			"Survive "
			"your")
	print("desert trek and out run the natives.")


def show_options():
	print("\n")
	print("A. Drink from your canteen.")
	print("B. Ahead moderate speed.")
	print("C. Ahead full speed.")
	print("D. Stop for the night.")
	print("E. Status check.")
	print("Q. Quit.")


def show_status(miles, drinks, natives):
	print("Miles traveled: ", miles)
	print("Drinks left in canteen: ", drinks)
	print("The natives are ", miles - natives, " miles behind you")
	input("Press Enter to continue")


def init_values():
	miles = 0
	thirst = 0
	tired = 0
	natives = -20
	drinks = 5
	return miles, thirst, tired, natives, drinks


def travel(speed, miles, thirst, camel, natives):
	new_miles, new_camel, new_thirst = 0, 0, 0
	if speed == 1:
		new_miles = miles + random.randrange(10, 21)
		new_thirst = thirst + random.randrange(1, 3)
		new_camel = camel + random.randrange(1, 4)
	elif speed == 2:
		new_miles = miles + random.randrange(5, 13)
		new_thirst = thirst + 1
		new_camel = camel + 1
	print("You traveled ", new_miles - miles, " miles.")
	natives += random.randrange(7, 15)
	return new_miles, new_thirst, new_camel, natives


def rest(camel, natives, thirst):
	if camel != 0:
		camel = 0
	natives += random.randrange(7, 14)
	if thirst > 0 and thirst < 7:
		thirst = 0
	print("The rest was very pleasant for your camel. It is happy now!")
	return camel, natives, thirst


def drink_canteen(canteen, thirst):
	if canteen > 0:
		canteen -= 1
		thirst = 0
	else:
		print("Your canteen is empty. Better hurry!")
	return canteen, thirst


def check_thirst(thirst, done):
	if not done:
		if thirst >= 4 and thirst < 8:
			print("You are thirsty!")

		elif thirst >= 8:
			print("You died of thirst!")
			done = True
	return done


def check_camel_tired(camel, done):
	if not done:
		if camel >= 5 and camel < 8:
			print("Your camel is getting tired.")
		elif camel >= 8:
			print("Your camel died of exhaustion!")
			done = True
	return done


def check_natives(natives, miles, Done):
	if not Done:
		if (miles - natives) <= 0:
			print("The natives have caught you! You are dead.")
			Done = True
		elif (miles - natives) <= 15:
			print("The natives are getting close!")
	return Done


def check_progress(miles, done):
	if miles >= 200 and not done:
		print("You safely traversed the desert. You won!")
		done = True
	return done


def check_condition(miles, thirst, camel, natives, drinks, Done):
	Done = check_thirst(thirst, Done)
	Done = check_camel_tired(camel, Done)
	Done = check_natives(natives, miles, Done)
	Done = check_progress(miles, Done)
	return Done


def main_loop():
	miles_traveled, thirst, camel_tired, natives_behind, drinks_left = \
		init_values()

	done = False
	while not done:
		done = check_condition(miles_traveled, thirst, camel_tired,
		                       natives_behind, drinks_left, done)
		if done:
			break
		show_options()
		choice = input("Your Choice? \n")
		if choice.upper() == "A":
			drinks_left, thirst = drink_canteen(drinks_left, thirst)
		# drink from canteen
		elif choice.upper() == "B":
			miles_traveled, thirst, camel_tired, natives_behind = travel(2,
			                                                             miles_traveled,
			                                                             thirst,
			                                                             camel_tired,
			                                                             natives_behind)
		# moderate speed
		elif choice.upper() == "C":
			miles_traveled, thirst, camel_tired, natives_behind = travel(1,
			                                                             miles_traveled,
			                                                             thirst,
			                                                             camel_tired,
			                                                             natives_behind)
		# fullspeed ahead
		elif choice.upper() == "D":
			camel_tired, natives_behind, thirst = rest(camel_tired,
			                                           natives_behind, thirst)
		# stop and rest
		elif choice.upper() == "E":
			show_status(miles_traveled, drinks_left, natives_behind)
		# status check
		elif choice.upper() == "Q":
			# quit
			done = True
		else:
			print("Invalid Choice")


def main():
	print_instructions()
	main_loop()


if __name__ == '__main__':
	main()
