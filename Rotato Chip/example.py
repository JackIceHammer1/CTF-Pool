user_input = input("Enter the string to encode: ")
length = len(user_input)

for i in range(length):
    if ((65 <= ord(user_input[i]) <= 77) or (97 <= ord(user_input[i]) <= 109)):
        user_input[i] = chr(ord(user_input[i]) + 13)
    elif ((78 <= ord(user_input[i]) <= 90) or (110 <= ord(user_input[i]) <= 122)):
        user_input[i] = chr(ord(user_input[i]) - 13)

print(user_input)
