import random
n=random.randint(40,60)
ss=random.randint(4,6)
location=random.randint(0,n-6)
secret="mdwmnaknap"
nrun=n//10 #tens
modn=n%10 #ones
count=0
for i in range(nrun+1):
    for j in range(10):
        if i==0:
            print(" ",end="")
        elif i<nrun:
            print(count,end="")
    count=count+1
for p in range(modn+1):
    print(nrun,end="")
print()
count2=0
for i in range(nrun):
    for i in range(10):
        print(i,end="")
for m in range(modn+1):
    if m<=modn:
        print(count2,end="")
        count2=count2+1
print("")

ocean=[]
for d in range(n+1):
    ocean.append("o")
for w in range(ss):
    ocean[location+w]="x"


hyphen=[]
for z in range(n+1):
    hyphen.append("-")
print("".join(str(x) for x in hyphen))

attempt=10
def gameWriteOut(key, string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in string:
        if letter in alphabet:
            letter_index = (alphabet.find(letter) - key) % len(alphabet)
            result = result + alphabet[letter_index]
        else:
            result = result + letter
    return "lbctf{"+result+"}"
while attempt>0 and hyphen.count("x")!=ss:
    choice=int(input("guess? "))
    if choice<=n:
        if ocean[choice]=="x":
            attempt=attempt-1
            hyphen[choice]="x"
            print("".join(str(x) for x in hyphen))
            print("Guesses left: "+str(attempt))
        else:
            hyphen[choice]="o"
            attempt=attempt-1
            print("".join(str(x) for x in hyphen))
            print("Guesses left: "+str(attempt))
    else:
        print("Out of range")
        choice=int(input("guess? "))
if hyphen.count("x")==ss:
    print("Winner!")
    print(gameWriteOut(9,secret))
else:
    print("Loser!")





  

