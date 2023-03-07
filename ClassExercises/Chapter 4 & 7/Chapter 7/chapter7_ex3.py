#Darwin Portillo
#Exercise 3

#print('I will display the numbers 1 through 10 as odd and even numbers. ')

#the numbers are placed in an array 
l1=[1,2,3,4,5,6,7,8,9,10]

#print odd then even numbers in l1
print('Odd numbers are: ')
for n in l1:
	if n%2!=0:
		print(f"{n} is odd\n")
print('Even numbers are: ')
for n in l1:
	if n%2==0:
		print(f"{n} is even\n")

