import sys
import numpy as np
import bitarray
from PIL import Image
from progress.bar import IncrementalBar
from colorama import Fore
np.set_printoptions(threshold=sys.maxsize)

def Encode(src, message, dest):
    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n
    bar = IncrementalBar('Encoding', max=height, suffix='%(percent)d%%')

    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print(Fore.RED +"ERROR: Need larger file size")

    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1
            if p % width == 0:
                bar.next()
        bar.finish()
        array=array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        print(Fore.GREEN + "Image Encoded Successfully")

def Decode(src, dest):

    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n
    bar = IncrementalBar('Decoding', max=height, suffix='%(percent)d%%')

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])
        if p % width == 0:
           bar.next()
    bar.finish()

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        message += chr(int(hidden_bits[i], 2))
        if "IEND" in message[-4:]:
            break

    with open(dest, 'wb') as f:
        f.write(bytes(message, 'utf-8'))
        f.close()
    #print(Fore.GREEN + "Hidden Message:" + Fore.RESET, message)

def Reshape(src, dest):
    img = Image.open(src, 'r')
    global width
    global height
    width, height = img.size
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    
    array = np.array(list(img.getdata()))

    global numBlockH
    global numBlockW

    numBlockH = 11
    numBlockW = 5

    global blockW
    global blockH

    blockW = width // numBlockW
    blockH = height // numBlockH

    swap_order = [9, 23, 10, 39, 54,
                  18, 15, 33, 52, 49, 
                  25, 42, 32, 21, 12,
                  35, 34, 40, 29, 45]
    length = len(swap_order)

    global bar

    bar = IncrementalBar('Swapping', max=blockH * blockW * length, suffix='%(percent)d%%')

    for i in range(length):
        array = swap(array, i, swap_order[i])

    bar.finish()

    array=array.reshape(height, width, n)
    reshaped_img = Image.fromarray(array.astype('uint8'), img.mode)
    reshaped_img.save(dest)
    print(Fore.GREEN + "\nImage Reshaped Successfully" + Fore.RESET)
    reshaped_img.show()
    
def swap(array, i, j):

    I = blockH * blockW * numBlockW * (i // numBlockW) + blockW * (i % numBlockW)
    J = blockH * blockW * numBlockW * (j // numBlockW) + blockW * (j % numBlockW)

    tmp = np.array([[0, 0, 0]])
    for k in range(blockH):
        for m in range(blockW):
            tmp[0] = array[I+m]
            array[I+m] = array[J+m]
            array[J+m] = tmp[0]
            bar.next()
        I += width
        J += width

    return array

def Stego():
    global PS
    PS = Fore.BLUE + "$ " + Fore.RESET
    print(Fore.BLUE + "--Welcome to StegLSB--" + Fore.RESET)
    print("1: Encode")
    print("2: Decode")
    print("3: Reshape")

    func = input(PS)

    if func == '1':
        print("Enter Source Image Path")
        src = input(PS)
        print("Enter Message to Hide")
        message = input(PS)
        print("Enter Destination Image Path")
        dest = input(PS)
        Encode(src, message, dest)

    elif func == '2':
        print("Enter Source Image Path")
        src = input(PS)
        print("Enter Destination Image Path")
        dest = input(PS)
        Decode(src, dest)
    elif func == '3':
        print("Enter Source Image Path")
        src = input(PS)
        print("Enter Destination Image Path")
        dest = input(PS)
        Reshape(src, dest)

    else:
        print(Fore.RED + "ERROR: Invalid option chosen"+ Fore.RESET)

''' Stego()'''
Reshape("test1.png", "teaser_2.png")