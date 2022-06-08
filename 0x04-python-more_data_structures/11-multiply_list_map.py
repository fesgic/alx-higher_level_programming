#!/usr/bin/python
def multiply_list_map(my_list=[], number=0):
    return (list(map(lambda x, number : x * number if len(my_list) != 0, my_list)))
