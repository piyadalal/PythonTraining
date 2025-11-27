#! /usr/bin/env python3
# Author: DCameron
# Description: This module defines how to use Doctesting
# functions
# ´
import sys

def add (*args):
    """Return SUM of ALL parameters
    >>> add(10,20)
    30.0
    """

    sum = 0
    for num in args:
        sum += num
    return float(sum)

def mul (*args):
    """Return product of ALL parameters"""
    product = 1
    for num in args:
        product *= num
    return float(product)

def div (x,z):
    """Return quotient of x divided b z to 3 decimal places parameters"""
    return round(x/z, 3)


def main():
    print("********** Basic Calc App ************")
    print(f"4 + 3 + 2 + 1 = {add(4, 3, 2, 1)}")
    print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
    print(f"4 / 3 = {div(4, 3)}")
    print("***************************************")
    return None

if __name__ == "__main__":
    #execute only if run dorectly as program
    #
    import doctest
    doctest.testmod()
    main()
    sys.exit(0) # Explicit EXIT with return code (0=success, 1-255=error)