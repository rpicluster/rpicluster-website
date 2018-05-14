# purpose: find the magic string in the image file and concatenate a string to it.

import sys, os
import zipfile

zip_ref = zipfile.ZipFile("Server.zip", 'r')
zip_ref.extractall(".")
zip_ref.close()
img = "Server.img"
# img = "testing"

network_name = raw_input("Enter a network name: ")
password = raw_input("Enter a password: ")
network_name = ''.join(format(ord(x), 'b') for x in network_name)
len_network = len(network_name)
password = ''.join(format(ord(x), 'b') for x in password)
len_pass = len(password)

def find_point(magic_num, img):
    pos = 0
    fd = open(img, 'rb')
    char = ord(fd.read(1))
    first = "" # first is the first half of the image, including the magic number
    second = "" # second is the second half.
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

    null = fd.read(len_network)
    null += fd.read(len_pass) # need to offset by the size of the string
    second += fd.read()
    return (first, second)


print("Calling find point on {}".format(img))
parts = find_point("0100010001000001010101110100000101000101", img)
print("After find point")

fd = open(img, 'wb')
print("writing first part of image")
fd.write(parts[0])
print("writing network name and password concatenate to magic string")
# fd.write("{0:08b}".format(len_network))
# fd.write("{0:08b}".format(len_pass))
fd.write(network_name)
fd.write(password)
print("writing second part of image")
fd.write(parts[1])
print("Finished writing")
fd.close()
