
year = int(input("Enter a year:\n"))
leap = False

if (year % 4 == 0):
	leap = True
	if (year % 100 == 0):
		if (year % 400 == 0):
			leap = True
		else:
			leap = False
else:
	leap = False

if (leap == True):
	print(str(year) + " is a leap year")
else:
	print(str(year) + " is not a leap year")
	
