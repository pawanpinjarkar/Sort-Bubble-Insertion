#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programming Assignment 1
CSCI B505
Fall 2017
@author: Pawan Pinjarkar
"""

import timeit
import glob, os

#Reads the list with integer numberes and sort the list using bubble sort
def bubbleSort(numberList,inputFileName):
    
    #Get the start time
    start = timeit.default_timer()
    
    #Get the length of the number list
    numberListSize = len(numberList)
 
    # Iterate though all the numbers from the list
    for i in range(numberListSize):
        # Numbers that are already in place
        for j in range(0, numberListSize-i-1):
            # Iterare the list from 0 to n-i-1
            # If current number is greater than the next number then swap 
            if numberList[j] > numberList[j+1] :
                numberList[j], numberList[j+1] = numberList[j+1], numberList[j]
                
    #Get the end time
    stop = timeit.default_timer()
    
    print("Bubble Sort")
    print ("File name : ",inputFileName," ",stop - start)


#Reads the list with integer numberes and sort the list using insertion sort
def insertionSort(numberList,inputFileName):
    
    #Get the start time
    start = timeit.default_timer()
    
    #Get the length of the number list
    numberListSize = len(numberList)
    
    # Iterate though all the numbers from the list
    for i in range(1, numberListSize):
        key = numberList[i]
        # For the numbers which are greater than the key, move the numbers in the list
        #to one position next to their current position
        j = i-1
        while j >=0 and key < numberList[j] :
                numberList[j+1] = numberList[j]
                j -= 1
        numberList[j+1] = key
        
    #Get the end time
    stop = timeit.default_timer()
    
    print("Insertion Sort")
    print ("File name : ",inputFileName," ",stop - start)
    print("*********************************************************************")
    
def main(files):

    #For every file in the list of files, open a file, read the file and add the integer numbers into a list
    for inputFileName in files:
        with open(inputFileName) as inputFile:
            numberList = []
            for line in inputFile:
                line = line.split()
                if line:            
                    try:
                        for i in line:
                            numberList.append(int(i))# Convert string number into int number
                    except ValueError:
                        pass
    
        #Call bubble sort method
        bubbleSort(numberList,inputFileName)
    
        #Call insertion sort method
        insertionSort(numberList,inputFileName)

      
#Program executon begins here
#Read .txt files from the current directory. It is assumed that the data files (*.txt) are kept in the same directory as of source code.
files =[]
#Read the .txt files from the directory and append the filenames into a list
for f in glob.glob("*.txt"):
    files.append(os.getcwd()+"/"+f)

#Print the file names
print(files)

#Call main function
main(files)