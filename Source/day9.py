## --- Day 9: Disk Fragmenter ---
# @Author : Art3mis
# @Date : 12/12/2024
# @File : day9.py
# @Project: Advent of Code 2024
# @Link : https://adventofcode.com/2024/day/9
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
            continue
        res += elem*i
    return res

start = time.time()

decodedLine, freeIndexes = decode(list(map(int, list(content))))
print(computeSum(moveLeft(decodedLine.copy(), freeIndexes)))
print(f"Execution time : {time.time()-start}")
# Solution for my input : 6463499258318
# Ran in 0.027s on my laptop

## ----- Part #2
# Same as part 1 but move a whole block of numbers to the left instead of one by one

def findFirstBlock(freeIndexes, length):
    # Find the first block of free consecutive indexes of a given length

    blockLength = 0
    firstIndex = 0
    for i, elem in enumerate(freeIndexes):
        if i==0:
            blockLength = 1
            firstIndex = elem
        else:
            if elem == freeIndexes[i-1]+1:
                blockLength += 1
            else:
                blockLength = 1
                firstIndex = elem

        if blockLength == length:
            return firstIndex

    return -1

def findIdInfos(decodedLine):
    # Find for each id in the decoded line, its first index and its length
    # Index of resulting list is the id, value is a list of [firstIndex, length]
    # Ex : [0, 1, 1, 2, 2, 2] -> [[0, 1], [1, 2], [3, 3]]

    # It could have been a bit more efficient to do this in the decode function

    currentValue = decodedLine[0]
    currentLength = 1
    currentFirstIndex = 0
    res = []

    i = 1
    while i < len(decodedLine):
        if decodedLine[i] == currentValue:
            currentLength += 1
        else:
            if currentValue != '.':
                res += [[currentFirstIndex, currentLength]]
            currentValue = decodedLine[i]
            currentLength = 1
            currentFirstIndex = i

        i += 1

    if currentValue != '.':
        res += [[currentFirstIndex, currentLength]]

    return res

def moveLeftBlock(decodedLine, freeIndexes):
    # Move each block of numbers on the right (starting from the right) of decodedLine
    # to the first free block large enough on the left

    idLocations = findIdInfos(decodedLine)
    n = len(idLocations)
    for i, (firstIndex, length) in enumerate(reversed(idLocations)):

        firstPlace = findFirstBlock(freeIndexes, length)
        if firstPlace != -1 and firstPlace < firstIndex:
            for i in range(length):
                decodedLine[firstPlace+i] = decodedLine[firstIndex+i]
                decodedLine[firstIndex+i] = '.'

                freeIndexes.remove(firstPlace+i)
    return decodedLine

start2 = time.time()
print(computeSum(moveLeftBlock(decodedLine.copy(), freeIndexes)))
print(f"Execution time : {time.time()-start2}")
# Solution for my input : 6493634986625 .
# Ran in 2.19s on my laptop