# This program demonstrates monthly and yearly automibile costs

def main():
	print('Enter the following expenses to calculate \nmonthly and yearly automobile expense.')

	#get expenses
	print()
	loan_payment = float(input('Enter loan payment: '))
	insurance = float(input('Enter insurance payment: '))
	gas = float(input('Enter gas payment: '))
	oil = float(input('Enter oil payment: '))
	tires = float(input('Enter tires payment: '))
	maintenance = float(input('Enter maintenance payment: '))
	print()

#call functions
	monthly_expense(loan_payment,insurance,gas,oil,tires,maintenance)
	yearly_expenses(monthly_cost)

#calculate monthly expenses
def monthly_expense(loan_payment,insurance,gas,oil,tires,maintenance):
	global monthly_cost
	monthly_cost = loan_payment+insurance+gas+oil+tires+maintenance
	print(f'Total monthly costs: ${monthly_cost:,.2f}')

#calculate yearly expenses
def yearly_expenses(monthly_cost):
	yearly_cost = monthly_cost*12
	print(f'Total yearly costs: ${yearly_cost:,.2f}')

main()