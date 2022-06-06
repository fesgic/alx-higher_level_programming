#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy = []
    for i in my_list:
        copy.append(i)
    if (idx < 0):
        return (copy)
    elif (idx >= len(my_list)):
        return (copy)
    else:
        copy[idx] = element
        return (copy)
