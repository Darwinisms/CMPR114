#Darwin Portillo

#set accumulator
total = 0.0 

#get first number 
print('Enter a series of positive numbers. A negative number will end the program.')
numbers = int(input('Enter number: '))

#print series and sum numbers 
while numbers >= 0:
	total = total + numbers
	numbers = int(input('Enter number: '))
print(f'Sum of all numbers is {total}')