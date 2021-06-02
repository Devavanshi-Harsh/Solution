#2: Write a Python program to calculate the number of days between two dates.
# Sample dates : (20200702), (20200711)
#import datetime module

from datetime import date



def divider(n):
    '''
    the program just take a string containing a date
    and returns year, month and day in integer formate
    '''

    year=int(n[0:4])
    month=int(n[4:6])
    day=int(n[6:9])
    return year, month, day



#input for first date
date1=input("enter first date in YYYYMMDD format")
year,month,day=divider(date1)
first_date=date(year, month, day)

#input for last date
date2=input("enter first date in YYYYMMDD format")
year,month,day=divider(date2)
last_date=date(year, month, day)

#calculations for result
diff_days=last_date-first_date

print(diff_days)
