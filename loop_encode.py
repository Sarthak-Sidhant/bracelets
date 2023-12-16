def encode_char_to_hex(char):
    # Check if the character is valid
    if not (char.isalnum() or char in '!#$%&()*+,-./:;<=>?@[\\]^_`{|}~ '):
        raise ValueError(f"Invalid character: {char}")

    # Convert character to ASCII value
    ascii_value = ord(char)

    # Convert ASCII value to hexadecimal
    hex_value = hex(ascii_value)[2:].upper()

    if len(hex_value) == 1:
        hex_value = '0' + hex_value

    return hex_value

def encode_string_to_hex(string):
    encoded_hex = ""
    for char in string:
        hex_value = encode_char_to_hex(char)

        # Preserve uppercase for original uppercase characters
        if char.isupper():
            encoded_hex += hex_value.upper()
        else:
            # Convert lowercase to uppercase for original lowercase characters
            if char.islower():
                encoded_hex += hex_value.lower()
            # Preserve special characters
            else:
                encoded_hex += hex_value

    return encoded_hex

string = input("what to encode: ")
encoded_hex = encode_string_to_hex(string)
print(encoded_hex)  # Output: 48656C6C6F2C20576F726C6421402324252628295F2B7B7D2931

for i in range(0,16):
    string=encoded_hex
    encode_string_to_hex(string)
    encoded_hex = encode_string_to_hex(string)

print(encoded_hex)


