#Darwin Portillo
#HW project 3

#set variable for package cost 
package_cost = 99.0

#get number of packages purchased
packages = int(input('Enter the number of packages purchased: \n')) 

#get gross cost of packages purchased 
gross_cost = packages*package_cost

#get discount %
if packages >= 1:
	if packages >= 1 and packages <10:
		discount = 0
	elif packages >= 10 and packages <= 19:
		discount = gross_cost*.10
	elif packages >= 20 and packages <= 49:
		discount = gross_cost*.20
	elif packages >= 50 and packages <= 99:
		discount = gross_cost*.30
	elif packages >= 100:
		discount = gross_cost*.40
else:
	discount = 0

#get discount and total
if packages <= 0:
	print('Packages purchased cannot be less than 1. Try again.')
if packages >=1 and packages <=9:
	print('Discount = $' + str(round(discount,2)))
	print('Total = $' + str(round(gross_cost,2))) 
if packages >=10:
		if packages >= 10 and packages <= 19:
			print('Discount = $' + str(round(discount,2)))
			print('Total after Discount = $' + str(round(gross_cost-discount,2)))
		elif packages >= 20 and packages <= 49:
			print('Discount = $' + str(round(discount,2)))
			print('Total after Discount = $' + str(round(gross_cost-discount,2)))
		elif packages >= 50 and packages <= 99:
			print('Discount = $' + str(round(discount,2)))
			print('Total after Discount = $' + str(round(gross_cost-discount,2)))
		elif packages >= 100:
			print('Discount = $' + str(round(discount,2)))
			print('Total after Discount = $' + str(round(gross_cost-discount,2)))
		 