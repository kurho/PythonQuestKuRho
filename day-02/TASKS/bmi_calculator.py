# BMI - NUTRITIONAL STATUS GUIDE
"""
    BMI         NUTRITIONAL STATUS

BELOW 18.5         UNDERWEIGHT
18.5 - 24.9       NORMAL WEIGHT
25.0 - 29.9        OVERWEIGHT
ABOVE 30.0          OBESITY
"""
 
# Write the code ↓ to read user's height and weight.
# Be cautious when reading input of various data types.







print("BMI CALCULATOR FOR ALF")
weight = float(input("\nEnter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
print("\nHEIGHT: %.2f - WEIGHT: %.2f: "%(height, weight))


# Write the code ↓ to perform the calculations of user's BMI and categorize its status.





BMI = weight/(height**2)

if BMI < 18.5:
    status = "underweight"
elif BMI >= 18.5 and BMI <= 24.9:
    status = "normal weight"
elif BMI >= 25.0 and BMI <= 29.9:
    status = "overweight"
elif BMI >= 30:
    status = "obese"

# Write the code ↓ to display the user's BMI and its classification.
# Select and employ a string concatenation method based on your personal preference and comfort level.
# Use :.2f format specifier when printing the BMI value to display the BMI with only two decimal places.

print("BMI: %.2f - NUTRITIONAL STATUS: %s " %(BMI, status))






