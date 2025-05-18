#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    tmp_set = list(set(my_list))
    for i in range(len(tmp_set)):
        result += tmp_set[i]
    return result
