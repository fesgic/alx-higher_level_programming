#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    size = len(sys.argv)
    start = 0
    for i in sys.argv:
        if (start == 0):
            start += 1
            continue
        total += int(i)
    print(total)
