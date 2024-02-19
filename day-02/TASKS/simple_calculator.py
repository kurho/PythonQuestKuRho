# Write the code ↓ to read user's input for two operands and selected operation.
# NOTE: The two operands must be read as floats.






print("Simple Calculator for Alf")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, x, /): ")
result = 0.0



# Write the code ↓ to perform the calculations based on the selected operation.







if operator == '+':
    answer = num1 + num2
elif operator == '-':
    answer = num1 - num2
elif operator == 'x':
    answer = num1 * num2
elif operator == '/':
    answer = num1 / num2
else:
    print("Invalid input")
    
 
# Write the code ↓ to display the result.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("The result of %.2f %s %.2f is %.2f" %(num1, operator, num2, result))






