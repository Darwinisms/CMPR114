#Darwin Portillo 

#set variable for months 
months = 12

#get number of years 
years = int(input('Enter numbers of years: ')) 
	
#validate if year is less than 1
if years < 1:
	print('Years must be positve, try again')

#print years and months 
for counter in range(1, years+1):
	#initialize an accumulator for total inches of rainfall 
	total = 0.0

#Display the year number.
	print(f'Enter Rainfall for Year {counter}: ')

#inner loop to get rainfall
	for months_num in range(1,months+1):

#get rainfall numbers 
		rainfall=int(input(f'Enter rainfall in inches for month {months_num} : '))

#add rainfall to the accumulator
		total += rainfall
#calculate average rainfall
		average= total/months

	print(f'After {months} months: ')
	print(f'\tTotal rainfall was {total} inches')
	print(f'\tAverage rainfall was {average} inches')