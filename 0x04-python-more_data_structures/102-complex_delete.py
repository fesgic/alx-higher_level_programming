#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        delete = []
        for k in a_dictionary:
            if a_dictionary[k] == value:
                delete.append(k)
        for i in delete:
            del a_dictionary[i]

    return (a_dictionary)
