#Darwin Portillo
#HW project 1 

#get month input 
month = int(input('Enter month as number between 1 and 12: \n'))

#display month as quarter 
if month >=1 and month <= 12:
	if month >=1 and month <=3:
		print('Month is in the First Quarter')
	elif month >=4 and month <=6:
		print('Month is in the Second Quarter')
	elif month >=7 and month <=9:
		print('Month is in the Third Quarter')
	elif month >=10 and month <=12:
		print('Month is in the Fourth Quarter')
else:
	print('Error. Number is not between desired range')