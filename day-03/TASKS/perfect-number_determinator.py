# Write the code ↓ to read the user's input for a positive integer.
# Be cautious when reading input of various data types.









print("PERFECT NUMBER DETERMINATOR FOR ALF")
number = int(input("Please, enter a positive integer: "))
while number <= 0:
    print("Invalid input")
    number = int(input("Please, enter a non-negative integer: ")) 
result = number

# Write the code ↓ to check if the entered integer is a Perfect Number using a loop.






perfect = 0
for i in range(1, number):
    if number % i == 0:
        perfect = perfect + i

# Write the code ↓ to display the Perfect Number check result.
# NOTE : You can use if-else statement or ternary operator to display the result.


if perfect == result:
    print("%d is a Perfect Number: "%(result))
else:
    print("%d is not a Perfect Number: " %(result))




