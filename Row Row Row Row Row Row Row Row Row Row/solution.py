from PIL import Image
import numpy as np
import random
from ast import literal_eval
import math

image = Image.open('rows.png')

a = np.asarray(image)

for i in a:
    print(chr(i[0][0]), end='')