import os
import sys

path = sys.argv[1]

print(path)
os.chdir(path)
count = 0

def fileNames(filepath):
    global count
    for files in sorted(os.listdir(filepath)):
        if not os.path.isdir(os.path.join(filepath, files)):
            print(" "*count*2, "\033[1;37;40m |-> "+f"\033[1;37;40m{files}")
        if os.path.isdir(os.path.join(filepath, files)):
            print(" "*count*2, "\033[1;37;40m |-"+f"\033[1;32;40m{files}")
            count += 1
            fileNames(os.path.join(filepath, files))
    count -= 1

for files in sorted(os.listdir()):
    newPath = os.path.join(path, files)

    if not os.path.isdir(newPath):
        print("\033[1;37;40m|-"+files)
    if os.path.isdir(newPath):
        print("\033[1;32;40m|-"+files)
        fileNames(newPath)