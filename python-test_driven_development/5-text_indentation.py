#!/usr/bin/python3
""" function that prints:
    a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    The function will get 1 input, text (Some string),
    then prints text with 2 lines after each ., ? and :

    If "text" is not string:
    it will raise a TypeError if an input is not string.
    Function shouldn't prints spaces at the beginning or at the end.
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
