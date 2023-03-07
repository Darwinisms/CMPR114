#Darwin Portillo
#Exercise 3 Part 2

#set total as 0
total=0

#set loop from 1 to 5 unsing range
for i in range(1,6):

#get number of bugs collected each day and create running total
	total+=int(input("Enter the number of bugs collected day "+str(i)+" : "))

#printing Total number of bugs collected
print("Total number of bugs collected are:", total)