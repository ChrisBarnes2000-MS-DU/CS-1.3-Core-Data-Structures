# make change in binary

# Start with highest directly below values we have add lower to meet required value

# given 211
# start with the highest value below it so 128
# then add lower values to we meet it
# possible values being 64, 32, 16, 8, 4, 2, 1

# so we have 128 + 64 + 16 + 2 +1  = 211 or in binary we have 

# 11010011 = 211


# binary_base = [1,2,4,8,16,32,64,128]




# Function to print binary number for the
# input decimal using recursion
def decimalToBinary(n):
    if(n > 1):
        # divide with integral result
        # (discard remainder)
        decimalToBinary(n//2)
    print(n % 2, end=' ')

# Function calculates the decimal equivalent
# to given binary number
def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)

# Driver code
if __name__ == '__main__':
    print('7 in binary: \t', end=' ')
    decimalToBinary(7)
    print('\n8 in binary: \t', end=' ')
    decimalToBinary(8)
    print("\n18 in binary: \t", end=' ')
    decimalToBinary(18)

    print()

    print('100 in decimal: \t', end=' ')
    binaryToDecimal(100)
    print('101 in decimal: \t', end=' ')
    binaryToDecimal(101)
    print('1001 in decimal: \t', end=' ')
    binaryToDecimal(1001)
