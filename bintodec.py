""" Converts a value from binary to decimal. 
    Created by QuirkySquid on 10/1/18 """

success = False
inputString = input("Enter a binary number: ")

while (not success):
    try:
        output = int(inputString, 2)
        print(output)
        success = True
    except:
        inputString = input("Please enter a valid binary number: ")

