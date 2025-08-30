#  Number Reverser using While Loop
num = int(input("Enter a number to reverse: "))
rev = 0
while num > 0:
    digit = num % 10         
    rev = rev * 10 + digit   
    num = num // 10          

print(f" Reversed number: {rev}")
