#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) >= ord('a') and ord(i) <= ord('z')):
            print("{:s}".format(chr(ord('A') + ord(i) - ord('a'))), end="")
        else:
            print("{:s}".format(i), end="")
    print("")
