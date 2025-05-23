'''
What is timedelta?
timedelta is used to do date/time arithmetic, such as:

Adding or subtracting days, weeks, hours, etc.

Calculating the difference between two dates/times.


xample 1: Add/Subtract Days
python'''

from datetime import datetime, timedelta

today = datetime.now()
print("Today:", today)

# Add 7 days
next_week = today + timedelta(days=7)
print("Next Week:", next_week)

# Subtract 2 days
two_days_ago = today - timedelta(days=2)
print("Two Days Ago:", two_days_ago)
'''

date1 = datetime(2024, 12, 31)
date2 = datetime(2025, 1, 10)

diff = date2 - date1
print("Difference:", diff)  # Output: 10 days, 0:00:00
print("Days only:", diff.days)  # Output: 10
'''
from datetime import timedelta, datetime

now = datetime.now()
print("Now:", now)

after_3_hours = now + timedelta(hours=3)
after_15_minutes = now + timedelta(minutes=15)
after_30_seconds = now + timedelta(seconds=30)

print("After 3 Hours:", after_3_hours)
print("After 15 Minutes:", after_15_minutes)
print("After 30 Seconds:", after_30_seconds)

timedelta(
    days=0,
    seconds=0,
    microseconds=0,
    milliseconds=0,
    minutes=0,
    hours=0,
    weeks=0
)


'''Adding timedelta to a date object

from datetime import date, timedelta'''

d = date.today()
print("Today:", d)

ten_days_later = d + timedelta(days=10)
print("10 Days Later:", ten_days_later)
