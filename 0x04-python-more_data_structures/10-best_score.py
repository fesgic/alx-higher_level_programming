#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None):
        return (None)
    if (len(a_dictionary) == 0):
        return (None)
    for k in a_dictionary:
        new = a_dictionary[k]
        track = k
        break
    for k in a_dictionary:
        if a_dictionary[k] > new:
            new = a_dictionary[k]
            track = k
    return (track)
