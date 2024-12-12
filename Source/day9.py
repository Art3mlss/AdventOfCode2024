## --- Day 9: Disk Fragmenter ---
# @Author : Art3mis
# @Date : 11/12/2024
# @File : day8.py
# @Project: Advent of Code 2024
# @Link : https://adventofcode.com/2024/day/8
## ---------------------------

## ----- Accessing Input File
path = "../Resources/"
day = "9"
with open(path+"day"+day+".txt", 'r') as file:
    content = file.read()

## ----- Import Libraries
import time

## ----- Part #1
# Decode input and move to the left of the list, then compute sum
# input : 12345
# decode : 0..111....22222
# moveleft : 022111222......
# ans : 0x0 + 2x1 + 2x2 + 1x3 + 1x4 + 1x5 + 2x6 + 2x7 + 2x8 + 0x9 + ... = output

def decode(line):
    # Decode the input, meaning that we will transform the input into a list of numbers and '.' for free spaces
    # Will also keep track of the free indexes (indexes where we can move numbers later)

    res = []
    resSize = 0
    id = 0
    freeIndexes = []
    for i, elem in enumerate(line):
        if i%2 == 0:
            res += [id]*elem
            id += 1
        else:
            res += ['.']*elem
            freeIndexes += [j for j in range(resSize, resSize+elem)]
        resSize += elem

    return res, freeIndexes

def moveLeft(decodedLine, freeIndexes):
    # Move the numbers to the left of the list at free indexes, starting from the end of the list

    i = len(decodedLine)-1
    j = 0
    while (i >= 0 and j < len(freeIndexes)) and i > freeIndexes[j]:
        # print(f"i : {i} - j : {j} - decodedLine : {decodedLine}") # -- To visiualize the process
        if decodedLine[i] != '.':
            decodedLine[freeIndexes[j]] = decodedLine[i]
            decodedLine[i] = '.'
            j += 1
        i -= 1

    return decodedLine

def computeSum(line):
    # Compute the sum of the line, by multiplying each number by its index and stopping at the first '.'

    res = 0
    for i, elem in enumerate(line):
        if elem == '.':
            break
        res += elem*i
    return res

start = time.time()

decodedLine, freeIndexes = decode(list(map(int, list(content))))
print(computeSum(moveLeft(decodedLine, freeIndexes)))
print(f"Execution time : {time.time()-start}")
# Solution for my input : 6463499258318
# Ran in 0.027s on my laptop