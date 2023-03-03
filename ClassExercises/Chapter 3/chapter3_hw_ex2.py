#Darwin Portillo
#HW project 2 

#get hot dogs & people attending 
number_of_people = int(input('Enter number of people: \n'))
hotdogs_per_person = int(input('Enter number of hot dogs per person: \n'))

# set variables for number of people and hot dogs 
hotdogs_per_package = 10
hotdog_buns_per_package = 8

#get total amount of hot dogs per person 
total_hotdogs = number_of_people * hotdogs_per_person

#get minimum number of hot dogs per packages required 
hotdog_packages_needed = total_hotdogs / hotdogs_per_package
print('The minimum number of hot dog packages required are: ', hotdog_packages_needed)

#get minimum number of hot dog buns per packages required
hotdog_buns_needed = total_hotdogs / hotdog_buns_per_package
print('The minimum number of hot dog bun packages required are: ', hotdog_buns_needed)

#get number of hot dogs left over 
hotdogs_left_over = total_hotdogs % hotdogs_per_package
print('The number of hot dogs left over are: ', round(hotdogs_left_over,3))

#get number of hot dog buns left over 
hotdog_buns_left_over = total_hotdogs % hotdog_buns_per_package
print('The number of hot dogs left over are: ', hotdog_buns_left_over)