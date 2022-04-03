# converting days to week & day, to format print as
# 1 week + 1 day
# 1 week + 2 days
# 3 weeks + 1 day,
# 12 weeks + 3 days
# 1 day
# 2 days
# 1 week
# 3 days

from ast import And

n = int(input("Enter the number of day:"))
week, day = divmod(n, 7)

#if week is greater than 0

if((week>0) and (day>0)):
    
   #if week equals 1 
   if((week==1) and (day==1)):
    print(week, "week +", day, "day")
   elif((week==1) and (day>1)):
     print(week, "week +", day, "days")
   
   #if week is greater than 1
   elif((week>1) and (day==1)):
       print(week, "weeks +", day, "day")
   elif((week>1) and (day>1)):
       print(week, "weeks +", day, "days")

#if week is 0

if((week==0) and (day>0)):
    if(day==1):
     print(day, "day")
    else:
     print(day, "days")

#if day is 0

if((day==0) and (week>0)):
    if (week==1):
     print(week, "week")
    else:
     print(week, "weeks")