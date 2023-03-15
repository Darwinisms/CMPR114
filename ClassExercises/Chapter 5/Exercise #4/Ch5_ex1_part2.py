#This program converts kilometers to miles 

def main():
	kilometers = float(input('Enter distance in Kilometers: '))
	
	conversion(kilometers)

def conversion(kilometers):
	miles = (kilometers*.6214)
	print(f'Miles = {miles:.2f}')

main()