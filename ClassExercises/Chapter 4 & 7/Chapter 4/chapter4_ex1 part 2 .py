#Darwin Portillo
#Exercise 2 Part 2

#get multiplication variable
multiple = 10 

#get first number to be tested in the while clause 
number = int(input('Enter a number less than 100: '))
product = number * multiple
print(f'Number entered x 100: {product}')

#maximum number 
while product < 100: 
	value = int(input('Enter a number: '))

	#multiply product by 10
	product = value * multiple
	print(f'Number entered multiplied by 10: {product}') 
