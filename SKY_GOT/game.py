"""
GOT - game of tanks

"""

import sys
import app.tank as tank

def main():
    # Instantiate or create 3 new tanks object
    eric_tank = tank.Tank('German', 'Tiger')
    juan_tank = tank.Tank('American','Sherman')
    priya_tank = tank.Tank('British','Churchill')

    # And the game begins..
    eric_tank.accel(63) # speed increases
    juan_tank.accel(29) # speed increases
    priya_tank.rotate_left(289)
    priya_tank.accel(34)
    priya_tank.shoot() # shell - 1
    # And success...
    eric_tank.take_damage(64) # health decreases by 64
    juan_tank.take_damage(27) # health decreases by 27

    #And now for some Game visuals!!
    print(f"Health of Eric: {eric_tank._health}")
    print(f"Health of Eric and Juan: {eric_tank + juan_tank}")
    print(f"Status of Eric Tank: {eric_tank}") ## is same as str(eric_tank) because print
    ## converts everythong to string
    print(str(eric_tank))

    eric_tank._health = 100
    print(f"Health of Eric Tank with : {eric_tank._health}")

    eric_tank.set_health(400)
    print(f"Health of Eric Tank using getter and setter: {eric_tank._health}")

    eric_tank.tank_health = 102 # variable with a special property
    print(f"Health of Eric Tank using property function: {eric_tank.tank_health}") # with getter use getter method with value use setter

    # use property
    # use decorator
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)