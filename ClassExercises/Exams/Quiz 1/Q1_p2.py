#Darwin Portillo

#get 4 scores and assign to variables 
num1 = float(input('Enter the first score: '))
num2 = float(input('Enter the second score: '))
num3 = float(input('Enter the third score: '))
num4 = float(input('Enter the fourth score: '))

#calculate the average of the four scores
average = (num1+num2+num3+num4)/4

#calculate the total 
total = num1+num2+num3+num4

#Display the average and total 
print(f'The total and average score is: sum = {total:,} , average = {average:,}')