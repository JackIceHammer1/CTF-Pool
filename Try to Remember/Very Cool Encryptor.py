i = 0
iKey = 0
numTotal = 0
num = []
numKey = []
char = []
charKey = []
enc = ""

mes = input("Please input the message you want to encrypt: ")

key = input("Please input a key in ASCII (a-z and numbers from 0-100000): ")
#a-z and 0-100000 are arbitrary btw

keyLis = list(key)

numKey = keyLis
charKey = keyLis

while iKey < len(key):
 numKey[iKey] = ord(keyLis[iKey])
 numTotal = numTotal + numKey[iKey]
 iKey = iKey + 1

enter = input("\nEnter any character to continue \n")

mesLis = list(mes)

num = mesLis
char = mesLis

while i < len(mes):
 num[i] = ord(mesLis[i])
 num[i] = num[i] + numTotal
 char[i] = chr(num[i])
 i = i + 1
enc = ''.join([str(elem) for elem in char])
print(enc)
