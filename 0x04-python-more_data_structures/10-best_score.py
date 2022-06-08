#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary == None):
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
