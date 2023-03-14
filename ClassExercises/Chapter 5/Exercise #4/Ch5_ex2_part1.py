# This program demonstrates passing two string
# arguments to a function.

def main():
#get first and last name 
	first_name = input('Enter your first name: ')
	last_name = input('Enter your last name: ')
#get address
	address = input('Enter your Address: ')
#get city 
	city = input('Enter city: ')
#get state 
	state = input('Enter state: ')
#get zip code  
	zip_code = input('Enter zip code: ')

	print(f'Your first and last name are:\n{first_name} {last_name}')
	print(f'Your address is:\n {address}')
	print(f' {city}')
	print(f' {state}, {zip_code}') 

main()