#Darwin Portillo
#Exercise 2

#set range for number of inputs 
max = 4
#get the accumulator 
total = 0.0

for counter in range(max):
#get sales and commisions four times  
	sales = float(input('Enter the amount of sales: \n'))
	comm_rate = float(input('Enter the commission rate: \n'))
#calculate commissions 
	commission = sales*comm_rate
#calculate the total sales + commissions 
	total = total+(sales+commission)
#print the running total of sales and commissions 
print(f'The total for all sales and commissions is ${total}.')
