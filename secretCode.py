#!/usr/bin/python

""" 
This is a simple module to convert text into ASCII code
it's a simple shift cipher, nothing to crazy
This module will enable the user to open a text file, read it, and encode each character into a new one and then save that into a new, encoded text file.
"""

def encode(inputFile, offset):
    if not open(inputFile):
        return inputFile, "does not exist!"
    encodedFile=open(inputFile+"."+`offset`+"enc", 'w')
    for line in open(inputFile):
        newLine = ""
        for letter in line:
            if ord(letter)==10:
                newCharNum = 10
            else:
                newCharNum = (((ord(letter)-32)-offset)%95)+32
            newChar = chr(newCharNum)
            newLine += newChar
        encodedFile.write(newLine)
    encodedFile.close()


def readEncoded(encodedFile, offset):
    readit = ""
    if not open(encodedFile):
        return encodedFile, "does not exist!"
    for line in open(encodedFile, 'r'):
        newLine = ""
        for letter in line:
            if ord(letter)==10:
                newCharNum = 10
            else:
                newCharNum = (((ord(letter)-32)+offset)%95)+32
            newChar = chr(newCharNum)
            newLine += newChar
        readit += newLine
    print readit

    
 
