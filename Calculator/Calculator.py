import sys
import app.basic
import app.basic as basic
import app.adv  as adv
from app.basic import add, mul, div

# imports import all the identifiers and executes all print statements and
# has sys.exit() so it terminates by only printing the print statements and tgen exit
def main():
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

        if option == "1":
            print(f"15 + 14 + 13 = {app.basic.add(15, 14, 13)}")
            print(f"15 * 14 * 13 = {basic.mul(15, 14, 13)}")
            print(f"15 / 14 = {div(15, 14)}")
        elif option == "2":
            print(f"15**2 = {adv.power(15, 2)}")
            print(f"15 % 2 = {adv.mod(15, 2)}")
            print(f"\N{square root}15 = {adv.sqrt(15)}")
        elif option == "q":
            break
        else:
            print("invalid option")
    return None

if __name__ == "__main__":
    print("running main script")
    main()
    sys.exit(0)
else:
    print("running module ")