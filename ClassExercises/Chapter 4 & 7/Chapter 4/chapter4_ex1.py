#Darwin Portillo
#Exercise 1


# set max temp (sentinel) 
MAX_TEMP = 102.5

#get the temperature 
temperature = float(input("Enter four temperatures under 102.5: "))

#
while temperature <= MAX_TEMP:
	print('The temperature is too high.')
	temperature = float(input('Enter the new Celsius temperature: '))