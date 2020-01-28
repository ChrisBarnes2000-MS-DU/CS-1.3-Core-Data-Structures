# make change in binary

# Start with highest directly below values we have add lower to meet required value

# given 211
# start with the highest value below it so 128
# then add lower values to we meet it
# possible values being 64, 32, 16, 8, 4, 2, 1

# so we have 128 + 64 + 16 + 2 +1  = 211 or in binary we have 

# 11010011 = 211


# binary_base = [1,2,4,8,16,32,64,128]

def dec_to_binary(val):
    out = ""
    if val > 1:
        dec_to_binary(val)
        out += (val % 2)
        print(out)

if __name__ == "__main__":
    decimal = 7
    print("starting dec: ", decimal)
    print("binary output: ", dec_to_binary(decimal))
