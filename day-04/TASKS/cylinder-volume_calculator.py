import math

# Write the code ↓ to read the radius and height of a cylinder from the user.
# Be cautious when reading input of various data types.


print("CYLINDER VOLUME CALCULATOR FOR ALF")
radius = float(input("Please, enter the radius of the cylinder: "))
while radius < 0:
    print("Invalid input")
    radius = float(input("Please, enter the radius of the cylinder: "))
height = float(input("Please, enter the radius of the cylinder: "))
while height < 0:
    print("Invalid input")
    height = float(input("Please, enter the radius of the cylinder: "))
# Write the code ↓ to calculate the volume of the cylinder using the formula V = πr^2h.
# Formula to calculate the volume (V) of a cylinder:
# V = π * r^2 * h



volume = math.pi * (radius * radius) * height



# Write the code ↓ to display the calculated volume with 2 decimal places.
# Select and employ a string concatenation method based on your personal preference and comfort level.


print("The volume of the cylinder is: %.2f" %(volume))



