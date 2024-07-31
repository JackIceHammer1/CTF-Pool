from PIL import Image
import numpy as np
from ast import literal_eval

img = Image.open("pillow.png").getdata()

message = ""

for i in img:
    message += chr(i[0] + i[1] + i[2])

w = open('solution.txt', 'w')

w.write(message)