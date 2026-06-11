#dates

#You can find the number of days between two dates by
#subtracting the day number of the earlier date from the
#day number of the later date.
import jmputils

# list packages installed
jmputils.jpip('list')

#install a new package through jpip
jmputils.jpip('install', 'datetime')

from datetime import date

earlier_date = date(2017, 6, 1)
later_date = date(2017, 6, 28)

days_between = later_date.day - earlier_date.day
print(days_between)
print("There are", days_between, "days between", earlier_date, "and", later_date)

import datetime
todays_date = date.today()
current_time = datetime.datetime.now()

#Print today's date with the
#form year/month/day. For example, January 15th, 2016
#would be 2016/1/15.
print(str(todays_date.year) + '/' + str(todays_date.month) + '/' + str(todays_date.day))

#Print the current time with
#the form hour:minute:second, such as 12:57:15. 
print(str(current_time.hour) + ':' + str(current_time.minute) + ':' + str(current_time.second))

#durations
start_hour = 3
start_minute = 48
length = 172

add_hours = length // 60
length -= add_hours * 60
add_minutes = length 

temp_minutes = start_minute + add_minutes
end_minutes = temp_minutes % 60
# increment the additional hours if the additional minutes are over an hour
add_hours += temp_minutes // 60
end_hours = start_hour + add_hours

print(str(end_hours) + ":" + str(end_minutes))



#Given the current date and expiration date, determine whether a food with the listed
#expiration date has expired. Print True if it has expired,
#False is it has not. A food is defined as expired if the
#current date is _after_ the expiration date, not equal to
#it.
current_day = 14
current_month = 7
current_year = 2019
exp_day = 14
exp_month = 6
exp_year = 2019

current_date = date(current_year, current_month, current_day)
expiry_date = date(exp_year, exp_month, exp_day)

days_between = expiry_date.day - current_date.day
months_between = expiry_date.month - current_date.month
years_between = expiry_date.year - current_date.year
print(days_between<0 or months_between<0 or years_between<0)