#Darwin Portillo
#Exercise 1 part 2

#get pocket number
pocket_number = int(input('Enter Pocket Number: \n'))

#get pocket colors and return message
if pocket_number >= 0 and pocket_number <= 36:
    
    if pocket_number == 0:
        pocket_color = "green"
   
 #use modulus operator to determine if number is even or odd    
    elif pocket_number >= 1 and pocket_number <= 10:
        if pocket_number % 2 != 0:
            pocket_color = "red"
        else:
            pocket_color = "black" 

    elif pocket_number >= 11 and pocket_number <= 18:
        if pocket_number % 2 != 0:
            pocket_color = "black" 
        else:
            pocket_color = "red"
    
    elif pocket_number >= 19 and pocket_number <= 28:
        if pocket_number % 2 != 0:
            pocket_color = "red"
        else:
            pocket_color = "black" 

    elif pocket_number >= 29 and pocket_number <= 36:
        if pocket_number % 2 != 0:
            pocket_color = "black" 
        else:
            pocket_color = "red"

    print("Pocket color  ", pocket_color)
else:
    print("Error. Number is not wihthin range of 0 and 36.\nTry again.")


