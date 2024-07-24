from PIL import Image
import numpy as np
import random
from ast import literal_eval
import math

flag = "lbctf{im_gonna_make_this_way_too_long_to_do_manually}"

array = []

print(len(flag))

for out in range(1, (10*len(flag))+1):
    print(math.ceil(out/10)-1)
    letter = flag[math.ceil(out/10)-1]
    e = [ord(letter), 254, 254]
    e = tuple(e)
    array.append(e)



arr = array
arr = literal_eval(arr)

print(len(arr))

im = Image.new('RGB', [10,len(flag)])    

im.putdata(arr)

im.save('rows.png')