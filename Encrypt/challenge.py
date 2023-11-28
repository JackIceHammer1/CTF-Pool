

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele   
    return str1 

def encrypt():
    i=0
    word = input("Enter your phrase to be encrypted: ")
    keys = input("Enter your one letter key: ")
    phrase = list(word)
    key = ord(keys)
    ke = int(key)
    pase = []
    
    p = len(word)
    while i < p:
        pase.append((ord(phrase[i]))*ke+47)
        i = i+1

    print(pase)
    input()

def decrypt():
    a = 0
    l = 0
    j = 0
    h = 0
    b = 0
    dphrase = [11880, 10780, 10890, 12760, 11220, 13530, 12320, 13310, 12760, 11440, 12210, 12100, 10450, 12540, 11110, 12980, 5610, 12540, 12650, 11110, 10450, 10890, 5280, 11000, 11110, 13750]
    lp = len(dphrase)
    dkey = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lk = len(dkey)
    flag = []
    dke = []
    
    while l < lk:
        dke.append(ord(dkey[l]))
        l = l+1
    
    while h < lk:
        while a < lp:
            flag.append(chr(int((dphrase[a]-47)/dke[b])))
            a = a +1
    
        a = 0
        b = b+1
        print(listToString(flag))
        print("\n")
        flag = []
    input()

while True:
    option = input("Decrypt or Encrypt?: ")
    if option == "Decrypt":
        decrypt()
    elif option == "Encrypt":
        encrypt()
    else:
        print("Invalid")
