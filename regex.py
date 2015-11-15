#! /usr/bin/python
# Author: Ulas Askan
# Date: 14 Nov 2015
# Python version: 2.7 
# This program takes a text file input by the user in a Linux filesystem and searches for a user input string
# The search simulates Regular expressions. The program can search for text anywhere in the opened file
# the beginning of each line (^) or the end of lines $

import os, re, subprocess 

### User inputs and variable definitions
TheFile = raw_input('Type in the file to search:  ')
while os.path.exists(TheFile) is False:
        print 'Invalid file/folder name, please try again!'
        TheFile = raw_input('Type in the file/folder to search:  ')

Search = raw_input('Type string to search:  ')

print 'Choose an option: \n \ta - Search anywhere in the line \n \t^ - Search beginning of a line \n\t$ - Search end of a line'
option = raw_input('a/^/$:  ')
while option not in ('a', '^', '$'):
        print 'Invalid option!'
        option = raw_input('a/^/$:  ')


### Check if the file is binary
def NonBinary(path):
    return (re.search(r':.* text', subprocess.Popen(["file", '-L', path], stdout=subprocess.PIPE).stdout.read()) is not None)

### Search anywhere option
if option == "a":
    if NonBinary(TheFile):
        with open(TheFile, 'rt') as txt:
            for line in txt:
                if Search in line:
                    print TheFile, ':', line,
    if not os.access(TheFile, os.R_OK):
        print TheFile, ': Permission denied'
  

### Search the beginning of a line option
elif option == "^":
    if NonBinary(TheFile):
        with open(TheFile, 'rt') as txt:
            for line in txt:
                CurrentLine = line
                regex = re.match(Search, CurrentLine)
                if regex:
                    print TheFile, ':', line,
    if not os.access(TheFile, os.R_OK):
        print TheFile, ': Permission denied'
        

### Search the end of a line option
elif option == "$":
    if NonBinary(TheFile):
	with open(TheFile, 'rt') as txt:
            for line in txt:
                CurrentLine = line
                if re.search(Search+r'$', CurrentLine):
                    print TheFile, ':', line,
    if not os.access(TheFile, os.R_OK):
        print TheFile, ': Permission denied'
