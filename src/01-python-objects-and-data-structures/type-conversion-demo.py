'''
    Circle Area      : pi*r^2
    Circle Perimeter : 2*pi*r

    * Given the radius of a circle, calculate its area and
    perimeter. (r: 3.14)
'''

pi = 3.14

r = float(input("radius: "))

area = pi * (r ** 2)
print(type(area))

perimeter = 2 * pi * r
print(type(perimeter))

print("area: " + str(area) + " perimeter: " + str(perimeter))
