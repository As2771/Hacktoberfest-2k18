#!/bin/python
# convert a decimal value into signed 64 bit binary
import math
import sys

ZERO_BINARY_STRING = list('0000000000000000000000000000000000000000000000000000000000000000')

def decimal_to_binary(decimal, binary_string):
    #########################################
    # Procedure:                            #   
    # find nearest power of 2 to decimal    #
    # flip that bit in the binary string    #
    # subtract that power of 2 from decimal #
    #########################################
    
    if decimal == 0:
        return ''.join(reversed(str(binary_string)))
    if decimal < 0:
        binary_string[63] = '1'
        decimal *= -1
    else:
        power_of_two = nearest_power_of_two(decimal)
        print(power_of_two)
        if power_of_two > 63:
            return None
        binary_string[power_of_two - 1] = '1'
        
        decimal -= power_of_two
    
    decimal_to_binary(decimal, binary_string)
    
def nearest_power_of_two(decimal):
    return int((2**(math.ceil(math.log(decimal, 2))))/2)

# handle arg parsing
def main():
    if len(sys.argv) < 1:
        print('No decimal value provided')
        exit(1)
    try:
        dec = int(sys.argv[1])
    except ValueError:
        print('Argument should be a decimal value not {}'.format(sys.argv[1]))
    binary_result = decimal_to_binary(dec, ZERO_BINARY_STRING)
    print('{} in binary is {}'.format(dec, binary_result))
    

if __name__ == '__main__':
    main()