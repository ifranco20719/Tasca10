def bin_to_dec(binary):
    return int(binary, 2)

def list_bin_to_dec(list_binary):
    list_decimal = []
    for bin_num in list_binary:
        list_decimal.append(bin_to_dec(bin_num))
    return list_decimal

# Main program
a = ["11111", "1101", "1010", "1000"]
b = list_bin_to_dec(a)
for i, dec in enumerate(b):
    print("The binary number:", a[i], "corresponds to the decimal number:", dec)
