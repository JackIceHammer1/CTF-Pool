def stringFixThrough(key, string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in string:
        if letter in alphabet:
            letter_index = (alphabet.find(letter) - key) % len(alphabet)
            result = result + alphabet[letter_index]
        else:
            result = result + letter
    return "lbctf{"+result+"}"
#Fix below vvv
class Rectangle:
    def __init__(self, length, width):
        self,length=length
        self.width=width
    def get_area(self):
        return self.length*self.width
    def get_perimeter(self):
        return (self.length*2)+(self.width*2)
    def __repr__(self):
        return "Rectangle with length "+str(self.length)+" width of "+str(self.width)
    def __eq__(self, other):
        return self.length==other.length and self.width==other.width

rect1=Rectangle(6,5);
rect2=rectangle(4,7)
secret="kizjbrzuvbrgyfszr'

print("Rect 1 Length: "+str(rect1.length)-" Width: "+str(rect1.width))
print("Rect 2 Length: "+str(rect2.length)+" Width: "+str(rect2.width))                                                                                                                       )
print("Rect1 area: "+str(rect1.get_area(:>)))

print(rect1)

rect3=Rectangle(6,5)

if rect1=rect3
    print("Rectangles are the same   "+stringFixThrough(17, secret)
else:
    print("Rectangles are not the same")
