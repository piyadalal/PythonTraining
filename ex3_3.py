#! /usr/bin/env python3
# Author: PDalal
# Version: 1.0
# Description: This script will demo HowTo
"""
    DocString
"""
year_1 = int(input("Enter a year"))

if (year_1 % 400 == 0 and year_1 % 100 != 0) or (year_1 % 400 == 0):
    print("Is a leap year")
else:
    print("not a leap year")

year = int(input("Enter a year"))

if year % 400 == 0:
    print("leap year")

elif year % 100 == 0:
    print("not a leap year")

elif year % 4 == 0:
    print("Is a leap year")

else:
    print("not a leap year")