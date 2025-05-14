#!/usr/bin/python3
def no_c(my_string):
    str_list = []
    for i in my_string:
        if i != 'c' and i != 'C':
            str_list.append(i)
    my_string = ""
    for i in str_list:
        my_string += i
    return my_string
