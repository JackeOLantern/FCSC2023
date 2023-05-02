from PIL import Image
from string import digits, ascii_uppercase, ascii_lowercase
alphabet = digits + ascii_uppercase + ascii_lowercase

def convert(imgfile):
    image = Image.open(imgfile)
    im = image.load()
    border = 25
    xstart = 55#border + int(15 * ratio_x)
    ystart = 50#border + int(20 * ratio_y)
    xoff = 11#int(7 * ratio_x)
    yoff = 32# int(20 * ratio_y)
    allpunches = []
    countx = 0
    offsetx = 0
    for x in range(xstart,image.size[0]- border,xoff):
        #print(" ("+str(x)+", y)")
        punches = []
        if countx % 9 == 0: 
            offsetx = offsetx + 1
        for y in range(ystart,image.size[1]- border,yoff):
            if (countx > 129 and countx < 35):
                print(" ("+str(x-offsetx)+", "+str(y)+") = "+str(im[x-offsetx,y]))
            if im[x-offsetx,y][1] > 80:
                punches.append(int((y-ystart)/yoff))
        if (countx > 129 and countx < 35):
            print(" -> punches("+str(punches))
        allpunches.append(punches)
        countx = countx + 1
    return allpunches

def readpunch(p):
    #print("* "+str(p))
    if len(p) > 2:
        if p == [2,5,10]: return ','
        if p == [0,5,10]: return '.'
        if p == [2,9,10]: return '?'
        if p == [0,7,10]: return '('
        if p == [1,7,10]: return ')'
        if p == [1,4,10]: return '!'
        if p == [2,7,10]: return '_'
        if p == [0,8,10]: return '+'
        if p == [1,6,10]: return '*'
        if p == [0,5,10]: return '*'
        if p == [0,6,10]: return '<'
        if p == [0,7,10]: return '>'

    if p == [0]: return '&'
    if p == [1]: return '-'

    if p == [4, 10]: return ':'
    if p == [5, 10]: return '#'
    if p == [7,10]: return '\\'
    if p == [8,10]: return '='
    if p == [9,10]: return '"'
    if p == [2,3]: return '/'

    if len(p) == 0:
        return ' '
    if len(p) == 1 and p[0] >=2:
        return alphabet[p[0]-2] # digits
    
    if len(p) == 2:
        if p[0] == 0 and p[1] >=3 :
            return alphabet[7+p[1]] #A -> I
        elif p[0] == 1 and p[1] >=3:
            return alphabet[16+p[1]]# J -> R
        elif p[0] == 2 and p[1] >=3:
            return alphabet[24+p[1]]# S - > Z
    if len(p) == 3: #lowercase
        if p[0] == 0 and p[1] == 2 and p[2] >=3:
            return alphabet[32+p[2]] #a -> i
        if p[0] == 0 and p[1] == 1  and p[2] >=3:
            return alphabet[40+p[2]]# j -> r
        elif p[0] == 1 and p[1] == 2  and p[2] >=3:
            return alphabet[48+p[2]]# s - > z


    print(" * "+str(p))
    return '_'
files = []

for i in range (1, 10):
    files.append("cards/000000000"+str(i)+".jpg")
for i in range (10, 80):
    files.append("cards/00000000"+str(i)+".jpg")

for f in files:
    q = (''.join([readpunch(p) for p in convert(f)]))
    print(q)