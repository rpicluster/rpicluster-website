# purpose: find the magic string in the image file and concatenate a string to it.

import sys, os
import zipfile
import fnmatch
import os

network_name = raw_input("Enter a network name: ")
password = raw_input("Enter a password: ")
network_name = ''.join(format(ord(x), 'b') for x in network_name)
password = ''.join(format(ord(x), 'b') for x in password)
len_network = len(network_name)
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

    null = fd.read(16)
    null += fd.read(len_network)
    null += fd.read(len_pass) # need to offset by the size of the string
    second += fd.read()
    return (first, second)

def write_img(img):
    parts = find_point("0100010001000001010101110100000101000101", img)
    fd = open(img, 'wb')
    fd.write(parts[0])
    fd.write("{0:08b}".format(len_network))
    fd.write("{0:08b}".format(len_pass))
    fd.write(network_name)
    fd.write(password)
    fd.write(parts[1])
    fd.close()

def find_img_files():
    img_files = []

    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.zip'):
            zip_ref = zipfile.ZipFile("Server.zip", 'r')
            zip_ref.extractall(".")
            zip_ref.close()

    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.img'):
            img_files.append(file)

    write_img(img_files[0])
    write_img(img_files[1])


find_img_files()
