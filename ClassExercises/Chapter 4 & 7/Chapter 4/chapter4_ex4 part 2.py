#Darwin Portillo
#Exercise 4 Part 2

# set variable for calorie burn per min
cal_per_minute = 4.2


# set the range to start from 10 to 30 exluding 31 and increase the value of i by 5 each time
for i in range(10,31,5):
    calories_burned = cal_per_minute*i
    print('You burn ',calories_burned,' calories in ',i , " minutes")