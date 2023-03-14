#This program demonstrates two functions that 
# have local variables with the same name 

def main():
# Call the texas fuction 
 texas()
# Call the california fuction 
 california()


#Definition of the texas fucntion. it creates 
# a local variable named birds 
def texas():
	birds = float(input('Enter number of Birds in Texas: '))
	print(f'Texas has {birds} birds.')

#Definition of the texas fucntion. it creates 
# a local variable named birds 
def california():
	birds = float(input('Enter number of Birds in California: '))
	print(f'California has {birds} birds.')

main()


