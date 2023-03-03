#Darwin Portillo
#Exercise 2 part 2


#get weight of package from customer
package_weight = float(input('Enter package weight: \n'))

if package_weight >0 and package_weight <=2:
	print('Shipping charge total: $', round(package_weight*1.50,2))
elif package_weight >2 and package_weight <=6:
	print('Shipping charge total: $', round(package_weight*3,2))
elif package_weight >6 and package_weight <=10:
	print('Shipping charge total: $', round(package_weight*4,2))
elif package_weight >10:
	print('Shipping charge total: $',round(package_weight*4.75,2))
else:
	print('Your package is must be made out of air.')