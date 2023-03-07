#Darwin Portillo

#get sales 
sales = float(input('Enter sales number: '))

#get commisions
if sales >=50000 and sales < 70000:
	commission = sales*.10
	salary = 70000
	total = salary + commission
	print(f'Commission is ${commission:,}')
	print(f'Salary plus commission is ${total:,}')

elif sales >=70000 and sales < 90000:
	commission = sales*.20
	salary = 80000
	total = salary + commission
	print(f'Commission is ${commission:,}')
	print(f'Salary plus commission is ${total:,}')
	
elif sales >=90000 and sales <= 100000:
	commission = sales*.30
	salary = 90000
	total = salary + commission
	print(f'Commission is ${commission:,}')
	print(f'Salary plus commission is ${total:,}')