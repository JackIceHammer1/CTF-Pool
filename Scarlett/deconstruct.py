import sympy
import numpy as np
word = input("Enter your phrase to be encrypted: ")
keys = input("Enter your one letter key: ")
phrase = list(word)
key = ord(keys)
x = sympy.Symbol('x')
f = 23 * x
ke = int(key) * int(sympy.diff(f, x))
pase = []
ke = bool(ke) * np.exp(1)
i=1
p = len(word)
while i < p:
    pase.append((ord(phrase[i]))*ke+71.9)
    i = i+1

print(pase)
input()