"""
Tank Class - for a game

"""
import vehicle

class Tank(vehicle.Vehicle):
    # 2 components of a class = Attributes/properties/data and behaviour/methods
    def __init__(self, country, model): #, speed, direction, location
        #create objects at run time for eg. 50 types of app at runtime
        self._speed = 0 # don't need speed as doesn't take value from objects
        self._direction = 0
        self._location = {'x':0, 'y':0, 'z':0}
        self._health = 100
        self._shells = 20
        # no EXPLICIT return as called IMPLICITLY/Auto


    def accel(self,increase):
        self._speed += increase
        return None

    def decel(self,decrease):
        self._speed -= decrease
        return None

    def rotate_left(self,degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self,degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self,damage):
        self._health -= damage
        return None

    #CREATE SOME SPECIAL METHODS
    # OPERATOR OVERLOADING
    def __add__(self, other):
        return self._health + other._health


    # Examples of DUCK TYPING - Tank can now quack like a string
    def __str__(self):
        return f"Model={self.model}, Speed = {self._speed}, Health = {self._health}"

    # Example of GETTER and SETTER methods
    def get_health(self):
        #return None # can't see anyones health
        #or only can see some healths
        return self._health

    def set_health(self, new_health):
        self._health = new_health
        return None

    tank_health = property(get_health, set_health)
    print(tank_health)



