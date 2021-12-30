#!/usr/bin/env python3

import os

'''This function search all the words in the file'''

FILTER_SYMS = ',.?!'

def all_words(file_name):

        with open(file_name, encoding="utf8") as file:
                read_file = file.read()
        no_line_break = read_file.replace("\n", " ")
                
        text = no_line_break.lower()
        words = text.split()
	
        for i in FILTER_SYMS.split():
                if i in words:
                        words = words.replace(i, "")

        return words


def result():

        '''This function contains
                - inputting the file path
                - calling the allWords defined functions
                - outputting all statistics
        '''
        
        file_name = input("Specify the file path: ")
        if not os.path.exists(file_name):
                print("File doesn't exist")
        else:
                words = all_words(file_name)
                unique = set(words)
                print("The number of all words: %d" %len(words))
                print("The number of unique words: %d" % len(unique))
result()

