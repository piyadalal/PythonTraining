#! /usr/bin/env python3
# Author: PDalal
# Version: 1.0
# Description: This script will demo HowTo
"""
    DocString
"""
master_pin = "0123"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = input("enter pin = ")
    if pin == master_pin:
        print("valid pin")
        break # correct master pin breaks out
    else:
        print("invalid pin")
        attempts += 1   # allow more attempts until pin not correct

else:
    # only executes ONCE when while loop becomes False
    print("Too  many attempts, card is blocked")


print("Done")