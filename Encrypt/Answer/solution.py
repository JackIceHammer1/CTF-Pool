i=0
l = 0
j = 0
h = 0
b = 0

phrase = [6581, 6944, 12389, 13478, 14204, 13841, 14083, 14446, 12268, 13357, 14083, 14688]
lp = len(phrase)
key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lk = len(key)
flag = []
ke = []

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele   
    return str1 

while l < lk:
    ke.append(ord(key[l]))
    l = l+1

while h < lk:
    while i < lp:
        flag.append(chr(int(phrase[i]/ke[b])))
        i = i +1

    i = 0
    b = b+1
    print(listToString(flag))
    print("\n")
    flag = []
input()
