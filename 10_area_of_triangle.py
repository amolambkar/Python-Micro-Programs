# calculate area
# of triangle
# in python

a = 5
b = 6
c = 7

# calculate the semi-perimeter
s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print(area)