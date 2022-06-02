#!/usr/bin/python3
import sys

if __name__ == "__main__":
    length = len(sys.argv)
    if (length == 1):
        print("{:d} arguments.".format(length - 1))
    else:
        if (length == 2):
            print("{:d} argument:".format(length - 1))
            print("{:d}: {:s}".format(length - 1, sys.argv[length - 1]))
        else:
            print("{:d} arguments:".format(length - 1))
            i = 1
            while (i < length):
                print("{:d}: {:s}".format(i, sys.argv[i]))
                i += 1
