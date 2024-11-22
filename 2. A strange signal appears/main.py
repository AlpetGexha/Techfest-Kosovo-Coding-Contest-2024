input = open("input.txt", "r").read()

def bits_key(hex_str):
    ones = 0;
    zeros = 0;

    for i in range(0, len(hex_str)):
        binary = bin(int(hex_str[i], 16))[2:].zfill(4) # 0010
        binary =  binary.lstrip('0') # 10 
        # print(binary)

        for j in range(0, len(binary)):
            if binary[j] == '1':
                ones += 1
            else:
                zeros += 1


    return ones * zeros


key = bits_key(input)
print(key)
