secret = "this is a test. ABC abc"

for c in secret:
	if (ord(c) == 32):
		print("SPACE", end=" ")
	else:
		print(ord(c), end="")

		ch = ord(c)
		ch += 1
		print(chr(ch), end=" ")
