def binary_to_text(binary_string):
    binary_values = binary_string.split()
    ascii_characters = [chr(int(b, 2)) for b in binary_values]
    return ''.join(ascii_characters)

# Maybe the stuff from the pixel file goes here?
binary_string = " "

decoded_flag = binary_to_text(binary_string)
print(f"Flag: {decoded_flag}")
