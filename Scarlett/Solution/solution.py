import sympy
import numpy as np
encrypted_message = eval(input("Enter the encrypted message: "))
keys = input("Enter your one letter key: ")
key = ord(keys)
x = sympy.Symbol('x')
f = 23 * x
ke = int(key) * int(sympy.diff(f, x))
ke = bool(ke) * np.exp(1)
decrypted_message = []
for encrypted_char in encrypted_message:
    decrypted_char = int((encrypted_char - 71.9) / ke)
    decrypted_message.append(chr(decrypted_char))
decrypted_message = ''.join(decrypted_message)
print("Decrypted message:", decrypted_message)