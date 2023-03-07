#Darwin Portillo

#get sales 
sales = float(input('Enter sales number: '))

#get commisions
if sales >=50000 and sales <= 60000:
	commission = sales*.10
	print(f'Commission is ${commission:,}')

elif sales >=70000 and sales <= 80000:
	commission = sales*.20
	print(f'Commission is ${commission:,}') 
	
elif sales >=90000 and sales <= 100000:
	commission = sales*.30
	print(f'Commission is ${commission:,}')