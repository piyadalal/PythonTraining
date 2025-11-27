import sys
import app.basic
import app.adv  as adv

menu = """
    Menu Options
    ------------
    1. Display Basic Calc examples
    2. Display Adv Calc examples
    q=quit
"""
while True:
    print(menu)
    option = input("Enter option (1-2,q=quit): ")

    if option == 1:
        print(f"15 + 14 + 13 = {basic.add(15, 14, 13)}")
        print(f"15 * 14 * 13 = {mul(15, 14, 13)}")
        print(f"15 / 14 = {div(15, 14)}")
    elif option == 2:
        print(f"15**2 = {power(15, 2)}")
        print(f"15 % 2 = {mod(15, 2)}")
        print(f"\N{square root}15 = {sqrt(15)}")
    elif option == "q":
        break
    else:
        print("invalid option")

sys.exit(0)