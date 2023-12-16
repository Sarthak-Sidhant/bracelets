import tkinter as tk
def encode_char_to_hex(char):
    # Check if the character is valid
    if not (char.isalnum() or char in "'!#$%&()*+,-./:;<=>?@[\\]^_`{|}~ " or char in '"'):
        raise ValueError(f"Invalid character: {char}")

    # Convert character to ASCII value
    ascii_value = ord(char)

    # Convert ASCII value to hexadecimal
    hex_value = hex(ascii_value)[2:].upper()

    if len(hex_value) == 1:
        hex_value = '0' + hex_value

    return hex_value

def decode_hex_to_char(hex_value):
    # Check if the hexadecimal value is valid
    if not hex_value.isalnum():
        raise ValueError(f"Invalid hexadecimal value: {hex_value}")

    # Convert hexadecimal value to integer
    ascii_value = int(hex_value, 16)

    # Convert ASCII value to character
    char = chr(ascii_value)

    return char

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

# Example usage with case sensitivity and special characters
string = input("what to code, what to decode: ")
encoded_hex = encode_string_to_hex(string)
print(encoded_hex)  # Output: 48656C6C6F2C20576F726C6421402324252628295F2B7B7D2931
decoded_string = decode_hex_to_string(encoded_hex)
print(decoded_string)  # Output: Hello, World!

def hex_to_color_and_emoji(hex_value):
    emoji_mapping = {
        "0": ("black", "😎"), #
        "1": ("blue", "🥰"),
        "2": ("green", "😐"),
        "3": ("aqua", "😏"),
        "4": ("red", "😒"),
        "5": ("purple", "😭"),
        "6": ("yellow", "😱"),
        "7": ("#fefefe", "💀"),
        "8": ("gray", "🤖"),
        "9": ("#ADD8E6", "💖"),
        "a": ("#90EE90", "✨"),
        "b": ("#ddfcf7", "😂"),
        "c": ("#FF7F7F", "👀"),
        "d": ("#CBC3E3", "👽"),
        "e": ("#FFFFED", "💩"),
        "f": ("#ffffff", "🤓"),
        "A": ("#90EE90", "✨"),
        "B": ("#ddfcf7", "😂"),
        "C": ("#FF7F7F", "👀"),
        "D": ("#CBC3E3", "👽"),
        "E": ("#FFFFED", "💩"),
        "F": ("#ffffff", "🤓"),
    }
    return emoji_mapping[hex_value]

def display_hex_beads(hex_string):
    # Create the main window
    root = tk.Tk()
    root.title("Hex Bead Display")

    # Create a frame to hold the beads and emojis
    bead_frame = tk.Frame(root)
    bead_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Initialize row and column counters
    row = 0
    column = 0

    # Iterate over the hex characters and create corresponding beads and emojis
    for i, hex_value in enumerate(hex_string):
        color, emoji = hex_to_color_and_emoji(hex_value)

        # Create a label for the bead with emoji as text
        bead_label = tk.Label(bead_frame, text=emoji, background=color, width=2, height=2)

        # Check if a new row is needed
        if column % 50 == 0:
            row += 1
            column = 0

        # Place the bead label in the grid
        bead_label.grid(row=row, column=column, padx=2, pady=2)

        # Increment the column counter
        column += 1

    # Start the main event loop
    root.mainloop()

# Example usage

display_hex_beads(encoded_hex)
