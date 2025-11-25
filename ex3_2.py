#! /usr/bin/env python3
# Author: PDalal
# Version: 1.0
# Description: This script will demo HowTo
"""
    DocString
"""
import sys

var = input("Please enter an integer")
try:
    if not var.isdecimal():
         #print("You must enter an Integer")
         sys.exit(1)

except SystemExit:
    print("You must enter an Integer")

number = int(var)
#stop = 0 or 1
if number % 2 == 0:
    stop = -2
else:
    stop = 0

for i in range(number, stop, -2):
    print(i)

