
def offset_genrate():
    num = 0
    for i in range(len(text)):
        x = i % 2
        num += x
    if len(text) % 2 == 0:
        num += 1
    return num

def check_offset():
    flag_len = len(text)
    binary_len = len(binary_result)
    y = binary_len % flag_len
    if y != 0:
        return False
    else:
        return True


def text_to_binary(text, Offset):
    binary_string = ""
    for char in text:
        binary_char = bin(ord(char))[2:]
        formatted_binary_char = binary_char.zfill(Offset)
        binary_string += formatted_binary_char

    return binary_string

text = input("what would you like to convert: ")
num = offset_genrate()
binary_result = text_to_binary(text, num)

print(binary_result)
check_offset()
