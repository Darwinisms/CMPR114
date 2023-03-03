#Darwin Portillo
#Exercise 4

#get number from input 
number = int(input('Enter number within 1 to 10: '))

#displays error message or roman numeral 

if number >10 or number < 1:
	print('The number entered is not whitin range. Please try again.')
elif number == 1:
	print('I')
elif number == 2:
	print('II')
elif number == 3:
	print('III')
elif number == 4:
	print('IV')
elif number == 5:
	print('V')
elif number == 6:
	print('VI')
elif number == 7:
	print('VII')
elif number == 8:
	print('VIII')
elif number == 9:
	print('IX')
elif number == 10:
	print('X')