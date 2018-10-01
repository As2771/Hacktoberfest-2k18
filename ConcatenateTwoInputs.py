import time

firstInput = input("Please enter your first input: ")
secondInput = input("Please enter your second input: ")

print(firstInput + " " + secondInput)

try:
    input("Press Enter to continue...")
except SyntaxError:
    pass