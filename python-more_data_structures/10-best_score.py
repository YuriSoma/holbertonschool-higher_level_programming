#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = ''
    max_score = 0
    if not a_dictionary:
        return None
    else:
        keys_list = list(a_dictionary)
        for i in keys_list:
            if a_dictionary[i] > max_score:
                max_score = a_dictionary[i]
                best_score = i
    return best_score
