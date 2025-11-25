#! /usr/bin/env python3
# Author: PDalal
# Version: 1.0
# Description: This script will demo HowTo
"""
    DocString
"""
count = 0 # 1. initialize the counter
while count < 10: # 2.Test Counter
    print(count)
    count += 1

# alternativel we could use for loop and range function
# range(start, stop, step) , range(0,10,1)
for num in range(0,10,1):
    print(num)

for num in range(0,10):
    print(num)

for num in range(10):
    print(num)

print(list(range(0,2)))

#print(range(0,10,0)) # ValueError: range() arg 3 must not be zero

step = 1
print(list(range(0, 10, step)))

