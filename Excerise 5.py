"""
Exercise 5: Days of the Month - 30 Marks
"""
"""
we made a variable to store in the value of of the months and days are in the list.
ex. like 31 days in to first month, 28 days into second month, and etc.
"""

month_days = {
    1: 31,
    2: 28, 
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

"""
the system will ask a question to the user and get the input. It will change it and 
turn it into an integer then will store in an variable
"""
month_number = int(input("Enter a month number (1-12): "))

"""
if the user input from the user is greater equal than 1, then it will check it by using the if statement.
an example is number of days in each month, stored in a dictionary less equal then 12.
It then asks the user for the month number and then takes the month number that it gets 
from the user and looking it up in the dictionary it prints out the number of days for 
that month number. Then if the input provided is true then print the how many days are in that month.
if not then using the else statement it will print out that it is a invalid month number and ask 
enter a number from 1 to 12
"""
if 1 <= month_number <= 12:
    days_in_month = month_days[month_number]
    print(f"There are {days_in_month} days in month {month_number}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
    
    