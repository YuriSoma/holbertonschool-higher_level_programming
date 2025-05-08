#!/usr/bin/python3
for asciiCode in range(97, 123):
    if chr(asciiCode) is not 'q' and chr(asciiCode) is not 'e':
        print("{}".format(chr(asciiCode)), end="")
