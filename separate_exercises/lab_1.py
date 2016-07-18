def main():
	fahren = int(input("Enter Temparature in Fahrenheit: "))

	celsius = (fahren - 32) * (5 / 9)

	print("The temperature in Celsius is ", celsius)


if __name__ == '__main__':
	main()
