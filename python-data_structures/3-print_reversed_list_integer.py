#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list) - 1
    for i in my_list:
        print("{:d}".format(my_list[length]))
        length -= 1
print_reversed_list_integer([1,2,3,7])
