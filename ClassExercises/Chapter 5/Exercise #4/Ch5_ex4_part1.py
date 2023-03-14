#creat a global variable 
num1 = 0
num2 = 0
num3 = 0

#get numbers and add them
def main(): 
	global num1, num2, num3
	num1 = int(input('Enter as number: '))
	num2 = int(input('Enter as number: '))
	num3 = int(input('Enter as number: '))
	add_numbers()
	avg_numbers()
	print(f'Sum of the three numbers is: {total}')
	print(f'Average of all three numbers is: {avg}')

#get total for all three numbers
def add_numbers():
	global total
	total = num1 + num2 + num3

#get avg for all three numbers
def avg_numbers():
	global avg
	avg = round((num1 + num2 + num3)/3,2)



# call the main function 
main()


#def add(num1,num2,num3):
#	global total
#	total = num1 + num2 + num3
#	return total
#add(3,2,6)
#print(total)


