from PIL import Image
import numpy as np
import random

enc = open("flag.txt", "r").read()
array = []
for out in range(256*256):
    num = ord(enc[out])
    a = random.randrange(1, num)
    num= num-a
    b = random.randrange(0, num)
    num= num-b
    c=num

    e = [a,b,c]
    random.shuffle(e)
    e = tuple(e)
    array.append(e)

arra = open("array.txt", 'w')
print(len(array))
arra.write(str(array))