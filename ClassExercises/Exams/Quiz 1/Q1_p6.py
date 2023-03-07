#Darwin Portillo

#set variable for # of test scores 
MAX = 4 


# Get the numbers and accumulate them.
for counter in range(MAX):
	while 
	test_scores = int(input('Enter a test score: '))
	total = 0.0
	if  test_scores >=90 and test_scores <=100:
		letter_grade = 'A'
	elif  test_scores >=80 and test_scores <90:
		letter_grade = 'B'
	elif  test_scores >=70 and test_scores <80:
		letter_grade = 'C'
	elif  test_scores >=60 and test_scores <70:
		letter_grade = 'D'
	elif  test_scores <60:
		letter_grade = 'F'
	print(f'Letter grade: {letter_grade}')
	total = total + test_scores

# Calculate the average test score for this student.
	average = total / MAX

# Display the average.
print(f'The average test score is: {average:.1f}')
print()