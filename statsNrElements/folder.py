import os

def loopDir(dirname, prefix) :
    files = os.listdir(dirname)
    for file in files :
        if os.path.isdir(file):
            print(prefix,file)
            loopDir(file, prefix + '  ')
        else:
            print(prefix+file)

loopDir('./', "")