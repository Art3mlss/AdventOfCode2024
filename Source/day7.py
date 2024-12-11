## --- Day 7: Bridge Repair ---
# @Author : Art3mis
# @Date : 11/12/2024
# @File : day7.py
# @Project: Advent of Code 2024
# @Link : https://adventofcode.com/2024/day/7
## ---------------------------

## ----- Accessing Input File
path = "../Resources/"
day = "7"
with open(path+"day"+day+".txt", 'r') as file:
    content = file.read()

## ----- Import Libraries
import time

## ----- Part #1
# Find the number of possibles operations to get the announced number

op = ['+', '*']

def allPossibleCombinations(operands, length):
    # Find all possible combinations of the operands with the specified
    if length == 1:
        return [[operand] for operand in operands]
    else:
        return [[operand] + e for operand in operands for e in allPossibleCombinations(operands, length-1)]

def isTargetAchievable(n, operands):
    # Find whether it is possible to get the number n with the operands and a specific combination of operations

    combinations = allPossibleCombinations(op, len(operands)-1)
    for combination in combinations: # combination = ['+', '*'] // operands = ['1', '2', '3']
        value = operands[0]
        for i in range(len(combination)):
            if combination[i] == '+':
                value += operands[i+1]
            else:
                value *= operands[i+1]

        if value == n:
            return True

    return False

# Count the sum of each number that is possible to get with the operands
start = time.time() # For performance measurement
res = 0
for line in content.split('\n'):
    val, operands = line.split(': ')
    if isTargetAchievable(int(val), list(map(int, operands.split(' ')))):
        res += int(val)

print(res)
print("Execution time : ", time.time()-start)
# Solution for my input : 20665830408335
# Ran in 0.68s on my laptop

## ----- Part #2
# Same question as before but with an additionnal || operator (concatenation)