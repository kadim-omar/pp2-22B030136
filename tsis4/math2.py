#1
import math

degree = int(input())
radian = degree * math.pi / 180

print("Input degree:", degree)
print("Output radian:", radian)

#2
height = 5
base1 = 5
base2 = 6

area = (base1 + base2) * height / 2

print("Height:", height)
print("Base, first value:", base1)
print("Base, second value:", base2)
print("Area:", area)

#3

num_sides = 4
side_length = 25

perimeter = num_sides * side_length
apothem = side_length / (2 * math.tan(math.pi / num_sides))
area = (perimeter * apothem) / 2

print("Input number of sides:", num_sides)
print("Input the length of a side:", side_length)
print("The area of the polygon is:", area)

#4
base_length = 5
height = 6

area = base_length * height

print("Length of base:", base_length)
print("Height of parallelogram:", height)
print("Area of parallelogram:", area)