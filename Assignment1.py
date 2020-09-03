# Find the values of slopes m1 & m2 of two lines when tangent of the angle is 1/3 and 
#and m1 is twice m2

# we will only take m2 into consideration and find m1 from it.
# Taking m1 = 2m2, and substituting in the tan value, we get the quadratic equation
# 2m2 ^2 -3m2 + 1 = 0

import math

a = 2
b = -3
c = 1

# calculate the discriminant
d = (b**2) - (4*a*c)

# Two roots of the quadratic equation are:

m2_1 = (-b-math.sqrt(d))/(2*a)
m2_2 = (-b+math.sqrt(d))/(2*a)

print('The values of m2 are {},{}, {} and {}'.format(m2_1,m2_1*-1, m2_2, m2_2*-1))

print('Values of m1 are {},{},{},{}'.format(m2_1*2, m2_1*-2,m2_2*2, m2_2*-2))

print(' The solutions for slopes of Line1 & Line 2 are:')
print('({},{})'.format(m2_1*2, m2_1))
print('({},{})'.format(m2_1*-2, m2_1*-1))
print('({},{})'.format(m2_2*2, m2_2))
print('({},{})'.format(m2_2*-2, m2_2*-1))
