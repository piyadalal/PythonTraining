#! /usr/bin/env python3
# Author: PDalal
# Version: 1.0
# Description: This script will demo HowTo
"""
    DocString
"""
master_pin = "0123"
pin = None

while pin != master_pin:
    pin = input("enter pin = ")
    if pin == master_pin:
        print("valid pin")
    else:
        print("invalid pin")


print("Done")