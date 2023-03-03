#Darwin Portillo 
#Exercise 1

#get variables
high_score = 95 

#get test scores
test1 = int(input('Enter test score 1: '))
test2 = int(input('Enter test score 2: '))
test3 = int(input('Enter test score 3: '))

#get average
average = round((test1 + test2 + test3)/3,2)


# print the average test score
print('The average score is ' + str(average))

#used to determine if the high score is above 100 
if average > 100: 
	print('The average cannot be over 100, try again') 
elif average > high_score:
	print('Your average is greater than the high score of ' + str(high_score))
elif average == high_score:
	print('Your average is equal to the high score of ' + str(high_score))
else:
	print(' Your average is below the high score of ' + str(high_score))



