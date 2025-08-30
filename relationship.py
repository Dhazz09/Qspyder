# Relationship Checker: Integer Edition

# Input two integers
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Check the relationship
if a > b:
    print(f"{a} is greater than {b} ")
elif a < b:
    print(f"{a} is less than {b} ")
elif a == b:
    print(f"{a} is equal to {b} ")
else:

    print("Unexpected input. ")
