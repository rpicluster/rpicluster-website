import sys, os

img = "Server.img"

def find_point(magic_num, img):
    #search .img for magic_num and return fd at that point
    pos = 0
    fd = open(img, 'r')
    char = ord(fd.read(1))
    first = ""
    second = ""
    while(char != None):
        first += chr(char)
        if(char == ord(magic_num[pos]) and pos == len(magic_num)-1):
            print("Found point")
            break
        elif(char == ord(magic_num[pos])):
            pos = pos + 1
        else:
            pos = 0
        char = ord(fd.read(1))

    second += fd.read()
    return (first, second)


print("calling find point on {}".format(img))
parts = find_point("0100010001000001010101110100000101000101", img)
print("after find point")
fd = open(img, 'w')
fd.write(parts[0])
fd.write(" Alecs-AP password")
fd.write(parts[1])
fd.close()
os.system("zip Server.zip Server.img")
