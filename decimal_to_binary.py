#!/bin/python
# convert a decimal value into signed 64 bit binary
import math
import sys

ZERO_BINARY_LIST = list('0000000000000000000000000000000000000000000000000000000000000000')

def decimal_to_binary(decimal, binary_list):
    #########################################
    # Procedure:                            #   
    # find nearest power of 2 to decimal    #
    # flip that bit in the binary string    #
    # subtract that power of 2 from decimal #
    #########################################
    
    if decimal == 0:
        # reverse list since everything is backwards right now
        binary_list = binary_list[::-1]
        binary_str = ''.join(binary_list)
        return binary_str
    if decimal < 0:
        binary_list[63] = '1'
        decimal *= -1
    else:
        power = nearest_power(decimal)
        if power > 63:
            return None
        binary_list[power] = '1'
        decimal -= (2**power)
    
    return decimal_to_binary(decimal, binary_list)
    
def nearest_power(decimal):
    return int(math.floor(math.log(decimal, 2)))

# handle arg parsing
def main():
    if len(sys.argv) < 1:
        print('No decimal value provided')
        sys.exit(1)
    try:
        dec = int(sys.argv[1])
    except ValueError:
        print('Argument should be a decimal value not {}'.format(sys.argv[1]))
    binary_result = decimal_to_binary(dec, ZERO_BINARY_LIST)
    if binary_result == None:
        print('{} is too large'.format(dec))
        sys.exit(1)
    print('{} in binary is {}'.format(dec, binary_result))
    

if __name__ == '__main__':
    main()