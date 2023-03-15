#This program will ask for hours and worked and hourly pay then calculate gross pay 

def main():
	hours_worked = float(input('Enter hours worked: '))
	hourly_pay = float(input('Enter hourly pay: '))
	gross_pay(hours_worked,hourly_pay)
#get gross pay
def gross_pay(hours_worked,hourly_pay):
	gross_pay = hours_worked*hourly_pay
	print(f'Total gross pay is: ${gross_pay:,.2f}')

#call main function
main()