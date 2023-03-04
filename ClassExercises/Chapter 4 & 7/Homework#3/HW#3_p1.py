#Darwin Portillo
#HW #3 Project 1 

#get speed of vehicle in mph 
mph = int(input('What is the speed of vehicle in mph: '))

#get hours traveled 
hours = int(input('Enter how many hours were traveled: ' ))

# Print the table headings.
print()
print('Hours\tDistance Traveled')
print('-------------------------')

#print the hours traveled and distance traveled 
for hours in range(1, hours + 1):
	#get distance 
	distance  = hours*mph 
	print(f'{hours}\t{distance}')