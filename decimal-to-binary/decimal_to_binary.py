import math

#function to convert decimal number into binary number
def convert_to_binary(dec_number):
    binary=[]
    while dec_number > 0:
        remainder=dec_number%2
        dec_number=math.floor(dec_number/2)
        binary.insert(0,remainder)
    binary_string=""
    for digit in binary:
        binary_string=binary_string+str(digit)
    return binary_string

if __name__=="__main__":
    decimal_number=int(input("Enter a decimal number:"))
    print("Binary equivalent of provided number is",convert_to_binary(decimal_number))

