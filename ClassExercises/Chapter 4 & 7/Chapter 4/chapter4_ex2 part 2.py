#Darwin Portillo
#Exercise 1 Part 2

#maximum number 
max = 5 

#get accumulator value 
total = 0.0 

#explain what we are doing 
print('This program calculate the sum of and average of the ')
print(f'{max} numbers you will enter.')

#get the numbers and accumulate them 
for counter in range(max):
	number = int(input('Enter a number: '))
	total = total+number


#Display the total of numbers 
print(f'The total is {total}.')

#calculate the average and print 
average = total / max
print(f'The average is {average}.')
