import numpy as np
from PIL import Image
import bitarray

def Encode(src, message, dest):

    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4   
    total_pixels = array.size//n

    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print("ERROR: Need larger file size")

    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        array=array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        print("Image Encoded Successfully")

def Decode(src):

    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4   
    total_pixels = array.size//n
    print("  image mode / pixels", img.mode, total_pixels)
    posx = 0
    posy = 0
    with open("resu3.png", 'wb') as f:
        #,(2,9),(3,7)
        #for (posx, posy) in [(4,7), (2,7), (2,6), (1,7), (4,4), (1,4),(0,8), (0,0), (3,10),(4,9),(1,6),(1,10),(4,10), (1,8), (2,8), (2,1),(2,2),(0,2),(0,2),(3,8),(4,5),(2,4),(3,9),(2,9),(3,7)]:
        hidden_bits = ""
        '''       for (posx, posy) in [(4,7), (2,7), (2,6), (1,7), (4,4), 
                             (4,9), (3,10), (0,0), (0,8), (1,4),
                             (1,6), (1,10),(4,10), (1,8), (2,8),
                             (3,8), (2,0), (0,2), (2,2), (2,1),
                             (4,5), (2,4), (3,9)]:
        
                       Nico  (1,4), (0,8), (0,0), (3,10), (4,9), 
                             (1,6), (1,10),(4,10), (1,8), (2,8),
                             (2,1), (2,2), (0,2), (0,2), (3,8),
                             (4,5), (2,4), (3,9), (2,9), (3,7)
                             ]:

                             [(4,7), (1,4), (1,6), (2,1), (4,5), 
                             (2,4), (2,2), (1,10), (0,8), (2,7),
                             (2,6), (0,0),(4,10), (0,2), (2,0),
                             (1,8), (3,10), (1,7), (4,4), (4,9),
                             (2,8), (3,8), (3,7), (2,9), (3,9)]:

                             [(4,7), (1,4), (1,6), (2,1), (4,5), 
                             (4,4), (4,9), (2,8), (3,8), (3,7),
                             (2,7), (0,8),(1,10), (0,2), (2,4),
                             (1,7), (3,10), (1,8), (2,0), (2,9),
                             (2,6), (0,0), (4,10), (2,2), (3,9)]:
                             '''
        for (posx, posy) in [(4,7), (1,4), (1,6), (2,1), (4,5), 
                             (2,4), (2,2), (1,10), (0,8), (2,7),
                             (2,0),(1,8), (4,10), (1,10), (1,6),
                             (2,6), (0,0), (3,9)]:
            print(posx, posy)
            row = 0
            col = 0
            count = 0
            for p in range(total_pixels):
                if col >= posx * (width / 5) and col < (posx +1) * (width / 5) and row >= posy *  (height / 11) and row < (posy+1) *  (height / 11) :
                    count= count+1
                    for q in range(0, 3):
                        hidden_bits += (bin(array[p][q])[2:][-1])
                col = col + 1
                if col == width:
                    col = 0
                    row = row + 1
        print(len(hidden_bits), (len(hidden_bits) % 8))
        f.write(bitstring_to_bytes2(hidden_bits))
        
'''
    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]
    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "FCSC{":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        print("Hidden Message:", message[:-5])
    else:
        print("No Hidden Message Found: ")
'''
def bitstring_to_bytes2(s):
    return bitarray.bitarray(s).tobytes()

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

def Stego():
    print("--Welcome to $t3g0--")
    print("1: Encode")
    print("2: Decode")

    func = input()

    if func == '1':
        print("Enter Source Image Path")
        src = input()
        print("Enter Message to Hide")
        message = input()
        print("Enter Destination Image Path")
        dest = input()
        print("Encoding...")
        Encode(src, message, dest)

    elif func == '2':
        print("Enter Source Image Path")
        src = input()
        print("Decoding...")
        Decode(src)

    else:
        print("ERROR: Invalid option chosen")

def StegoFast():
    print("Decoding...")
    Decode("C:/dev/FCSC_2023/01_teaser/teaser.png")

StegoFast()