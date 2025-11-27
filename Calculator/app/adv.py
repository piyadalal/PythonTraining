import sys

def power(x, z):
    """ Return POWER of x to z as a float """
    return float(x**z)

def mod(x, z):
    """ Return REMAINDER of x divided by z as a float """
    return float(x % z)

def sqrt(x):
    """ Return of x as a float """
    return float(x**0.5)

print("------------ Adv Calc App ------------")
print(f"9 ** 8 = {power(9, 8)}")
print(f"9 % 8 = {mod(9, 8)}")
print(f"\N{square root}9 = {sqrt(9)}")
print("--------------------------------------")

sys.exit(0) # Explicit EXIT with return code (0=success, 1-255=error)