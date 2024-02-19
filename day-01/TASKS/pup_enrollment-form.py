# Write the code ↓ to read user's input.
# Be cautious when reading input of various data types.
print("PUP Enrollment Form")
Name = input("Enter your full name: ")
Age = input("Enter your age: ")
Average = float(input("Enter your general weighted average: "))
is_Member = input("Are you a member of the AWS Cloud Club - Department of Cloud Computing? (yes/no): ").lower() == "yes"






# Write the code ↓ to display the user's personal information.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("\nYour Enrollment Form:")
print("Name: "+Name)
print("Age: ",Age)
print("GWA: ",Average)
if is_Member:
    print("Awstraunot: Yes")
else:
    print("Awstraunot: No")




