#Darwin Portillo
#Exercise 5 Part 2

#set variables
fastest= None
slowest = None
total = 0.0

#Get number of laps
laps=int(input('Enter number of laps:'))

#Repeat for each loop
for lap in range(1,laps+1):
	print('Lap',lap,'of', laps)
	lap_time=float(input('Enter lap time in minutes: '))
	total +=lap_time

#is the lap the fastest so far
	if fastest ==None or lap_time < fastest:
		fastest = lap_time

#is the lap is slowest so far
	if slowest ==None or lap_time > slowest:
		slowest = lap_time

print('\nfastest lap:', fastest)
print('slowest lap:', slowest)
print('average lap:', round(total/laps,2))