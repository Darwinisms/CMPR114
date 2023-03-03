#Darwin Portillo 
#Exercise 3

#list variables 
bonus = 500
comission_rate = .12

#get sales input 
sales = int(input('What is your total sales? '))

#get sales bonus number 
if sales > 50000:
	print('You met your sales quota!')
	print('Your bonus is $' + str(bonus))
else:
	print('Sorry, you do not get a sales bonus this year.')
	print('Sales qouta was not met.')
