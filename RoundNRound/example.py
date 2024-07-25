def shift_string(input_string):
    output_string = ""
    for i in range(1,len(input_string)+1):
        char = input_string[i-1]
        shifted_char = chr((ord(char) - ord('a') + i) % 26 + ord('a'))
        output_string += shifted_char
    return output_string

input_string = input("Enter a string to shift: ")
output_string = shift_string(input_string)
print("Shifted string: " + output_string)
