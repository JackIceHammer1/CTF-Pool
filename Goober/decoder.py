password_file = "pw.goober"
flag_file = "flag.goober"

with open(password_file, "r") as file:
    password = file.read().strip()

with open(flag_file, "r") as file:
    encoded_flag = file.read()

def decode_flag(encoded_flag, password):
    flag = ""
    for i in range(len(encoded_flag)):
        char = encoded_flag[i]
        password_char = password[i % len(password)]
        decoded_char = chr(ord(char) ^ ord(password_char))
        flag += decoded_char
    return flag

decoded_flag = decode_flag(encoded_flag, password)
print(decoded_flag)