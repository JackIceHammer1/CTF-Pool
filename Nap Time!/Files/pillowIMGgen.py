from PIL import Image
import numpy as np
import random
from ast import literal_eval

arr = open("array.txt").read()
arr = literal_eval(arr)

print(len(arr))

im = Image.new('RGB', [256,256])    

im.putdata(arr)

im.save('pillow.png')