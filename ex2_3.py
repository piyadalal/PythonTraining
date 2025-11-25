from math import pi, tan, cos

y0 = 1

x = 0.5

elevation = 80

v0 = 44

g = 9.81

theta = elevation * (pi / 180)

y = y0 + (x * tan(theta)) - ((g * (x ** 2)) / (2 * ((v0 * cos(theta)) ** 2)))

# y = y0 + x * tan(theta) - g * x**2 / 2 / (v0 * cos(theta))**2 

print("Height of the projectile:", y, "meters") 