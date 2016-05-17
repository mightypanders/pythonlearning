months="JanFebMarAprMayJunJulAugSepOctNovDec"

n = int(input("Enter month Number: "))
if(n>0 and n<13):
	mE=(3*n)
	mA=mE-3
	print (months[mA:mE])
else:
	print("falsche Zahl")