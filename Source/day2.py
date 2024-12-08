## --- Day 2: Red-Nosed Reports ---
# @Author : Art3mis
# @Date : 08/12/2024
# @File : day2.py
# @Project: Advent of Code 2024
# @Link : https://adventofcode.com/2024/day/2
## ---------------------------------

## ----- Accessing Input File
path = "../Resources/"
day = "2"
with open(path+"day"+day+".txt", 'r') as file:
    content = file.read()

## ----- Part #1
# Find out if each line of the input is in ascending or descending order (by 1, 2, or 3 steps) or neither

def checkOrder(l):
    # Function to check if a list is in ascending or descending order (by 1, 2, or 3 steps) or neither
    ascending = all(
        (l[i + 1] == l[i] + 1) or
        (l[i + 1] == l[i] + 2) or
        (l[i + 1] == l[i] + 3)
        for i in range(len(l) - 1)
    )
    descending = all(
        (l[i + 1] == l[i] - 1) or
        (l[i + 1] == l[i] - 2) or
        (l[i + 1] == l[i] - 3)
        for i in range(len(l) - 1)
    )
    if ascending:
        return "ascending"
    elif descending:
        return "descending"
    else:
        return "neither"

def isSafe(l):
    return checkOrder(l) != "neither"

safeCount = 0
for report in content.split("\n"):
    report = list(map(int, report.split()))
    if isSafe(report):
        safeCount += 1

print(safeCount)
# Solution for my input : 314

## ----- Part #2
# Find out if each line of the input is in ascending or descending order (by 1, 2, or 3 steps) by removing exactly one
# item or if it is not possible

def listWithoutIndex(l, index):
    return [l[i] for i in range(len(l)) if i != index]

def robustCheckOrder(l):
    # Function to check if a list is in ascending or descending order (by 1, 2, or 3 steps) by removing exactly one item
    return any(isSafe(listWithoutIndex(l, i)) for i in range(len(l)))

safeCountBis = 0
for report in content.split("\n"):
    report = list(map(int, report.split()))
    if robustCheckOrder(report):
        safeCountBis += 1

print(safeCountBis)
# Solution for my input : 373