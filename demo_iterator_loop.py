#! /usr/bin/env python3
# Author: PDalal
# Version: 1.0
# Description: This script will demo HowTo iterate through sequences
# str,tuple,list,dict,set using an iterator for loop
"""
    Code template for coder , DocString for user
"""
students = ["a", "b", "c", "d"]
for name in students:
    print(name, end="/n")
    print(name, end=",")

# Iterate through the list and modify each object
# using iterators for loops and index
# enumerate returns tuple as (index_no, object: list, str ) ()
idx = 0
for name in students:
    print(name.upper())
    students[idx] = name.upper()
    idx += 1


#enumrate removes need for idx and idx increment
# enumerate returns a tuple immutable tube of idx, name
for (idx,name) in enumerate(students):
    if idx not in (1,2):
        print(name.upper())
        students[idx] = name.upper()
print("Students =", students) # same as putting in else and 2 spaces not required as part of loop