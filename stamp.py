import zipfile, sys

magic_num = sys.argv[1]
file = sys.argv[2]

def find_point(magic_num, img):
    #search .img for magic_num
    pos = 0
    fd = open(img, 'r+')
    char = fd.read('1')
    while(char):
        #may need to read  char by char to find the exact string then return fd at that char then write
        if(pos == len(magic_num)):
            return fd
        elif(char == magic_num[pos]):
            pos = pos + 1
        else:
            pos = 0
        char = fd.read('1')
    return fd




zip_ref = zipfile.ZipFile(file, 'r')
zip_ref.extractall(".")
split = file.split('.')
img = split[0] + ".img"
fd = find_point(magic_num, img)


fd.close()
zip_ref.close()