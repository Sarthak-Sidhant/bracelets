def decode_hex_to_char(hex_value):
    # Check if the hexadecimal value is valid
    if not hex_value.isalnum():
        raise ValueError(f"Invalid hexadecimal value: {hex_value}")

    # Convert hexadecimal value to integer
    ascii_value = int(hex_value, 16)

    # Convert ASCII value to character
    char = chr(ascii_value)

    return char


def decode_hex_to_string(hex_string):
    decoded_string = ""
    for i in range(0, len(hex_string), 2):
        hex_value = hex_string[i:i+2]
        char = decode_hex_to_char(hex_value)

        # Keep uppercase for original uppercase characters
        if hex_value.isupper():
            decoded_string += char.upper()
        else:
            # Keep lowercase for original lowercase characters
            if hex_value.islower():
                decoded_string += char
            # Preserve special characters
            else:
                decoded_string += char

    return decoded_string

string = input("what to code, what to decode: ")
decoded_string = decode_hex_to_string(string)
print(decoded_string)  # Output: Hello, World!
