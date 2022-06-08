#!/usr/bin/python
def multiply_list_map(my_list=[], number=0):
    def multi(a):
        return (a * number)
    return (list(map(multi, my_list)))
