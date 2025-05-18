#!/usr/bin/python3
def roman_to_int(roman_string):
    str_list = list(roman_string)
    converted_count = 0
    for i in range(len(str_list)):
        if str_list[i] == 'M':
            if i != 0 and str_list[i - 1] == 'C':
                converted_count += 800
            else:
                converted_count += 1000
        elif str_list[i] == 'D':
            if i != 0 and str_list[i - 1] == 'C':
                converted_count += 300
            else:
                converted_count += 500
        elif str_list[i] == 'L':
            if i != 0 and str_list[i - 1] == 'X':
                converted_count += 30
            else:
                converted_count += 50
        elif str_list[i] == 'V':
            if i != 0 and str_list[i - 1] == 'I':
                converted_count += 3
            else:
                converted_count += 5
        elif str_list[i] == 'C':
            if i != 0 and str_list[i - 1] == 'X':
                converted_count += 80
            else:
                converted_count += 100
        elif str_list[i] == 'X':
            if i != 0 and str_list[i - 1] == 'I':
                converted_count += 8
            else:
                converted_count += 10
        elif str_list[i] == 'I':
            converted_count += 1
    return converted_count
print(roman_to_int("IV"))
