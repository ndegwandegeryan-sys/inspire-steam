#Name : ndegwandegeryan
#Date : 13/02/2026
#program to do mathematical operations

import math
number = 16.79

print(abs(number))

print(math.ceil(number))

angle_radians= 60
angle_degree = angle_radians/180

x = 1 #radains
y = math.degrees(x)


print(x)
print(y)



print(math.sin(angle_degree))
print(math.cos(angle_degree))
print(math.tan(angle_degree))


print(min(3,4))
print(max(13,46))

print(math.sqrt(144))

print(25**2) #25 raised to power 2

print(5**3)


for x in range(-180,210,30):
    print(math.sin(x))

for x in range(-180,210,30):
    print(math.cos(x))

for x in range(-180,210,30):
    print(math.tan(x))

for x in range (1,9) :
    print(x**2)
