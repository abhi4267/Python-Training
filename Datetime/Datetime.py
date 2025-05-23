'''Python's datetime module provides tools for working with dates and times. Formatting datetime objects into strings is achieved using the strftime() method, which takes format codes as arguments to specify the desired output. Parsing strings into datetime objects is done using the strptime() method, requiring a format string that matches the input.'''
from datetime import datetime
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date) # Output will vary depending on the current time

'''To parse a string in the format "MM/DD/YYYY" into a datetime object:
Python'''

date_string = "08/16/2023"
date_object = datetime.strptime(date_string, "%m/%d/%Y")
print(date_object) # Output: 2023-08-16 00:00:00