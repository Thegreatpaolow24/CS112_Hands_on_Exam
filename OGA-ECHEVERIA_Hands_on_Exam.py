def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:]

def decimal_to_octal(decimal_num):
    return oct(decimal_num)[2:]

def decimal_to_hexadecimal(decimal_num):
    return hex(decimal_num)[2:]

while True:
    try:
        user_input = int(input("Enter 1 to convert to binary, 2 to convert to octal, or 3 to convert to hexadecimal: "))
        if user_input == 1 or user_input == 2 or user_input == 3:
            decimal_num = int(input("Enter a decimal number: "))
            if user_input == 1:
                result = decimal_to_binary(decimal_num)
                print(f"Binary: {result}")
            elif user_input == 2:
                result = decimal_to_octal(decimal_num)
                print(f"Octal: {result}")
            else:
                result = decimal_to_hexadecimal(decimal_num)
                print(f"Hexadecimal: {result}")
            break
        else:
            print("Invalid input. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
