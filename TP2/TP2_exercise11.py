print("----------WELCOME----------")
binary_number = input("Please enter a 4 digit binary number to be converted to a decimal: ")

decimal_number = int(binary_number[0]) * (2 ** 3) + int(binary_number[1]) * (2 ** 2) + int(binary_number[2]) * (2 ** 1) + int(binary_number[3]) * (2 ** 0)

print("Binary form:", binary_number)
print("Decimal form:", decimal_number)