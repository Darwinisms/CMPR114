#Darwin Portillo

#get gross salary 
salary = int(input('Enter your gross salary: '))

#get 10% of salary 
ten_percent = salary*.10

#add 10% to gross salary
total  = salary + ten_percent

#print salary with decimals and $
print(f'Total salary after 10% is ${total:,}')
