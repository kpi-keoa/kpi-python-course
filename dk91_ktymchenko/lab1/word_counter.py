#!/usr/bin/python 3

import os

'''This function search all the words in the file'''

def allWords(fileName):
 
	with open(fileName, encoding="utf8") as file:
		readFile = file.read()
	noLineBreak = readFile.replace("\n", " ")
	noPunctuation = noLineBreak.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
	text = noPunctuation.lower()
	words = text.split()
	return words

'''The main function contains
    - inputting the file path
    - calling the allWords defined functions
    - outputting all statistics
'''

def result():
        fileName = input("Specify the file path: ")
        if not os.path.exists(fileName):
                print("File doesn't exist")
        else:
                words = allWords(fileName)
                unique = set(words)
                print("The number of all words: %d" %len(words))
                print("The number of unique words: %d" % len(unique))
result()

