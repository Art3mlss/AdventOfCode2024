## --- Day 8: Resonant Collinearity ---
# @Author : Art3mis
# @Date : 11/12/2024
# @File : day8.py
# @Project: Advent of Code 2024
# @Link : https://adventofcode.com/2024/day/8
## ---------------------------

## ----- Accessing Input File
path = "../Resources/"
day = "8"
with open(path+"day"+day+".txt", 'r') as file:
    content = file.read()

## ----- Import Libraries
import time

## ----- Part #1
# Find the symmetry of each pair of the same character in the input grid

def findSymmetry(x1, y1, x2, y2):
    # find the symmetric point of (x1, y1) with respect to (x2, y2)
    return 2*x2-x1, 2*y2-y1

# Find the position of each occurence of the same character in the grid
start = time.time() # For performance measurement
pos = {}
for i, row in enumerate(content.split('\n')):
    for j, cell in enumerate(row):
        if cell == '.':
            continue
        if cell in pos:
            pos[cell].append((i, j))
        else:
            pos[cell] = [(i, j)]

# Find the symmetries of each pair of the same character
symmetries = set()
for key in pos:
    for i, (x1, y1) in enumerate(pos[key]):
        for j, (x2, y2) in enumerate(pos[key]):
            if i != j:
                sx, sy = findSymmetry(x1, y1, x2, y2)
                if 0 <= sx < len(content.split('\n')) and 0 <= sy < len(content.split('\n')[0]):
                    symmetries.add((sx, sy))

print(len(symmetries))
print("Execution time : ", time.time()-start)
# Solution for my input : 271
# Ran in 0.003s on my laptop

## ----- Part #2
# Same as before, but it now repeats over the whole line of symmetry

def findDifference(x1, y1, x2, y2):
    # find the difference dx, dy of x and y (can be negative)
    return x2-x1, y2-y1

start2 = time.time() # For performance measurement

# Same as before, but it now repeats over the whole line of symmetry
symmetriesLines = set()
for key in pos:
    for i, (x1, y1) in enumerate(pos[key]):
        for j, (x2, y2) in enumerate(pos[key]):
            if i != j:
                dx, dy = findDifference(x1, y1, x2, y2)
                sx, sy = x2, y2
                while 0 <= sx < len(content.split('\n')) and 0 <= sy < len(content.split('\n')[0]):
                    symmetriesLines.add((sx, sy))
                    sx += dx
                    sy += dy

print(len(symmetriesLines))
print("Execution time : ", time.time()-start2)
# Solution for my input : 994
# Ran in 0.017s on my laptop