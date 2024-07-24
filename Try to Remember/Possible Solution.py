i = 0
e = 65
sub = 0
mem = 0
num = []
char = []
charArr = []
lis = []
enc = ""

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += str(ele)
    return str1

mes = input("Please input the message you want to decrypt: ")

mesLis = list(str(mes))


num = mesLis
char = mesLis

print(mesLis)

while e < 128:
  num[i] = ord(mesLis[i])
  if i == 0:
    sub = num[i] - e
  num[i] = num[i] - sub
  if num[i] < 0:
    mesLis = list(str(mes))
    num = mesLis
    i = -1
    e = e + 1
  else:
    char[i] = chr(num[i])
    if i == len(mes) - 1:
      mesLis = list(str(mes))
      num = mesLis
      i = -1
      e = e + 1
      print("Possible message: ",listToString(char))
  i = i + 1